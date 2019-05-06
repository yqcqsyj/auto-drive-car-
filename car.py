import RPi.GPIO as GPIO 
import time

R_En = 15
R_F = 13
R_B = 11
L_En = 36
L_F = 40
L_B = 38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)                         
GPIO.setup(R_En,GPIO.OUT)             
GPIO.setup(R_F,GPIO.OUT)             
GPIO.setup(R_B,GPIO.OUT)            
GPIO.setup(L_En,GPIO.OUT)            
GPIO.setup(L_F,GPIO.OUT)
GPIO.setup(L_B,GPIO.OUT)

def car_move_forward():
    GPIO.output(R_En,GPIO.HIGH)
    GPIO.output(R_F,GPIO.HIGH)
    GPIO.output(R_B,GPIO.LOW)
    GPIO.output(L_En,GPIO.HIGH)
    GPIO.output(L_F,GPIO.HIGH)
    GPIO.output(L_B,GPIO.LOW)
    
def car_move_backward():
    GPIO.output(R_En,GPIO.HIGH)
    GPIO.output(R_F,GPIO.LOW)
    GPIO.output(R_B,GPIO.HIGH)
    GPIO.output(L_En,GPIO.HIGH)
    GPIO.output(L_F,GPIO.LOW)
    GPIO.output(L_B,GPIO.HIGH)

def car_turn_left():
    GPIO.output(R_En,GPIO.HIGH)
    GPIO.output(R_F,GPIO.LOW)
    GPIO.output(R_B,GPIO.HIGH)
    GPIO.output(L_En,GPIO.HIGH)
    GPIO.output(L_F,GPIO.HIGH)
    GPIO.output(L_B,GPIO.LOW)

def car_turn_right():
    GPIO.output(R_En,GPIO.HIGH)
    GPIO.output(R_F,GPIO.HIGH)
    GPIO.output(R_B,GPIO.LOW)
    GPIO.output(L_En,GPIO.HIGH)
    GPIO.output(L_F,GPIO.LOW)
    GPIO.output(L_B,GPIO.HIGH)

def car_back_left():
    GPIO.output(R_En,GPIO.HIGH)
    GPIO.output(R_F,GPIO.LOW)
    GPIO.output(R_B,GPIO.HIGH)
    GPIO.output(L_En,GPIO.HIGH)
    GPIO.output(L_F,GPIO.HIGH)
    GPIO.output(L_B,GPIO.HIGH)

def car_back_right():
    GPIO.output(R_En,GPIO.HIGH)
    GPIO.output(R_F,GPIO.HIGH)
    GPIO.output(R_B,GPIO.HIGH)
    GPIO.output(L_En,GPIO.HIGH)
    GPIO.output(L_F,GPIO.LOW)
    GPIO.output(L_B,GPIO.HIGH)
    
def clean_GPIO():
    GPIO.cleanup()
def car_stop():
    GPIO.output(R_En,GPIO.HIGH)
    GPIO.output(R_F,GPIO.HIGH)
    GPIO.output(R_B,GPIO.HIGH)
    GPIO.output(L_En,GPIO.HIGH)
    GPIO.output(L_F,GPIO.HIGH)
    GPIO.output(L_B,GPIO.HIGH)
    
if __name__ == '__main__':
	car_move_forward()
	clean_GPIO()