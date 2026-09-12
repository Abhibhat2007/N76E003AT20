# Nuvoton N76E003 Arduino Core & Board Package

Arduino Board Package for the **Nuvoton N76E003** (1T 8051 microcontroller). Write standard Arduino code (`pinMode`, `digitalWrite`, `analogRead`, `Serial`, `delay`) inside **Arduino IDE 1.8.x or 2.x** and upload directly over USB (CH340 / CP2102) using the built-in UART ISP bootloader.

---

## Table of Contents
1. [Prerequisites](#1-prerequisites)
2. [Installation via Arduino Boards Manager (Recommended)](#2-installation-via-arduino-boards-manager-recommended)
3. [Manual / Offline Installation](#3-manual--offline-installation)
4. [Uploading Your First Sketch](#4-uploading-your-first-sketch)
5. [Board Pinout & Sensor Cheat Sheet](#5-board-pinout--sensor-cheat-sheet)
6. [Example Sketches](#6-example-sketches)
7. [How to Publish to GitHub & Create Releases](#7-how-to-publish-to-github--create-releases)
8. [Troubleshooting](#8-troubleshooting)

---

## 1. Prerequisites

Before uploading sketches, make sure your computer has the following installed:

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
  - Install Python from [python.org](https://www.python.org/) (ensure **"Add Python to PATH"** is checked).
  - Open terminal and install `pyserial`:
    ```cmd
    pip install pyserial
    ```

---

## 2. Installation via Arduino Boards Manager (Recommended)

To install this board package on any computer running Arduino IDE:

1. Open **Arduino IDE**.
2. Go to **File -> Preferences** (or press `Ctrl + ,`).
3. Find the **Additional Boards Manager URLs** field.
4. Add the following URL (if you already have URLs there, separate them with a comma or click the icon next to the field to add a new line):
   ```text
   https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/arduino-n76e003/main/package_nuvoton_n76e003_index.json
   ```
   *(Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username once uploaded).*
5. Click **OK**.
6. Open **Tools -> Board -> Boards Manager...** (or click the Boards icon on the left sidebar in Arduino IDE 2.x).
7. Type `N76E003` in the search bar.
8. Click **Install**.
9. Once installation finishes, close the Boards Manager!

---

## 3. Manual / Offline Installation

If you don't have an internet connection or prefer not to use GitHub:

1. Locate your Arduino sketchbook directory:
   - On Windows: `C:\Users\<YourUsername>\Documents\Arduino\`
2. Inside that directory, open (or create) the `hardware` folder:
   `Documents\Arduino\hardware\`
3. Copy the `nuvoton` folder into it so the structure looks like:
   ```text
   Documents/
     └── Arduino/
           └── hardware/
                 └── nuvoton/
                       └── 8051/
                             ├── boards.txt
                             ├── platform.txt
                             ├── cores/
                             ├── variants/
                             └── tools/
   ```
4. Restart Arduino IDE. The board will appear under **Tools -> Board -> Nuvoton N76E003 Boards**.

---

## 4. Uploading Your First Sketch

### 4.1 Select Board & Settings
In Arduino IDE:
1. **Tools -> Board -> Nuvoton N76E003 Boards -> Nuvoton N76E003 (TSSOP20/QFN20)**.
2. **Tools -> Upload Method -> Serial Bootloader (UART ISP)**.
3. **Tools -> Clock Frequency -> 16 MHz (Internal HIRC)**.
4. **Tools -> Port -> COMx** (Select your CH340 USB COM port, e.g., `COM11`).

### 4.2 Test Blink Sketch
Copy and paste this code:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Built-in LED on P1.2
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

### 4.3 Upload
1. Click the **Upload** button (`->`).
2. The bottom terminal will display:
   ```text
   Connecting to N76E003 on COM11...
   >>> IF NOT AUTO-CONNECTING: PRESS THE RESET BUTTON ON YOUR BOARD NOW <<<
   ```
3. If your board does not auto-reset, **press the physical red `RESET` button on your board once**.
4. The flasher will report:
   ```text
   [INFO] Connected to N76E003 ISP bootloader successfully!
   [INFO] Device ID detected: 0x3650 (N76E003)
   Flashing: [====================] 100%
   [SUCCESS] Firmware launched! N76E003 is now running your sketch.
   ```
5. Your on-board `LED(P1.2)` is now blinking!

---

## 5. Board Pinout & Sensor Cheat Sheet

Pin mapping for the **PARAS N76E003** breakout board:

| Board Silkscreen | Arduino Pin Name | Hardware Function | Notes |
|---|---|---|---|
| **`LED(P1.2)`** | `LED_BUILTIN` or `8` or `P1_2` | User LED / GPIO | Built-in LED on board |
| **`P0.5`** | `A0` or `14` | 12-bit ADC Input (AIN1) | 0 to 4095 reading |
| **`P0.4`** | `A1` or `15` | 12-bit ADC Input (AIN2) | 0 to 4095 reading |
| **`PWM5P0.3`** | `A2` or `13` or `PIN_D13` | ADC Input (AIN3) / PWM / GPIO | Digital 13 |
| **`PWM4P0.1`** | `A3` or `12` or `PIN_D12` | ADC Input (AIN4) / PWM / GPIO | Digital 12 |
| **`PWM3P0.0`** | `A4` or `11` or `PIN_D11` | ADC Input (AIN5) / PWM / GPIO | Digital 11 |
| **`PWM2P1.0`** | `A5` or `10` or `PIN_D10` | ADC Input (AIN6) / PWM / GPIO | Digital 10 |
| **`PWM1P1.1`** | `A6` or `9` or `PIN_D9` | ADC Input (AIN7) / PWM / GPIO | Digital 9 |
| **`P0.6TX`** | `1` or `PIN_D1` (or `A7`) | Serial TX (UART0) | To CH340 RX |
| **`P0.7RX`** | `0` or `PIN_D0` | Serial RX (UART0) | To CH340 TX |
| **`SCLP1.3`** | `7` or `PIN_D7` | GPIO / Hardware I2C SCL | Wire bus |
| **`SDAP1.2`** | `8` or `PIN_D8` | GPIO / Hardware I2C SDA | Wire bus |
| **`P1.4`** | `6` or `PIN_D6` | GPIO / SPI CLK | SPI bus |
| **`P1.5PWM5`**| `5` or `PIN_D5` | GPIO / PWM | |
| **`P1.6`** | `4` or `PIN_D4` | GPIO | |
| **`P1.7`** | `3` or `PIN_D3` | GPIO / External INT1 | Interrupts |
| **`P3.0`** | `2` or `PIN_D2` | GPIO / External INT0 | Interrupts |
| **`+5V` / `+3V` / `GND`** | Power Rails | Power supplies for sensors | Up to 500mA USB |

---

## 6. Example Sketches

### 6.1 Reading an Analog Sensor with Serial Monitor
Connect an analog sensor (Potentiometer, LDR light sensor, or LM35 temperature sensor) to `P0.5` (`A0`), and power pins to `+5V` and `GND`:

```cpp
void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(A0); // Returns 0 to 4095 (12-bit ADC)
  
  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);
  
  delay(500);
}
```
*(Open the Arduino Serial Monitor at **115200 baud** to view live data).*

### 6.2 Digital Sensor (Button / PIR / Obstacle Sensor)
Connect sensor signal to pin `3` (`P1.7`):

```cpp
const int sensorPin = 3;

void setup() {
  pinMode(sensorPin, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int state = digitalRead(sensorPin);
  
  if (state == HIGH) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
```

---

## 7. How to Publish to GitHub & Create Releases

Follow these steps to publish this repository so anyone in the world can install it via the Boards Manager URL.

### Step 7.1: Create GitHub Repository
1. Go to [github.com/new](https://github.com/new).
2. Repository name: `arduino-n76e003` (or `n76e003-arduino`).
3. Set to **Public**.
4. Do **not** initialize with README or license (we already have them).
5. Click **Create repository**.

### Step 7.2: Push Files to GitHub
Open a terminal in this directory and push:

```bash
git init
git add .
git commit -m "Initial release of Nuvoton N76E003 Arduino core"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/arduino-n76e003.git
git push -u origin main
```

### Step 7.3: Build the Release Archive
Whenever you make updates to the core, run the build script:

```bash
python build_package.py --user YOUR_GITHUB_USERNAME --repo arduino-n76e003
```
This script:
1. Packages the core into `n76e003-arduino-1.0.0.zip`.
2. Automatically calculates the exact **SHA-256 checksum** and **file size**.
3. Updates `package_nuvoton_n76e003_index.json` with the new hash, size, and download URL.

Commit the updated JSON:
```bash
git add package_nuvoton_n76e003_index.json
git commit -m "Update package index for v1.0.0"
git push
```

### Step 7.4: Create GitHub Release
1. In your GitHub repository, click **Releases** (right sidebar) -> **Create a new release**.
2. Click **Choose a tag**, type `v1.0.0`, and click **Create new tag**.
3. Release title: `v1.0.0 - Initial Release`
4. Drag and drop `n76e003-arduino-1.0.0.zip` into the **Attach binaries by dropping them here or selecting them** box.
5. Click **Publish release**.

### Step 7.5: Done!
Your Boards Manager URL is ready to share:
```text
https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/arduino-n76e003/main/package_nuvoton_n76e003_index.json
```

---

## 8. Troubleshooting

### Q1: `[ERROR] pyserial is required`
Run in terminal:
```cmd
pip install pyserial
```

### Q2: `Connection timeout! N76E003 did not enter ISP mode`
- Make sure you selected the correct COM port under **Tools -> Port**.
- Ensure you press the physical red **`RESET`** button on your board while the script says `Connecting to N76E003 on COMx...`.

### Q3: `sdcc: command not found`
- Install SDCC and restart your terminal / Arduino IDE.
- Make sure `C:\Program Files\SDCC\bin` (or `C:\Project_n76e003\sdcc\bin`) is in your Windows User `PATH`.

### Q4: Code uploads but LED doesn't blink
- Check pin mapping: On the PARAS board, the user LED is on `P1.2` (`LED_BUILTIN` or pin `8`).
- Give the red **`RESET`** button a quick press after upload finishes.
