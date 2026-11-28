#!/usr/bin/env python3
"""Общее хранилище истории буфера обмена.

Используется демоном clipboard-daemon и интерфейсом clipboard-ui.
Файл истории — обычный JSON, доступ к нему сериализуется flock-блокировкой.
"""

import contextlib
import fcntl
import json
import os
import tempfile
import time

CACHE_DIR = os.path.expanduser(
    os.environ.get("CLIPBOARD_HISTORY_DIR", "~/.cache/clipboard-history")
)
HISTORY_FILE = os.path.join(CACHE_DIR, "history.json")
LOCK_FILE = os.path.join(CACHE_DIR, "history.lock")

MAX_ENTRIES = int(os.environ.get("CLIPBOARD_HISTORY_MAX", "300"))
MAX_TEXT = int(os.environ.get("CLIPBOARD_HISTORY_MAX_TEXT", "200000"))


def _ensure_dir():
    os.makedirs(CACHE_DIR, mode=0o700, exist_ok=True)


@contextlib.contextmanager
def locked():
    """Межпроцессная блокировка на время чтения-изменения-записи."""
    _ensure_dir()
    fd = os.open(LOCK_FILE, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def load():
    """Возвращает список записей, новые сверху."""
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []

    entries = data.get("entries", []) if isinstance(data, dict) else []
    result = []
    for item in entries:
        if not isinstance(item, dict):
            continue
        text = item.get("text")
        if not isinstance(text, str) or not text.strip():
            continue
        try:
            ts = int(item.get("time", 0))
        except (TypeError, ValueError):
            ts = 0
        result.append({"text": text, "time": ts})
    return result


def save(entries):
    """Атомарно записывает историю."""
    _ensure_dir()
    data = {"version": 1, "entries": entries[:MAX_ENTRIES]}
    fd, tmp = tempfile.mkstemp(dir=CACHE_DIR, prefix=".history.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(tmp, 0o600)
        os.replace(tmp, HISTORY_FILE)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def add(text, timestamp=None):
    """Добавляет текст, поднимая дубликат наверх."""
    if not text or not text.strip():
        return False

    text = text.replace("\x00", "")
    if len(text) > MAX_TEXT:
        text = text[:MAX_TEXT]

    with locked():
        entries = load()
        entries = [e for e in entries if e["text"] != text]
        entries.insert(0, {"text": text, "time": int(timestamp or time.time())})
        save(entries)
    return True


def remove(text):
    with locked():
        entries = [e for e in load() if e["text"] != text]
        save(entries)


def clear():
    with locked():
        save([])


def count():
    return len(load())
