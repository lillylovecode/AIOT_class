import mylib
import joblib

# 載入先前訓練好的模型
model_filename = 'crop_model.pkl'
loaded_model = joblib.load(model_filename)

temperature, humidity = mylib.read_dht_sensor(14)
if temperature is not None and humidity is not None:
    print(f'Temperature: {temperature:.2f}°C')
    print(f'Humidity: {humidity*100:.2f}%')
else:
    print('Failed to retrieve data from the sensor.')

# 定義要預測的特徵資料
# 這裡以示例資料作為單筆預測，您可以替換成您的實際資料
new_data = [[60, 55, 44, temperature, humidity, 7.840207144, 263.9642476]]

# 使用模型進行預測
predicted_class = loaded_model.predict(new_data)

# 輸出預測結果

print(f"預測的農田適用作物為: {predicted_class}")
