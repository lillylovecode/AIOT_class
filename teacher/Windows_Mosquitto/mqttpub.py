#Publisher
import paho.mqtt.client as mqtt
import random
import time

TopicServerIP = "192.168.100.15"  # 替換為您的 MQTT 伺服器地址
TopicServerPort = 1883
TopicName = "LED"

mqttc = mqtt.Client("python_pub")
mqttc.connect(TopicServerIP, TopicServerPort)

while True:
    PRstatus = random.randint(0, 1)
    print ("PRstatus = ", PRstatus)
    time.sleep(1)
    if PRstatus == 1:
        mqttc.publish(TopicName, "Turn on led")
    else:
        mqttc.publish(TopicName, "Turn off led")
