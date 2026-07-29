# 🕐 Sticky Clock

A lightweight always-on-top analog clock with a built-in countdown timer — designed for full-screen workflows where you can't afford to minimize your window just to check the time.

---

## Why This Exists

When you're gaming, coding, editing video, or doing anything in full-screen mode, checking the time means breaking your focus. Sticky Clock sits pinned to the top-left corner of your screen, always visible, always on top — no matter what's open underneath it.

---

## Features

- **Analog clock** with hour, minute, and second hands
- **Always on top** — floats above every window including full-screen apps
- **Pinned to top-left corner** so it never gets in the way
- **Countdown timer** with Start, Pause/Resume, and Reset
- **Alert when timer ends** — plays a beep and shows a popup
- Lightweight — no background services, no tray icon, no bloat

---



---

## Getting Started

### Option 1 — Run the EXE (Windows, no setup needed)

1. Go to the [`dist/`](./dist) folder
2. Download `StickyClock.exe`
3. Double-click it — done

> **Note:** Windows Defender or your antivirus may flag it. This is normal for PyInstaller-built executables. It's safe to allow it.

### Option 2 — Run from source (requires Python)

**Requirements:** Python 3.x (tkinter is included by default)

```bash
git clone https://github.com/IoNiCx1/Sticky-Clock.git
cd Sticky-Clock
python clock.py
```

---

## How to Use

**Clock** — starts automatically on launch. It reads your system time, so it's always accurate.

**Countdown Timer:**
1. Type a number of minutes in the input box
2. Click **Start**
3. Click **Pause** to pause, then **Resume** to continue
4. Click **Reset** to clear it
5. When time runs out, a beep plays and a popup appears

---

## Build the EXE Yourself

If you want to rebuild the executable from source:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "StickyClock" --icon=clock.ico clock.py
```

The output will be in the `dist/` folder.

---

## Project Structure

```
Sticky-Clock/
├── clock.py        # Main application
├── clock.ico       # App icon
├── clock.spec      # PyInstaller build config
├── dist/           # Pre-built Windows executable
└── LICENSE         # MIT License
```

---

## Tech Stack

- **Python 3** — core language
- **tkinter** — GUI and canvas drawing
- **math / time** — clock hand calculations and system time
- **PyInstaller** — packages everything into a single `.exe`

---

## License

MIT — free to use, modify, and distribute. See [LICENSE](./LICENSE) for details.

---

*Built by [Omkar Mishra](https://github.com/IoNiCx1)*
