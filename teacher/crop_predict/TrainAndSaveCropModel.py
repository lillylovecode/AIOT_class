#引入所需的套件
from sklearn import svm  # 引入支援向量機 (SVM) 分類器
from sklearn.utils import Bunch # 引入 Bunch 類別，用於組織資料
from sklearn.metrics import accuracy_score
import pandas as pd  # 引入 pandas 套件，用於處理資料
import joblib # 引入 joblib 套件，用於儲存模型

# 資料檔案的路徑
csv_filename = "crop.csv"

# 從 CSV 檔案讀取資料
data = pd.read_csv(csv_filename)
#print(data[:2]) #顯示前兩筆資料

# 將資料轉換成 NumPy 陣列
data_array = data.iloc[:, :-1].to_numpy()
#iloc[列,欄]，-1代表最後一欄
#:代表全部
#由於pandas中默認csv的第一行為標題，因此標題的索引值為-1

# 提取特徵名稱
feature_names = data.columns[:-1].tolist()
#扣除最後一欄

# 提取目標值
target = data.iloc[:, -1].to_numpy()
#提取最後一欄

# 提取目標值的名稱
target_name = data.columns[-1]
#提取最後一欄的名稱

# 使用 Bunch 將資料組織成一個資料集
dataset = Bunch(data=data_array, target=target, feature_names=feature_names, target_names=[target_name])

# 輸出資料集的資料部分
print("Data:")
print(dataset.data)

# 輸出資料集的目標值部分
print("Target:")
print(dataset.target)

# 輸出特徵名稱
print("Feature Names:")
print(dataset.feature_names)

# 輸出目標值的名稱
print("Target Name:")
print(dataset.target_names)

# 創建默認的 SVM 分類器，使用徑向基函數核 (RBF) 和指定的 gamma 參數和正規化參數 C
clf = svm.SVC()

# 使用資料集訓練 SVM 模型
clf.fit(dataset.data, dataset.target)

# 儲存模型
model_filename = "crop_model.pkl"
joblib.dump(clf, model_filename)
print(f"model saved to {model_filename}")
