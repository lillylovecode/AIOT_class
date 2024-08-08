import joblib

# 載入先前訓練好的模型
model_filename = 'crop_model.pkl'
loaded_model = joblib.load(model_filename)

# 定義要預測的特徵資料
# 這裡以示例資料作為單筆預測，您可以替換成您的實際資料
new_data = [[60, 55, 44, 23.00445915, 82.3207629, 7.840207144, 263.9642476]]

# 使用模型進行預測
predicted_class = loaded_model.predict(new_data)

# 輸出預測結果

print(f"預測的農田適用作物為: {predicted_class}")