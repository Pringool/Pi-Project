from gpiozero import Button as button, LED
import time 



class Settings():
    button1 = button (23)
    button2 = button (24)
    button3 = button (25)
    button4 = button (17)
    button5 = button (27)

    led1 = LED(22)
    led2 = LED(10)
    led3 = LED(9)
    led4 = LED(11)
    led5 = LED(5)

    def leuchten1():
        Settings.led1.on()

    def leuchten2():
        Settings.led2.on()

    def leuchten3():
        Settings.led3.on()

    def leuchten4():
        Settings.led4.on()

    def leuchten5():
        Settings.led5.on()

    
    


Settings.button1.when_pressed = Settings.leuchten1
Settings.button2.when_pressed = Settings.leuchten2
Settings.button3.when_pressed = Settings.leuchten3
Settings.button4.when_pressed = Settings.leuchten4
Settings.button5.when_pressed = Settings.leuchten5







try: 
  while True:
    time.sleep(0.5)
except KeyboardInterrupt: print("Ende") 
