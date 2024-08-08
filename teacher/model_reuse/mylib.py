#import RPi.GPIO as GPIO
#import Adafruit_DHT
#import time

#def read_dht_sensor(pin, sensor_type=Adafruit_DHT.DHT11):
def read_dht_sensor(pin):
    try:
        #humidity, temperature = Adafruit_DHT.read_retry(sensor_type, pin)
        humidity = 0.8679
        temperature = 24.3
        if humidity is not None and temperature is not None:
            return temperature, humidity
        else:
            return None, None
    except Exception as e:
        print(f'Error: {str(e)}')
        return None, None

# 請將這個函數呼叫放在您想要讀取溫濕度的地方
# 第一個參數是接線的GPIO pin，第二個參數是傳感器類型，預設為DHT11

# 例如，如果您的 DHT 連接到 GPIO 4，您可以這樣呼叫函數：
# temperature, humidity = read_dht_sensor(4)

# 如果您使用的是 DHT22 傳感器，您可以這樣呼叫函數：
# temperature, humidity = read_dht_sensor(4, Adafruit_DHT.DHT22)

'''if __name__ == '__main__':
    temperature, humidity = read_dht_sensor(14)
    if temperature is not None and humidity is not None:
        print(f'Temperature: {temperature:.2f}°C')
        print(f'Humidity: {humidity*100:.2f}%')
    else:
        print('Failed to retrieve data from the sensor.')'''