import RPi.GPIO as GPIO
import time

servo_pin = 18  # GPIO18（物理ピン12）

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# 周波数50HzでPWM制御開始
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_angle(angle):
    duty = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)  # サーボ保持をオフに（省電力）

try:
    while True:
        set_angle(90)
        time.sleep(1)
        set_angle(0)
        time.sleep(1)
        set_angle(180)
        time.sleep(1)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
