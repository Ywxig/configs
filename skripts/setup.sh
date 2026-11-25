#!/usr/bin/env bash

set -u

# Список пакетов по умолчанию (можно передать свои аргументами при запуске)
DEFAULT_PACKAGES=(
    git
    htop
    niri
    fuzzel
    waybar
    awww
    kitty
    mako
    gtklock
    fastfetch
    cava
    alacritty
)

# Если переданы аргументы командной строки — используем их
if [ "$#" -gt 0 ]; then
    PACKAGES=("$@")
else
    PACKAGES=("${DEFAULT_PACKAGES[@]}")
fi

# Проверяем, что скрипт запущен на системе с pacman
if ! command -v pacman >/dev/null 2>&1; then
    echo "Ошибка: pacman не найден. Этот скрипт предназначен для Arch Linux и производных дистрибутивов." >&2
    exit 1
fi

# Определяем команду для повышения прав (sudo или doas)
if [ "$(id -u)" -eq 0 ]; then
    PRIV=""
elif command -v sudo >/dev/null 2>&1; then
    PRIV="sudo"
elif command -v doas >/dev/null 2>&1; then
    PRIV="doas"
else
    echo "Ошибка: нужны права root, но не найдены ни sudo, ни doas." >&2
    exit 1
fi

to_install=()
missing_pkgs=()

echo "Проверяем пакеты..."

for pkg in "${PACKAGES[@]}"; do
    # Проверяем, установлен ли уже пакет
    if pacman -Qi "$pkg" >/dev/null 2>&1; then
        echo "  [уже установлен] $pkg"
    # Проверяем, существует ли пакет в синхронизированных репозиториях
    elif pacman -Si "$pkg" >/dev/null 2>&1; then
        echo "  [к установке]     $pkg"
        to_install+=("$pkg")
    else
        echo "  [не найден]       $pkg"
        missing_pkgs+=("$pkg")
    fi
done

if [ "${#missing_pkgs[@]}" -gt 0 ]; then
    echo ""
    echo "Внимание: следующие пакеты не найдены в репозиториях (возможно, они в AUR):"
    printf '  - %s\n' "${missing_pkgs[@]}"
fi

if [ "${#to_install[@]}" -eq 0 ]; then
    echo ""
    echo "Нечего устанавливать."
    exit 0
fi

echo ""
echo "Обновляем базы пакетов и устанавливаем: ${to_install[*]}"

# Сначала обновляем базы (-Sy), затем ставим пакеты (--needed защищает от повторной установки)
if ! $PRIV pacman -Sy --needed "${to_install[@]}"; then
    echo "Ошибка при установке пакетов." >&2
    exit 1
fi

echo "Готово!"
