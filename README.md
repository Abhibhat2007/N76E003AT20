# Nuvoton N76E003 Arduino Core & Board Package

Arduino Board Package for the **Nuvoton N76E003** (1T 8051 microcontroller). Write standard Arduino code (`pinMode`, `digitalWrite`, `analogRead`, `Serial`, `delay`) inside **Arduino IDE 1.8.x or 2.x** and upload directly over USB (CH340 / CP2102) using the built-in UART ISP bootloader.

---

## Table of Contents
1. [Prerequisites](#1-prerequisites)
2. [Installation via Arduino Boards Manager](#2-installation-via-arduino-boards-manager)
3. [Uploading Your First Sketch](#3-uploading-your-first-sketch)
4. [Board Pinout & Sensor Cheat Sheet](#4-board-pinout--sensor-cheat-sheet)
5. [Example Sketches](#5-example-sketches)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. Prerequisites

Before uploading sketches, ensure your computer has the following installed:

### 1.1 SDCC Compiler (Small Device C Compiler)
The N76E003 uses the 8051 architecture and requires SDCC to compile:
- **Windows**:
  - Open PowerShell as Administrator and run:
    ```powershell
    winget install SDCC.SDCC
    ```
  - Or download the Windows installer from [SourceForge SDCC](https://sourceforge.net/projects/sdcc/files/).
  - Verify by opening a new Command Prompt / PowerShell and running:
    ```cmd
    sdcc --version
    ```
    *(Ensure SDCC is in your system `PATH`)*

### 1.2 Python & PySerial
The USB upload tool uses Python with `pyserial`:
- **Windows**:
  - Install Python from [python.org](https://www.python.org/) (ensure **"Add Python to PATH"** is checked during installation).
  - Open terminal and install `pyserial`:
    ```cmd
    pip install pyserial
    ```

---

## 2. Installation via Arduino Boards Manager

To install this board package in Arduino IDE:

1. Open **Arduino IDE**.
2. Go to **File -> Preferences** (or press `Ctrl + ,`).
3. In the **Additional Boards Manager URLs** field, paste the following URL:
   ```text
   https://raw.githubusercontent.com/Abhibhat2007/N76E003AT20/main/package_nuvoton_n76e003_index.json
