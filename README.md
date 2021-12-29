# ESP32 + SSD1306 : Weather Station using Micropython

#### **Parts required**

- [x] ESP32 board
- [x] SSD1306 OLED
- [x] Jumper wires and USB cable for powering the ESP32
- [x] Register for account in Openweathermap.org website and get API key

#### **Register for an account from openweathermap.org**
- Signup for an account
- Open URL 
- Copy the Key value from the website

#### **Edit micropython program with your API key**

- Open main.py in any editor(Thonny)
- Replace the text "YOUR-API-KEY" in below code with your own API key

#### **Save it as main.py in your ESP32**

- Thonny editor is well suited, as it can edit python as well as save directly to ESP32.

#### **Wiring ESP32 with SSD1306**

**ESP32 <--> SSD1306**
- OLED SCK --> GPIO 22
- OLED SDA --> GPIO 21
- OLED VDD --> Bat
- OLED GND --> GND
