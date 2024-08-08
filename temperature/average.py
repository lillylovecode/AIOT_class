import sqlite3

# 初始化資料庫連接
conn = sqlite3.connect('temperature.db')
cursor = conn.cursor()

# 獲取最後10筆數據
cursor.execute('SELECT temperature, humidity FROM temperature_data ORDER BY id DESC LIMIT 10')
data = cursor.fetchall()

if data:
    temperatures = [row[0] for row in data]
    humidities = [row[1] for row in data]

    # 計算平均值
    avg_temperature = sum(temperatures) / len(temperatures)
    avg_humidity = sum(humidities) / len(humidities)

    print(f'Average Temperature: {avg_temperature:.2f}°C')
    print(f'Average Humidity: {avg_humidity:.2f}%')
else:
    print('No data available.')

# 關閉資料庫連接
conn.close()
