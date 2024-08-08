import speech_recognition as sr
import paho.mqtt.client as mqtt

# MQTT 設定
mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic_light_on = "home/light/on"
mqtt_topic_light_off = "home/light/off"
mqtt_topic_ac_on = "home/ac/on"
mqtt_topic_ac_off = "home/ac/off"

# 初始化 MQTT 客戶端
client = mqtt.Client()

# 連接 MQTT Broker
client.connect(mqtt_broker, mqtt_port)

# 定義指令的關鍵詞
keywords = ["開燈", "關燈", "開冷氣", "關冷氣"]

# 聲音識別函數
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("請說話...")
        
        # 調整降噪參數
        r.adjust_for_ambient_noise(source, duration=1)  # 調整持續時間以收集背景噪音樣本

        audio = r.listen(source)

    try:
        # 使用 Google 語音辨識引擎識別語音
        command = r.recognize_google(audio, language="zh-TW")
        print("您說的是：", command)

        # 判斷辨識到的指令，並發佈到 MQTT 標籤
        for keyword in keywords:
            if keyword in command:
                if keyword == "開燈":
                    client.publish(mqtt_topic_light_on, "ON")
                elif keyword == "關燈":
                    client.publish(mqtt_topic_light_off, "OFF")
                elif keyword == "開冷氣":
                    client.publish(mqtt_topic_ac_on, "ON")
                elif keyword == "關冷氣":
                    client.publish(mqtt_topic_ac_off, "OFF")

                # 顯示識別結果
                print("辨識結果：", keyword)
                break
        else:
            print("未辨識出任何指令")

    except sr.UnknownValueError:
        print("抱歉，無法辨識您的指令")
    except sr.RequestError as e:
        print("無法連接到 Google 語音辨識服務；{0}".format(e))

# 不斷地識別語音指令
while True:
    recognize_speech()
