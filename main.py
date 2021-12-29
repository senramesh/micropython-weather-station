import utime
import ujson
import machine
import ssd1306
import urequests as requests

## Initialize the ssd1306 OLED
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)

while True:
    ## Dubai
    response_json = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=25.204849&lon=55.270782&units=metric&exclude=minutely,hourly,daily,alerts&appid=YOUR-API-KEY').json()
    dxb_current_temp_celsius = response_json['current']['feels_like']
    
    ## Display in OLED
    oled.fill(0)
    oled.text('Dubai   :' + str(dxb_current_temp_celsius), 1, 24, 1)
    oled.show()
    utime.sleep(5)