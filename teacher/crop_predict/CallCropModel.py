import joblib

# 載入訓練好的模型
model_filename = 'crop_model.pkl'
loaded_model = joblib.load(model_filename)

# 定義要預測的特徵資料
# 這裡以示例資料作為單筆預測，您可以替換成您的實際資料
new_data = [[29,71,18,22.17499963,62.13873825,6.410441476,53.46622584]]

# 使用模型進行預測
predicted_class = loaded_model.predict(new_data)

# 輸出預測結果
print(f"預測的農田適用作物為: {predicted_class}")