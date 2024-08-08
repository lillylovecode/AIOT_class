import time
import datetime
import Adafruit_DHT
import sqlite3

# 初始化DHT感測器
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # 這裡的4表示GPIO 4，請根據你的設置調整

# 初始化資料庫連接
conn = sqlite3.connect('temperature.db')
cursor = conn.cursor()

# 創建資料表（如果不存在）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS temperature_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature REAL,
        humidity REAL,
        timestamp DATETIME
    )
''')

while True:
    # 讀取溫溼度數據
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        # 獲取當前日期時間
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 將數據寫入資料庫
        cursor.execute('INSERT INTO temperature_data (temperature, humidity, timestamp) VALUES (?, ?, ?)', (temperature, humidity, timestamp))
        conn.commit()

        print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}% at {timestamp}')

    time.sleep(60)  # 每1分鐘執行一次
