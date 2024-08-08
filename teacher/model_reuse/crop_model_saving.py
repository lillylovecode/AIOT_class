# 引入所需的套件
from sklearn import svm  # 引入支援向量機 (SVM) 分類器
from sklearn.utils import Bunch  # 引入 Bunch 類別，用於組織資料
from sklearn.metrics import accuracy_score
import pandas as pd  # 引入 pandas 套件，用於處理資料
import joblib

# 資料檔案的路徑
csv_filename = "crop.csv"

# 從 CSV 檔案讀取資料
data = pd.read_csv(csv_filename)


# 將資料轉換成 NumPy 陣列
data_array = data.iloc[:, :-1].to_numpy()


# 提取特徵名稱
feature_names = data.columns[:-1].tolist()


# 提取目標值
target = data.iloc[:, -1].to_numpy()


# 提取目標值的名稱
target_name = data.columns[-1]

# 使用 Bunch 將資料組織成一個資料集
dataset = Bunch(data=data_array, target=target, feature_names=feature_names, target_names=[target_name])


# 輸出資料集的資料部分
'''print("Data:")
print(dataset.data)

# 輸出資料集的目標值部分
print("Target:")
print(dataset.target)

# 輸出特徵名稱
print("Feature Names:")
print(dataset.feature_names)

# 輸出目標值的名稱
print("Target Name:")
print(dataset.target_names)'''

# 設定 SVM 模型的參數 C (正規化參數)
#C = 1.0

# 創建 SVM 分類器，使用線性核函數 (linear) 和指定的正規化參數 C
#clf = svm.SVC(kernel="linear", C=C)

# 創建線性 SVM 分類器，指定正規化參數 C、最大迭代次數和是否使用雙對偶問題
#clf = svm.LinearSVC(C=C, max_iter=10000, dual="auto")

# 創建 SVM 分類器，使用徑向基函數核 (RBF) 和指定的 gamma 參數和正規化參數 C
#clf = svm.SVC(kernel="rbf", gamma=0.7, C=C)

# 創建 SVM 分類器，使用多項式核函數 (poly)，指定多項式的次數、gamma 參數和正規化參數 C
#clf = svm.SVC(kernel="poly", degree=3, gamma="auto", C=C)

# 創建默認的 SVM 分類器，使用默認的核函數 (通常是 RBF) 和正規化參數 C
clf = svm.SVC()

# 使用資料訓練 SVM 模型
clf.fit(dataset.data, dataset.target)

# 儲存訓練好的模型到檔案
model_filename = 'crop_model.pkl'
joblib.dump(clf, model_filename)
#print(f"模型已儲存到 {model_filename}")

# 計算模型的準確度
#print("Accuracy:", clf.score(dataset.data, dataset.target))

# 使用模型進行預測
#print("Prediction:", clf.predict([[60, 55, 44, 23.00445915, 82.3207629, 7.840207144, 263.9642476
#]]))