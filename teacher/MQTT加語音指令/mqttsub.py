#Windows安裝mosquitto
#Windows啟動MQTT Server， 以系統管理員權限在cmd執行net start mosquitto指令
#在Windows安裝paho，在cmd執行pip install paho-mqtt
import paho.mqtt.client as mqtt

# 模擬感測器啟動函數
def start_sensor(topic):
    # 在這裡可以實現啟動相對應感測器的邏輯
    print(f"啟動了與主題 '{topic}' 相關的感測器")

# MQTT 設定
mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic_commands = [
    "home/light/on",
    "home/light/off",
    "home/ac/on",
    "home/ac/off"
]

# 當收到 MQTT 訊息時的處理函數
def on_message(client, userdata, message):
    topic = message.topic
    print(f"收到訊息：{topic} {str(message.payload.decode())}")

    # 啟動相對應的感測器
    start_sensor(topic)

# 初始化 MQTT 客戶端
client = mqtt.Client()

# 設定收到訊息時的處理函數
client.on_message = on_message

# 連接 MQTT Broker
client.connect(mqtt_broker, mqtt_port)

# 訂閱指定主題
for topic in mqtt_topic_commands:
    client.subscribe(topic)

# 持續接收訊息
client.loop_forever()
