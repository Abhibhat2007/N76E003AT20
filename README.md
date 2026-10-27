# Nuvoton N76E003 Arduino Core & Board Package

Arduino Board Package for the **Nuvoton N76E003** (1T 8051 microcontroller). Write standard Arduino code (`pinMode`, `digitalWrite`, `analogRead`, `analogWrite`, `Serial`, `delay`) inside **Arduino IDE 1.8.x or 2.x** and upload directly over USB (CH340 / CP2102) using the built-in UART ISP bootloader.

---

## Table of Contents
1. [Prerequisites](#1-prerequisites)
   - [1.1 SDCC Compiler (8051 C Compiler)](#11-sdcc-compiler-8051-c-compiler)
   - [1.2 Python & PySerial (With App Execution Alias Fix)](#12-python--pyserial)
   - [1.3 CH340 USB Drivers](#13-ch340-usb-drivers)
2. [Installation via Arduino Boards Manager](#2-installation-via-arduino-boards-manager)
3. [Uploading Your First Sketch](#3-uploading-your-first-sketch)
4. [PARAS Board Pinout & Hardware Reference](#4-paras-board-pinout--hardware-reference)
   - [4.1 Physical Board Diagram](#41-physical-board-diagram-top-view)
   - [4.2 Left Side Header (12 Pins)](#42-left-side-header-12-pins-top-to-bottom)
   - [4.3 Right Side Header (12 Pins)](#43-right-side-header-12-pins-top-to-bottom)
   - [4.4 Bottom Expansion Header (5 Pins)](#44-bottom-expansion-header-5-pins-left-to-right)
   - [4.5 Analog Inputs (12-bit ADC - analogRead)](#45-analog-inputs-quick-reference-analogread)
   - [4.6 Hardware PWM Pins & Motor Control (analogWrite)](#46-hardware-pwm-pins--motor-control-analogwrite)
   - [4.7 Communication Interfaces (Serial, I2C, SPI)](#47-communication-interfaces-quick-reference)
5. [Example Sketches](#5-example-sketches)
   - [5.1 Built-in LED Blink](#51-builtin-led-blink)
   - [5.2 Smooth LED Fading (Hardware PWM)](#52-smooth-led-fading-hardware-pwm)
   - [5.3 DC Motor Speed & Direction Control](#53-dc-motor-speed--direction-control)
   - [5.4 Reading an Analog Sensor with Serial Monitor](#54-reading-an-analog-sensor-with-serial-monitor)
   - [5.5 Digital Sensor (Button / PIR Motion Sensor)](#55-digital-sensor-button--pir-motion-sensor)
6. [Troubleshooting & FAQs](#6-troubleshooting)

---

## 1. Prerequisites

Before uploading sketches, ensure your computer has the following installed:

### 1.1 SDCC Compiler (8051 C Compiler)
The N76E003 uses the high-performance 1T 8051 architecture and compiles using SDCC:
- **Windows**:
  - Open PowerShell as Administrator and run:
    ```powershell
    winget install SDCC.SDCC
    ```
  - Or download the Windows installer (.exe) directly from [SourceForge SDCC](https://sourceforge.net/projects/sdcc/files/).
  - Verify installation by opening a new Command Prompt or PowerShell and running:
    ```cmd
    sdcc --version
    ```
  - *(Ensure `C:\Program Files\SDCC\bin` is added to your Windows system `PATH`)*.

### 1.2 Python & PySerial
The build tools and USB ISP upload script require Python 3 and the `pyserial` module:
- Install Python from [python.org](https://www.python.org/) (ensure **"Add python.exe to PATH"** is checked during installation).
- Install `pyserial`:
  ```cmd
  pip install pyserial
  ```

> [!IMPORTANT]
> **Windows 10 & 11 Fix for `exit status 9009` (App Execution Alias Issue)**:
> In Windows 10 & 11, Microsoft includes dummy command shortcuts that hijack `python.exe` and `python3.exe`, redirecting them to the Microsoft Store. This causes Arduino IDE to fail compilation with:
> `Python was not found; run without arguments to install from the Microsoft Store... Compilation error: exit status 9009`
>
> **To fix this immediately**:
> 1. Open the Windows Start menu, type **Manage app execution aliases**, and press **Enter** (or open **Windows Settings** -> **Apps** -> **Advanced app settings** -> **App execution aliases**).
> 2. Scroll down to find **App Installer (`python.exe`)** and **App Installer (`python3.exe`)**.
> 3. Turn **OFF** both toggles.
> 4. Restart Arduino IDE.

### 1.3 CH340 USB Drivers
The PARAS N76E003 board includes an onboard CH340G USB-to-UART chip:
- If no COM port appears in Arduino IDE under **Tools -> Port** when plugged in via USB, download and install the official [WCH CH341SER Driver](https://www.wch-ic.com/downloads/CH341SER_EXE.html).

---

## 2. Installation via Arduino Boards Manager

1. Open **Arduino IDE** (version 1.8.x or 2.x).
2. Go to **File -> Preferences** (or press `Ctrl + ,`).
3. In the **Additional Boards Manager URLs** field, enter:
   ```text
   https://raw.githubusercontent.com/Abhibhat2007/N76E003AT20/main/package_nuvoton_n76e003_index.json
   ```
   *(If you already have other URLs, separate them with a comma or click the window icon next to the field).*
4. Click **OK**.
5. Open **Tools -> Board -> Boards Manager...** (or click the Boards icon in the Arduino IDE 2 sidebar).
6. Search for **`N76E003`**.
7. Click **Install** on **Nuvoton N76E003 8051 Boards**.

---

## 3. Uploading Your First Sketch

### 3.1 Board Configuration
In Arduino IDE, select the following under the **Tools** menu:
- **Board**: `Nuvoton N76E003 Boards` -> `Nuvoton N76E003 (TSSOP20/QFN20)`
- **Upload Method**: `Serial Bootloader (UART ISP)`
- **Clock Frequency**: `16 MHz (Internal HIRC)`
- **Port**: Select your board's USB COM port (e.g., `COM11`)

### 3.2 Blink Sketch
Open or paste this standard sketch:

```cpp
#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Built-in LED on P1.2 (Pin 8)
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}
```

### 3.3 Upload Procedure
1. Click the **Upload** button (`->`).
2. Watch the bottom output console. When it shows:
   ```text
   Connecting to N76E003 on COMx...
   >>> IF NOT AUTO-CONNECTING: PRESS THE RESET BUTTON ON YOUR BOARD NOW <<<
   ```
3. **Press the physical red `RESET` button** on your PARAS board once.
4. The uploader connects, flashes memory, and launches your code:
   ```text
   [INFO] Connected to N76E003 ISP bootloader successfully!
   [INFO] Device ID detected: 0x3650 (N76E003)
   Flashing: [====================] 100%
   [SUCCESS] Firmware launched! N76E003 is now running your sketch.
   ```
5. The onboard blue LED (`LED P1.2`) will start blinking!

---

## 4. PARAS Board Pinout & Hardware Reference

The **PARAS N76E003** breakout board features two 12-pin side headers and one 5-pin bottom expansion header.

### 4.1 Physical Board Diagram (Top View)

```text
                     +---------------------------------------+
                     | [ USB ]               [ RESET BUTTON ]|
                     |                                       |
                     |  (POWER LED)            (LED P1.2)    |
                     |                     [ PARAS ]         |
                     |                                       |
         (Top)   GND | [1]                               [1] | GND
                 GND | [2]                               [2] | +3V
                +5V  | [3]                               [3] | P1.4       (D6 / SPI_CLK / PWM4)
                +5V  | [4]                               [4] | SCLP1.3    (D7 / SPI_MOSI / PWM3)
(D5 / PWM5) P1.5PWM5 | [5]                               [5] | SDAP1.2    (D8 / LED_BUILTIN / PWM0)
(D4)            P1.6 | [6]                               [6] | PWM1P1.1   (D9 / A3 / PWM1)
(D3 / A4)       P1.7 | [7]                               [7] | PWM2P1.0   (D10 / PWM2)
(D2 / A5)       P3.0 | [8]                               [8] | PWM3P0.0   (D11 / SPI_MISO / PWM3)
(D17 / RST)  P2.0RST | [9]                               [9] | PWM4P0.1   (D12 / SPI_SS / PWM4)
(D0 / A6)     P0.7RX | [10]                             [10] | P0.2       (D16 / ICE_CLK)
(D1 / A7)     P0.6TX | [11]                             [11] | PWM5P0.3   (D13 / A2 / PWM5)
(D14 / A0)      P0.5 | [12]     [ N76E003 CHIP ]        [12] | P0.4       (D15 / A1 / PWM3)
                     +---------------------------------------+
                                  |   |   |   |   |
                                 GND RST SCL SDA +5V
                                [ 5-Pin Bottom Header ]
```

---

### 4.2 Left Side Header (12 Pins, Top to Bottom)

| Pin # | Board Silkscreen | Port Pin | Arduino Digital | Arduino Analog | Alternate Hardware Functions | Notes / Best Use |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| **1**  | **`GND`** | — | Power | Power | Ground supply rail (0V) | Common Ground |
| **2**  | **`GND`** | — | Power | Power | Ground supply rail (0V) | Common Ground |
| **3**  | **`+5V`** | — | Power | Power | +5V power rail from USB | Sensor power supply |
| **4**  | **`+5V`** | — | Power | Power | +5V power rail from USB | Sensor power supply |
| **5**  | **`P1.5PWM5`** | `P1.5` | `D5` (or `5`) | — | `PWM5`, `I2C_SDA`, `SS` | Hardware I2C SDA / General IO |
| **6**  | **`P1.6`** | `P1.6` | `D4` (or `4`) | — | `I2C_SCL`, `TXD_1` | Hardware I2C SCL / Motor Direction |
| **7**  | **`P1.7`** | `P1.7` | `D3` (or `3`) | **`A4`** | `AIN0`, `INT1` | 12-bit ADC Ch 0 / Ext Interrupt 1 / Motor Direction |
| **8**  | **`P3.0`** | `P3.0` | `D2` (or `2`) | **`A5`** | `AIN1`, `INT0`, `ICE_DAT` | 12-bit ADC Ch 1 / Ext Interrupt 0 |
| **9**  | **`P2.0RST`** | `P2.0` | `D17` (or `17`) | — | `RST` | Reset Pin (connected to red button) |
| **10** | **`P0.7RX`** | `P0.7` | `D0` (or `0`) | `A6` | `RXD0`, `AIN2` | Hardware Serial RX (Connected to CH340 TX) |
| **11** | **`P0.6TX`** | `P0.6` | `D1` (or `1`) | `A7` | `TXD0`, `AIN3` | Hardware Serial TX (Connected to CH340 RX) |
| **12** | **`P0.5`** | `P0.5` | `D14` (or `14`) | **`A0`** | `AIN4` | **Primary 12-bit ADC Input** (Potentiometers, Sensors) |

---

### 4.3 Right Side Header (12 Pins, Top to Bottom)

| Pin # | Board Silkscreen | Port Pin | Arduino Digital | Arduino Analog | Alternate Hardware Functions | Notes / Best Use |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| **1**  | **`GND`** | — | Power | Power | Ground supply rail (0V) | Common Ground |
| **2**  | **`+3V`** | — | Power | Power | +3.3V regulated power rail | 3.3V sensor supply |
| **3**  | **`P1.4`** | `P1.4` | `D6` (or `6`) | — | `SPI_CLK`, `PWM4`, `SDA_1` | Hardware SPI Clock (SCK) |
| **4**  | **`SCLP1.3`** | `P1.3` | `D7` (or `7`) | — | `SPI_MOSI`, `SCL_1` | Hardware SPI MOSI |
| **5**  | **`SDAP1.2`** | `P1.2` | `D8` (or `8`) | — | **`PWM0`**, `STADC` | **Onboard User LED** (`LED_BUILTIN` / Hardware PWM0) |
| **6**  | **`PWM1P1.1`** | `P1.1` | `D9` (or `9`) | **`A3`** | **`PWM1`**, `AIN7`, `CLO` | **Hardware PWM1 (Motor A Speed / ENA)** / ADC Ch 7 |
| **7**  | **`PWM2P1.0`** | `P1.0` | `D10` (or `10`) | — | **`PWM2`**, `SPCLK` | **Hardware PWM2 (Motor B Speed / ENB)** |
| **8**  | **`PWM3P0.0`** | `P0.0` | `D11` (or `11`) | — | **`PWM3`**, `SPI_MISO` | **Hardware PWM3** / SPI MISO |
| **9**  | **`PWM4P0.1`** | `P0.1` | `D12` (or `12`) | — | `SPI_SS` | Hardware SPI Slave Select (SS) |
| **10** | **`P0.2`** | `P0.2` | `D16` (or `16`) | — | `ICE_CLK`, `RXD_1` | Nu-Link ICE Clock / General GPIO |
| **11** | **`PWM5P0.3`** | `P0.3` | `D13` (or `13`) | **`A2`** | `AIN6` | 12-bit ADC Ch 6 / General GPIO |
| **12** | **`P0.4`** | `P0.4` | `D15` (or `15`) | **`A1`** | `AIN5`, `STADC` | **Secondary 12-bit ADC Input** (Preset / Joystick) |

---

### 4.4 Bottom Expansion Header (5 Pins, Left to Right)

| Pin # | Board Silkscreen | Connected To | Description |
|:---:|:---|:---|:---|
| **1** | **`GND`** | Ground rail | 0V Common Ground |
| **2** | **`RST`** | `P2.0` / Reset | External Reset line |
| **3** | **`SCL`** | `P1.6` (`D4`) | Hardware I2C Clock (for OLED / I2C displays) |
| **4** | **`SDA`** | `P1.5` (`D5`) | Hardware I2C Data (for OLED / I2C sensors) |
| **5** | **`+5V`** | +5V Rail | +5V Power Output |

---

### 4.5 Analog Inputs Quick Reference (`analogRead`)

The N76E003 provides high-speed **12-bit SAR ADC** (`0` to `4095`, representing `0.000 V` to `5.000 V`):

| Arduino Name | Board Silkscreen | Header Location | Hardware Channel | Best Use Cases |
|:---:|:---|:---|:---:|:---|
| **`A0`** | **`P0.5`** | Left Header, Pin 12 (Bottom Left) | `AIN4` | Primary analog input (Potentiometer, LM35, LDR) |
| **`A1`** | **`P0.4`** | Right Header, Pin 12 (Bottom Right) | `AIN5` | Secondary analog input (1k Preset, Joysticks) |
| **`A2`** | **`PWM5P0.3`** | Right Header, Pin 11 | `AIN6` | Analog input |
| **`A3`** | **`PWM1P1.1`** | Right Header, Pin 6 | `AIN7` | Analog input |
| **`A4`** | **`P1.7`** | Left Header, Pin 7 | `AIN0` | Analog input / Single-wire sensors (DHT11) |
| **`A5`** | **`P3.0`** | Left Header, Pin 8 | `AIN1` | Analog input |
| **`A6`** | **`P0.7RX`** | Left Header, Pin 10 | `AIN2` | *(Shared with USB RX — reserved for Serial)* |
| **`A7`** | **`P0.6TX`** | Left Header, Pin 11 | `AIN3` | *(Shared with USB TX — reserved for Serial)* |

---

### 4.6 Hardware PWM Pins & Motor Control (`analogWrite`)

The N76E003 features a dedicated hardware 16-bit PWM generator configured in this Arduino core for standard 8-bit `analogWrite(pin, value)` (`0` to `255`):

| Arduino Pin | Port Pin | Hardware PWM | Silkscreen | Best Use Cases |
|:---:|:---:|:---:|:---:|:---|
| **`8`** / **`LED_BUILTIN`** | `P1.2` | `PWM0` | **`SDAP1.2`** | Built-in LED fading / Status indicators |
| **`9`** | `P1.1` | `PWM1` | **`PWM1P1.1`** | **Motor A Speed (ENA)** / DC Motor Speed Control |
| **`10`** | `P1.0` | `PWM2` | **`PWM2P1.0`** | **Motor B Speed (ENB)** / DC Motor Speed Control |
| **`11`** | `P0.0` | `PWM3` | **`PWM3P0.0`** | Motor Speed / High-speed buzzer / Power regulation |

- **PWM Resolution**: 8-bit (`0` = 0% duty / fully OFF, `255` = 100% duty / fully ON).
- **PWM Frequency**: **~3.9 kHz** (16 MHz system clock divided by 16 prescaler across 255 period counts).
- **Silent Motor Operation**: ~3.9 kHz is above typical audible motor resonance, ensuring completely silent, smooth DC motor speed control with drivers such as **L298N**, **TB6612FNG**, **L9110S**, **DRV8833**, or MOSFET modules!

---

### 4.7 Communication Interfaces Quick Reference

- **Hardware Serial (UART0 at 115200 baud)**:
  - `Serial.begin(115200)` uses `P0.6TX` and `P0.7RX`, connected to the onboard CH340 USB chip.
- **Hardware I2C (`Wire` / OLED displays)**:
  - `SCL`: `P1.6` (Left Header Pin 6 or Bottom Header Pin 3)
  - `SDA`: `P1.5` (Left Header Pin 5 or Bottom Header Pin 4)
- **Hardware SPI (`SPI`)**:
  - `SCK`: `P1.4` (Right Header Pin 3 / `D6`)
  - `MOSI`: `SCLP1.3` (Right Header Pin 4 / `D7`)
  - `MISO`: `PWM3P0.0` (Right Header Pin 8 / `D11`)
  - `SS`: `PWM4P0.1` (Right Header Pin 9 / `D12`)

---

## 5. Example Sketches

### 5.1 Built-in LED Blink
```cpp
#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Pin 8 (P1.2)
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

### 5.2 Smooth LED Fading (Hardware PWM)
Demonstrates standard Arduino `analogWrite` with smooth fade-in and fade-out:

```cpp
#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Fade In: 0 to 255
  for (int i = 0; i <= 255; i++) {
    analogWrite(LED_BUILTIN, i);
    delay(8);
  }

  // Fade Out: 255 to 0
  for (int i = 255; i >= 0; i--) {
    analogWrite(LED_BUILTIN, i);
    delay(8);
  }
}
```

### 5.3 DC Motor Speed & Direction Control
Controls a DC motor using an H-bridge motor driver (e.g., L298N, TB6612FNG, or L9110S):

```text
Wiring Connections:
  N76E003 Pin 9  (PWM1) ---> Motor Driver ENA (PWM Speed Control)
  N76E003 Pin 3  (P1.7) ---> Motor Driver IN1 (Direction Pin 1)
  N76E003 Pin 4  (P1.6) ---> Motor Driver IN2 (Direction Pin 2)
  N76E003 GND           ---> Motor Driver GND (Common Ground)
  External Power (5V-12V)---> Motor Driver VCC & GND
```

```cpp
#include <Arduino.h>

const int MOTOR_PWM = 9;  // P1.1 (PWM1) - Speed control (0 to 255)
const int MOTOR_IN1 = 3;  // P1.7 - Direction control 1
const int MOTOR_IN2 = 4;  // P1.6 - Direction control 2

void setMotor(int speed, bool forward) {
  if (forward) {
    digitalWrite(MOTOR_IN1, HIGH);
    digitalWrite(MOTOR_IN2, LOW);
  } else {
    digitalWrite(MOTOR_IN1, LOW);
    digitalWrite(MOTOR_IN2, HIGH);
  }
  analogWrite(MOTOR_PWM, speed); // 0 = STOP, 255 = Full Speed
}

void setup() {
  pinMode(MOTOR_PWM, OUTPUT);
  pinMode(MOTOR_IN1, OUTPUT);
  pinMode(MOTOR_IN2, OUTPUT);
}

void loop() {
  // 1. Accelerate Forward
  for (int spd = 0; spd <= 255; spd += 5) {
    setMotor(spd, true);
    delay(40);
  }
  delay(1000); // Full speed forward for 1 second

  // 2. Stop Motor
  analogWrite(MOTOR_PWM, 0);
  delay(500);

  // 3. Accelerate Reverse
  for (int spd = 0; spd <= 255; spd += 5) {
    setMotor(spd, false);
    delay(40);
  }
  delay(1000); // Full speed reverse for 1 second

  // 4. Stop Motor
  analogWrite(MOTOR_PWM, 0);
  delay(500);
}
```

### 5.4 Reading an Analog Sensor with Serial Monitor
Connect an analog sensor (Potentiometer, LM35, or LDR) to `P0.5` (`A0`), and power pins to `+5V` and `GND`:

```cpp
#include <Arduino.h>

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(A0); // 12-bit ADC returns 0 to 4095
  
  Serial.print("Analog Reading: ");
  Serial.println(sensorValue);
  
  delay(500);
}
```
*(Open Arduino Serial Monitor at **115200 baud** to view live data).*

### 5.5 Digital Sensor (Button / PIR Motion Sensor)
Connect digital sensor to `D3` (`P1.7`):

```cpp
#include <Arduino.h>

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

## 6. Troubleshooting

### Q1: `Compilation error: exit status 9009` or `Python was not found...`
- **Cause**: Windows 10 & 11 have Microsoft Store "App Execution Aliases" enabled by default, preventing Arduino IDE from launching Python.
- **Solution**:
  1. Open Windows Start menu, type **Manage app execution aliases**, and press Enter.
  2. Locate **App Installer (`python.exe`)** and **App Installer (`python3.exe`)**.
  3. Toggle **both OFF**.
  4. Ensure Python 3 is installed with "Add Python to PATH" checked.
  5. Restart Arduino IDE.

### Q2: `[ERROR] pyserial is required`
Run in your command prompt / terminal:
```cmd
pip install pyserial
```

### Q3: `Connection timeout! N76E003 did not enter ISP mode`
- Ensure the correct COM port is chosen in **Tools -> Port**.
- Ensure you press the physical red **`RESET`** button on your board while the IDE output says `Connecting to N76E003 on COMx...`.

### Q4: `sdcc: command not found`
- Install SDCC via `winget install SDCC.SDCC` or from SourceForge.
- Verify `C:\Program Files\SDCC\bin` is in your Windows User or System `PATH`.
- Restart Arduino IDE so it loads the updated PATH.

### Q5: Code uploads but LED does not fade / acts as on-off switch
- Arduino IDE caches compiled object files in temporary directories.
- If you recently updated the core files, change your selected board to any other board (e.g., Arduino Uno) and switch back to **Nuvoton N76E003 (TSSOP20/QFN20)**, or restart Arduino IDE. This flushes the build cache and forces a fresh compilation.

### Q6: Board not showing up in Tools -> Port
- Ensure the USB cable supports data transfer (not a charge-only cable).
- Install the [CH340 Driver](https://www.wch-ic.com/downloads/CH341SER_EXE.html) if your PC does not recognize the USB-to-UART bridge.
