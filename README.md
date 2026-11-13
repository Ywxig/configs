<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1f16ad90-67db-4adb-bda0-0889e557d520" />

# 🗺️ Arch Rice — niri + waybar

Конфиги Arch Linux на композиторе **niri** (scrollable-tiling Wayland) с панелью **waybar**,
лаунчером **fuzzel** и терминалом **kitty**. Репозиторий лежит прямо в `~/.config`.

---

## 1. 📦 Что лежит в репозитории

| Путь | Что это |
|---|---|
| `niri/` | Конфиг композитора niri (биндинги, анимации, layout) |
| `waybar/` | Бар: `config` (модули), `style.css` (тема), `cava.sh`, `window_pill.py` |
| `kitty/` | Терминал kitty |
| `alacritty/` | Терминал alacritty (запасной) |
| `fuzzel/` | Лаунчер приложений |
| `mako/` | Уведомления |
| `cava/` | Аудио-визуализатор + свои шейдеры и темы |
| `fastfetch/` | Нейофetch + логотипы Arch |
| `gtklock/` | Экран блокировки (config + стиль) |
| `README.md` | Этот файл |

> ⚠️ Скрипты бара — `~/.local/bin/fuzzel-powermenu` и `~/.local/bin/poweroff-confirm` —
> в репозитории не лежат. Если переносишь конфиги на другую машину, скопируй их отдельно.

---

## 2. 🧩 Используемые пакеты

### Композитор и сессия

| Пакет | Зачем | Команда |
|---|---|---|
| niri | Композитор Wayland | `pacman -S niri` |
| xwayland-satellite | Поддержка X11-приложений | `pacman -S xwayland-satellite` |
| xdg-desktop-portal-gnome | Порталы (скриншоты, пипетка и т.д.) | `pacman -S xdg-desktop-portal-gnome` |
| xsettingsd | Настройки тем для GTK-приложений | `pacman -S xsettingsd` |
| nwg-look | GUI-настройка GTK-тем | `pacman -S nwg-look` |
| sddm | Экран входа | `pacman -S sddm` |
| plymouth-kcm / breeze-plymouth | Заставка при загрузке | `pacman -S plymouth-kcm breeze-plymouth` |

### Бар и рабочий стол

| Пакет | Зачем | Команда |
|---|---|---|
| waybar | Статус-бар | `pacman -S waybar` |
| fuzzel | Лаунчер | `pacman -S fuzzel` |
| mako | Уведомления | `pacman -S mako` |
| gtklock | Экран блокировки | `pacman -S gtklock` |
| grim + slurp | Скриншоты | `pacman -S grim slurp` |
| wl-clipboard | Буфер обмена | `pacman -S wl-clipboard` |
| brightnessctl | Яркость | `pacman -S brightnessctl` |
| cava | Аудио-визуализатор для бара | `pacman -S cava` |
| network-manager-applet | Апплет сети (+ nm-connection-editor) | `pacman -S network-manager-applet` |
| blueman | Bluetooth-менеджер | `pacman -S blueman` |

### Терминал и CLI

| Пакет | Зачем | Команда |
|---|---|---|
| kitty | Основной терминал | `pacman -S kitty` |
| alacritty | Второй терминал | `pacman -S alacritty` |
| zsh (+ autosuggestions, syntax-highlighting) | Shell | `pacman -S zsh zsh-autosuggestions zsh-syntax-highlighting` |
| neovim / emacs-wayland | Редакторы | `pacman -S neovim emacs-wayland` |
| fastfetch | Нейофетч | `pacman -S fastfetch` |
| btop / htop / nvtop | Мониторы | `pacman -S btop htop nvtop` |
| ttyper / sl | Забавы ради | `pacman -S ttyper sl` |

### Система и железо

| Пакет | Зачем | Команда |
|---|---|---|
| keyd | Кастомные раскладки/бинды на уровне ядра | `pacman -S keyd` |
| tlp + tlpui | Экономия батареи (GUI) | `pacman -S tlp tlpui` |
| auto-cpufreq | Автотурбo CPU | `yay -S auto-cpufreq` |
| zram-generator | Сжатый swap в RAM | `pacman -S zram-generator` |
| fwupd / smartmontools | Фirmware и здоровье дисков | `pacman -S fwupd smartmontools` |
| gnome-keyring + seahorse | Хранилище ключей/паролей | `pacman -S gnome-keyring seahorse` |
| iwd | Wi-Fi бэкенд | `pacman -S iwd` |
| docker + docker-compose | Контейнеры | `pacman -S docker docker-compose` |
| yay | AUR-хелпер | `pacman -S yay` |
| flatpak | Песочница-приложения | `pacman -S flatpak` |

### Шрифты

| Пакет | Зачем | Команда |
|---|---|---|
| ttf-nerd-fonts-symbols | Иконки в waybar | `pacman -S ttf-nerd-fonts-symbols` |
| ttf-jetbrains-mono-nerd | Шрифт бара (рекомендую — ещё не установлен!) | `pacman -S ttf-jetbrains-mono-nerd` |
| ttf-fira-code | Моноширинный с лигатурами | `pacman -S ttf-fira-code` |
| noto-fonts-emoji | Эмодзи (флаги языка и т.д.) | `pacman -S noto-fonts-emoji` |
| noto-fonts-cjk / noto-fonts-extra | Азиатские и дополнительные глифы | `pacman -S noto-fonts-cjk noto-fonts-extra` |
| ttf-liberation / ttf-dejavu | Классические метрики | `pacman -S ttf-liberation ttf-dejavu` |
| ttf-ms-fonts | Windows-шрифты | `yay -S ttf-ms-fonts` |

### Приложения

| Пакет | Зачем | Команда |
|---|---|---|
| firefox | Браузер | `pacman -S firefox` |
| obsidian | Заметки | `pacman -S obsidian` |
| discord / telegram-desktop | Мессенджеры | `pacman -S discord telegram-desktop` |
| qbittorrent | Торренты | `pacman -S qbittorrent` |
| onlyoffice-bin | Офис | `yay -S onlyoffice-bin` |
| gimp / krita / inkscape / audacity | Графика и звук | `pacman -S gimp krita inkscape audacity` |
| krita-plugin-gmic | Плагин фильтров для Krita/GIMP | `pacman -S krita-plugin-gmic` |
| ark / gwenview | Архиватор / просмотр картинок (KDE) | `pacman -S ark gwenview` |
| qalculate-gtk / pavucontrol / easyeffects / helvum | Калькулятор и аудио | `pacman -S qalculate-gtk pavucontrol easyeffects helvum` |
| foliate / ghostwriter | Читалка / Markdown-редактор | `pacman -S foliate ghostwriter` |
| dbeaver | Базы данных | `pacman -S dbeaver` |
| ppsspp | Эмулятор PSP | `pacman -S ppsspp` |
| ollama / opencode | Локальные LLM и AI-агент | `pacman -S ollama opencode` |

### AUR (через yay)

```sh
yay -S auto-cpufreq onlyoffice-bin nirimod-ru-git sddm-sugar-dark ttf-ms-fonts game-devices-udev
```

> `nirimod-ru-git` — GTK-конфигуратор для niri с русским переводом.

### Flatpak

```sh
flatpak install flathub com.valvesoftware.Steam   # Steam
flatpak install flathub dev.zed.Zed               # Zed (редактор)
flatpak install flathub org.videolan.VLC          # VLC
flatpak install flathub org.vinegarhq.Sober       # Roblox
flatpak install flathub org.pvermeer.WebAppHub    # Web-приложения
flatpak install flathub ru.linux_gaming.PortProton# PortProton (wine-игры)
```

### Сервисы (systemd)

| Сервис | Команда |
|---|---|
| sddm (экран входа) | `systemctl enable sddm` |
| NetworkManager | `systemctl enable NetworkManager` |
| bluetooth | `systemctl enable bluetooth` |
| tlp | `systemctl enable tlp` |
| keyd | `systemctl enable keyd` |
| auto-cpufreq | `systemctl enable auto-cpufreq` |

> ⚠️ `tlp` и `auto-cpufreq` одновременно — потенциальный конфликт управления питанием.
> Сейчас включены оба; если батареи хватает, лучше оставить один из них.

---

## 3. 🎨 Палитра

Базовая тема — **Tokyo Night** (waybar, fuzzel, gtklock), терминал kitty — **Catppuccin Mocha**.

| Цвет | HEX | Использование |
|---|---|---|
| <img src="https://placehold.co/40x14/2b2b2b/2b2b2b.png" width="40"/> | `#2b2b2b` | Фон бара |
| <img src="https://placehold.co/40x14/1a1b26/1a1b26.png" width="40"/> | `#1a1b26` | Фон «островков» (bg) |
| <img src="https://placehold.co/40x14/c0caf5/c0caf5.png" width="40"/> | `#c0caf5` | Основной текст (fg) |
| <img src="https://placehold.co/40x14/565f89/565f89.png" width="40"/> | `#565f89` | Приглушённый текст (muted) |
| <img src="https://placehold.co/40x14/7aa2f7/7aa2f7.png" width="40"/> | `#7aa2f7` | Акцент 1 (accent) |
| <img src="https://placehold.co/40x14/7dcfff/7dcfff.png" width="40"/> | `#7dcfff` | Акцент 2 (accent2) |
| <img src="https://placehold.co/40x14/f2555a/f2555a.png" width="40"/> | `#f2555a` | Ошибки/критичное (red) |
| <img src="https://placehold.co/40x14/a6e3a1/a6e3a1.png" width="40"/> | `#a6e3a1` | Успех/зарядка (green) |
| <img src="https://placehold.co/40x14/f9e2af/f9e2af.png" width="40"/> | `#f9e2af` | Предупреждение (yellow) |
| <img src="https://placehold.co/40x14/172c43/172c43.png" width="40"/> | `#172c43` | Фон gtklock |
| <img src="https://placehold.co/40x14/1e1e2e/1e1e2e.png" width="40"/> | `#1e1e2e` | Фон kitty (Catppuccin Mocha) |

---

## 4. 🚀 Установка с нуля (алгоритм)

> Репозиторий — это сам `~/.config`, поэтому клонировать нужно прямо туда.

**Шаг 0.** Бэкап старого конфига, если он есть:

```sh
mv ~/.config ~/.config.bak
```

**Шаг 1.** Клонировать репозиторий:

```sh
git clone git@github.com:Ywxig/configs.git ~/.config
# или по HTTPS:
# git clone https://github.com/Ywxig/configs.git ~/.config
```

**Шаг 2.** Поставить пакеты из официальных репозиториев:

```sh
sudo pacman -S --needed \
  niri xwayland-satellite xdg-desktop-portal-gnome xsettingsd nwg-look sddm \
  plymouth-kcm breeze-plymouth waybar fuzzel mako gtklock grim slurp wl-clipboard \
  brightnessctl network-manager-applet blueman cava \
  kitty alacritty zsh zsh-autosuggestions zsh-syntax-highlighting neovim emacs-wayland \
  fastfetch btop htop nvtop ttyper sl \
  keyd tlp tlp-pd tlp-rdw tlpui zram-generator fwupd smartmontools \
  gnome-keyring seahorse iwd docker docker-compose git yay flatpak \
  ttf-nerd-fonts-symbols ttf-jetbrains-mono-nerd ttf-fira-code noto-fonts-emoji \
  noto-fonts-cjk noto-fonts-extra ttf-liberation ttf-dejavu \
  firefox obsidian discord telegram-desktop qbittorrent ppsspp \
  gimp krita krita-plugin-gmic inkscape audacity ark gwenview \
  qalculate-gtk pavucontrol easyeffects helvum foliate ghostwriter dbeaver \
  ollama opencode pacman-contrib reflector handlr-regex xdg-utils
```

**Шаг 3.** Поставить AUR-пакеты:

```sh
yay -S auto-cpufreq onlyoffice-bin nirimod-ru-git sddm-sugar-dark ttf-ms-fonts game-devices-udev
```

**Шаг 4.** Flatpak-приложения (по желанию):

```sh
flatpak install flathub com.valvesoftware.Steam dev.zed.Zed org.videolan.VLC \
  org.vinegarhq.Sober org.pvermeer.WebAppHub ru.linux_gaming.PortProton
```

**Шаг 5.** Скопировать скрипты бара (их нет в репо):

```sh
mkdir -p ~/.local/bin
# перенеси fuzzel-powermenu и poweroff-confirm в ~/.local/bin
chmod +x ~/.local/bin/fuzzel-powermenu ~/.local/bin/poweroff-confirm
```

**Шаг 6.** Включить сервисы:

```sh
sudo systemctl enable sddm NetworkManager bluetooth tlp keyd auto-cpufreq
```

**Шаг 7.** Указать zsh как shell (если ещё не так) и перезагрузиться:

```sh
chsh -s /bin/zsh
reboot
```

После входа через **SDDM** выбирается сессия **niri** — и рис готов. 🎉

---

## 5. 🔄 Обновление конфигов

```sh
git -C ~/.config pull
```

Waybar перечитывает `style.css` сам; после правки `config` перезапусти бар:

```sh
pkill waybar && niri msg action spawn waybar
```
