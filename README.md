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
   ```
   *(If you already have other URLs, separate them with a comma or click the icon next to the field to add a new line).*
4. Click **OK**.
5. Open **Tools -> Board -> Boards Manager...** (or click the Boards icon on the left sidebar in Arduino IDE 2.x).
6. Search for **`N76E003`**.
7. Click **Install** on **Nuvoton N76E003 8051 Boards**.

---

## 3. Uploading Your First Sketch

### 3.1 Board Configuration
In Arduino IDE, set:
- **Tools -> Board -> Nuvoton N76E003 Boards -> Nuvoton N76E003 (TSSOP20/QFN20)**
- **Tools -> Upload Method -> Serial Bootloader (UART ISP)**
- **Tools -> Clock Frequency -> 16 MHz (Internal HIRC)**
- **Tools -> Port -> COMx** (Select your CH340 USB COM port, e.g., `COM11`)

### 3.2 Blink Sketch
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

### 3.3 Upload
1. Click the **Upload** button (`->`).
2. When the terminal prompts:
   ```text
   Connecting to N76E003 on COMx...
   >>> IF NOT AUTO-CONNECTING: PRESS THE RESET BUTTON ON YOUR BOARD NOW <<<
   ```
   Press the physical red **`RESET`** button on your board once.
3. The flasher will automatically erase, flash, and verify:
   ```text
   [INFO] Connected to N76E003 ISP bootloader successfully!
   [INFO] Device ID detected: 0x3650 (N76E003)
   Flashing: [====================] 100%
   [SUCCESS] Firmware launched! N76E003 is now running your sketch.
   ```
4. Your on-board `LED(P1.2)` will start blinking!

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
| **5**  | **`P1.5PWM5`** | `P1.5` | `D5` (or `5`) | — | `PWM5`, `I2C_SDA`, `SS` | Hardware I2C SDA / PWM5 |
| **6**  | **`P1.6`** | `P1.6` | `D4` (or `4`) | — | `I2C_SCL`, `TXD_1` | Hardware I2C SCL |
| **7**  | **`P1.7`** | `P1.7` | `D3` (or `3`) | **`A4`** | `AIN0`, `INT1` | 12-bit ADC Ch 0 / Ext Interrupt 1 (DHT11 Data) |
| **8**  | **`P3.0`** | `P3.0` | `D2` (or `2`) | **`A5`** | `AIN1`, `INT0`, `ICE_DAT` | 12-bit ADC Ch 1 / Ext Interrupt 0 |
| **9**  | **`P2.0RST`** | `P2.0` | `D17` (or `17`) | — | `RST` | Reset Pin (connected to red button) |
| **10** | **`P0.7RX`** | `P0.7` | `D0` (or `0`) | `A6` | `RXD0`, `AIN2`, `PWM0` | Hardware Serial RX (Connected to CH340 TX) |
| **11** | **`P0.6TX`** | `P0.6` | `D1` (or `1`) | `A7` | `TXD0`, `AIN3`, `PWM1` | Hardware Serial TX (Connected to CH340 RX) |
| **12** | **`P0.5`** | `P0.5` | `D14` (or `14`) | **`A0`** | `AIN4`, `PWM2` | **Primary 12-bit ADC Input** (Potentiometer / Sensors) |

---

### 4.3 Right Side Header (12 Pins, Top to Bottom)

| Pin # | Board Silkscreen | Port Pin | Arduino Digital | Arduino Analog | Alternate Hardware Functions | Notes / Best Use |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| **1**  | **`GND`** | — | Power | Power | Ground supply rail (0V) | Common Ground |
| **2**  | **`+3V`** | — | Power | Power | +3.3V regulated power rail | 3.3V sensor supply |
| **3**  | **`P1.4`** | `P1.4` | `D6` (or `6`) | — | `SPI_CLK`, `PWM4`, `SDA_1` | Hardware SPI Clock (SCK) |
| **4**  | **`SCLP1.3`** | `P1.3` | `D7` (or `7`) | — | `SPI_MOSI`, `PWM3`, `SCL_1` | Hardware SPI MOSI |
| **5**  | **`SDAP1.2`** | `P1.2` | `D8` (or `8`) | — | `PWM0`, `STADC` | **Onboard User LED** (`LED_BUILTIN`) |
| **6**  | **`PWM1P1.1`** | `P1.1` | `D9` (or `9`) | **`A3`** | `AIN7`, `PWM1`, `CLO` | 12-bit ADC Ch 7 / PWM1 |
| **7**  | **`PWM2P1.0`** | `P1.0` | `D10` (or `10`) | — | `PWM2`, `SPCLK` | PWM2 / General GPIO |
| **8**  | **`PWM3P0.0`** | `P0.0` | `D11` (or `11`) | — | `SPI_MISO`, `PWM3` | Hardware SPI MISO / PWM3 |
| **9**  | **`PWM4P0.1`** | `P0.1` | `D12` (or `12`) | — | `SPI_SS`, `PWM4` | Hardware SPI Slave Select (SS) / PWM4 |
| **10** | **`P0.2`** | `P0.2` | `D16` (or `16`) | — | `ICE_CLK`, `RXD_1` | Nu-Link ICE Clock / General GPIO |
| **11** | **`PWM5P0.3`** | `P0.3` | `D13` (or `13`) | **`A2`** | `AIN6`, `PWM5` | 12-bit ADC Ch 6 / PWM5 |
| **12** | **`P0.4`** | `P0.4` | `D15` (or `15`) | **`A1`** | `AIN5`, `PWM3`, `STADC` | **Secondary 12-bit ADC Input** (1k Preset) |

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
| **`A6`** | **`P0.7RX`** | Left Header, Pin 10 | `AIN2` | *(Shared with USB RX — keep for Serial)* |
| **`A7`** | **`P0.6TX`** | Left Header, Pin 11 | `AIN3` | *(Shared with USB TX — keep for Serial)* |

---

### 4.6 Communication Interfaces Quick Reference

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

### 5.1 Reading an Analog Sensor with Serial Monitor
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

### 5.2 Digital Sensor (Button / PIR Motion Sensor)
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

## 6. Troubleshooting

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
- Make sure `C:\Program Files\SDCC\bin` (or your SDCC installation `bin` folder) is in your Windows User `PATH`.

### Q4: Code uploads but LED doesn't blink
- Check pin mapping: On the PARAS board, the user LED is on `P1.2` (`LED_BUILTIN` or pin `8`).
- Give the red **`RESET`** button a quick press after upload finishes.
