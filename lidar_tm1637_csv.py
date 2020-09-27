#!/usr/bin/env python
# For countdown from keyboardInput
import tm1637
import time
import RPi.GPIO as GPIO
import serial
import pigpio
SERVO = 16
#buzzer = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzer,GPIO.OUT)
#GPIO.output(buzzer,0)
Display = tm1637.TM1637(17,18,tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightnes(1)
ser = serial.Serial(
 port='/dev/ttyS0',
 baudrate = 19200,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
#        print(timeformat, end='\r')
	currenttime = [ int(mins / 10), mins % 10, secs / 10, secs % 10 ]
	Display.Show(currenttime)
	Display.ShowDoublepoint(1)
        time.sleep(1)
        t -= 1
	if t <=0:
		t = 0
		for i in range(3):
	        	currenttime2 = [ int(t / 10), t % 10, t / 10, t % 10 ]
		        Display.Show(currenttime2)
 	        	Display.ShowDoublepoint(1)
			GPIO.output(buzzer,1)
			time.sleep(0.8)
			GPIO.output(buzzer,0)
			time.sleep(0.8)
			Display.Clear()
    print('Goodbye!\n\n\n\n\n')
def distance():
                ser.write("O")
		y=ser.readline()
		time.sleep(0.05)
                ser.write("F")
                dd=ser.readline()
		temp = dd[3:8]
		dist=round(float(temp),2)
		return dist
def disp(dist):
                a=int(dist)/10
                b=int(dist)%10
                c=int(dist*10)%10
                d=int(dist*100)%10
                dist2 = [a,b,c,d]
                print(dist2)
                Display.Show(dist2)
                Display.ShowDoublepoint(1)
		time.sleep(0.1)
def write_li(i,dist):
	with open("lidar.csv", "a") as log:
        	log.write("{0},{1}\n".format(i,dist))


#lidar_str="angel,distance\n"
def write_csv():
	with open("lidar.csv","w") as f:
	       	lidar =f.write(lidar_str)
#lidar = []
try:
	while True:
		pi = pigpio.pi() # Connect to local Pi.
	        for i in range(1600,1700,10):
			print ('i = %d ns' % i)
                	pi.set_servo_pulsewidth(SERVO, i) # Minimum throttle.
			dist =distance()
			disp(dist)
			write_li(i,dist)
			print (dist)
                	time.sleep(10)
                for i in range(1700,1600,-10):
                        print ('i = %d ns' % i)
                        pi.set_servo_pulsewidth(SERVO, i) # Minimum throttle.
                        dist =distance()
                        disp(dist)
                        write_li(i,dist)
                        print (dist)
                        time.sleep(10)
except KeyboardInterrupt:
	ser.write('C')
	Display.Clear()
	GPIO.cleanup()
