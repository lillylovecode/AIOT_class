import mylib

if __name__ == '__main__':
    temperature, humidity = mylib.read_dht_sensor(14)
    if temperature is not None and humidity is not None:
        print(f'Temperature: {temperature:.2f}°C')
        print(f'Humidity: {humidity*100:.2f}%')
    else:
        print('Failed to retrieve data from the sensor.')
