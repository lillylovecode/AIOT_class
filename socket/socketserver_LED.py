import socket
from datetime import datetime
import LED
import RPi.GPIO as GPIO
import time
import mylib

server_ip = '192.168.100.7'
server_port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((server_ip, server_port))
server.listen(5)
print(f"伺服器已啟動，監聽在 {server_ip}:{server_port}")

red_pin = 2

while True:
    try:
        client_socket, client_address = server.accept()
        print(f"與客戶端 {client_address} 建立連線")

        while True:
            
            LED.Setup(red_pin,"IN")
            LED.Setup(red_pin,"OUT")
            LED.TurnOffLED(red_pin)
                    
            data = client_socket.recv(1024)
            if data:
                print(f"收到來自客戶端的資料：{data}")
                if data == b'ron':
                    for i in range(1,5):
                        LED.TurnOnLED(red_pin)
                        time.sleep(0.5)
                        LED.TurnOffLED(red_pin)
                        time.sleep(0.5)
                    print("開啟紅燈")                   
                elif data == b'rof':
                    LED.TurnOffLED(red_pin)
                    time.sleep(2)
                    print("關閉紅燈")
                elif data == b'yon':
                    print("開啟黃燈")
                elif data == b'yof':
                    print("關閉黃燈")
                elif data == b'gon':
                    print("開啟綠燈")
                elif data == b'gof':
                    print("關閉綠燈")
                elif data == b'getth':
                    # 回傳當前temp,humi給客戶端
                    temperature, humidity = mylib.read_dht_sensor(14)
                    response = f"current temp={temperature:.2f}°C,humidity={humidity*100:.2f}%"
                    client_socket.sendall(response.encode())
                    print(f"已回傳當前data給客戶端：{response}")
                elif data == b'gettime':
                    # 回傳當前時間給客戶端
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    client_socket.sendall(current_time.encode())
                    print(f"已回傳當前時間給客戶端：{current_time}")
                break  # 收到資料後中斷當前連線並等待新的連線
    except Exception as e:
        print(f"錯誤發生: {e}")
    finally:
        client_socket.close()
        GPIO.cleanup()