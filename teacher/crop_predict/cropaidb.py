# 匯入必要的庫
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 連接MySQL數據庫
import mysql.connector

# 建立數據庫連接
conn = mysql.connector.connect(
    host="163.15.172.114",
    user="sid01",
    password="1234",
    database="crop"
)

# 從數據庫中獲取數據
query = "SELECT N, P, K, temperature, humidity, ph, rainfall, label FROM crop_rec"
df = pd.read_sql(query, conn)
print(df)

# 關閉數據庫連接
conn.close()

# 將目標值編碼為整數
le = LabelEncoder()
df['label'] = le.fit_transform(df['label'])

# 分割數據集為訓練集和測試集
X = df.iloc[:, :-1]  # 特徵值
y = df['label']  # 目標值

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用隨機森林分類器進行模型訓練
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# 進行預測
y_pred = clf.predict(X_test)

# 計算準確率
accuracy = accuracy_score(y_test, y_pred)
print("模型準確率: {:.2f}%".format(accuracy * 100))