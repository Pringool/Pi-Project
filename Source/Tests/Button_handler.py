from gpiozero import Button as button
import time 

button1 = button (24)
button2 = button (25)
button3 = button (23)



def test1():
    print("Button 1")

def test2():
    print("Button 2")

def test3():
    print("Button 3")


button1.when_pressed = test1

button2.when_pressed = test2

button3.when_pressed = test3

try: 
  while True:
    time.sleep(0.5)
except KeyboardInterrupt: print("Ende") 
