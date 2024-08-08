import RPi.GPIO as GPIO
import time

def Setup(GPIOnum,OUT_IN):
    GPIO.setmode(GPIO.BCM)
    
    if OUT_IN == "OUT":
        GPIO.setup(GPIOnum,GPIO.OUT)
    else:
        GPIO.setup(GPIOnum,GPIO.IN)

def TurnOnLED(GPIOnum):
    GPIO.output(GPIOnum,True)

def TurnOffLED(GPIOnum):
    GPIO.output(GPIOnum,False)
    
def GetGPIOStatus(GPIOnum):
    GPIO_State = GPIO.input(GPIOnum)
    return GPIO_State

red_pin = 2
yellow_pin = 19
green_pin = 13


if __name__ == "__main__":
    try:
        '''Setup(red_pin,"IN")
        print("The status of the GPIO{0} is {1}".format(red_pin,GetGPIOStatus(red_pin)))
        Setup(red_pin,"OUT")
        
        Setup(yellow_pin,"IN")
        print("The status of the GPIO{0} is {1}".format(yellow_pin,GetGPIOStatus(yellow_pin)))
        Setup(yellow_pin,"OUT")
        
        Setup(green_pin,"IN")
        print("The status of the GPIO{0} is {1}".format(green_pin,GetGPIOStatus(green_pin)))
        Setup(green_pin,"OUT")'''
        
        '''while True:
            #red light 2 sec
            TurnOnLED(red_pin)
            time.sleep(2)
            TurnOffLED(red_pin)
            
            #yellow light shine 5 times
            for i in range (1,5):
                TurnOnLED(yellow_pin)
                time.sleep(0.2)
                TurnOffLED(yellow_pin)
                time.sleep(0.2)
            
            #green light 1 sec
            TurnOnLED(green_pin)
            time.sleep(1)
            TurnOffLED(green_pin)'''

    except KeyboardInterrupt:
        GPIO.cleanup()
