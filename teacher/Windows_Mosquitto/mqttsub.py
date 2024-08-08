#Subscriber
import paho.mqtt.client as mqtt

# MQTT 伺服器設定
broker_address = "192.168.100.15"  # 替換為您的 MQTT 伺服器地址
port = 1883  # 或您的自訂端口
topic = "hello_topic"  # 替換為您的主題

def on_connect(client, userdata, flags, rc):
    print("Connected with result code" +str(rc))
    client.subscribe("LED")

def on_message(client, usersata, msg):
    print(msg.topic + "  " + str(msg.payload))
    if (msg.payload == b'Turn on led'):
        print("Now LED is On.")
    if (msg.payload == b'Turn off led'):
        print("Now LED is Off.")

# 建立新的 MQTT 客戶端實例
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# 連接到 MQTT 伺服器
client.connect(broker_address, 1883, 60)
client.subscribe(topic)
client.loop_forever()