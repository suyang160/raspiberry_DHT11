import RPi.GPIO as GPIO
import time
import socket
from time import strftime,asctime,ctime,gmtime,mktime
import threading
#s=socket.socket()
host = '192.168.0.150'
port = 12345
#s.connect((host,port))
global timer
full_name=" "
last_time=" "
def  DHT11_read():
	global last_time
        flag=1
	a=1
	while flag==1:
			channel =17
			data = []
			j = 0
			 
			GPIO.setmode(GPIO.BCM)
			 
			time.sleep(0.2)
			 
			GPIO.setup(channel, GPIO.OUT)
			GPIO.output(channel, GPIO.LOW)
			time.sleep(0.02)
			GPIO.output(channel, GPIO.HIGH)
			GPIO.setup(channel, GPIO.IN)
			 
			while GPIO.input(channel) == GPIO.LOW:
			  continue
			while GPIO.input(channel) == GPIO.HIGH:
			  continue
			 
			while j < 40:
			  k = 0
			  while GPIO.input(channel) == GPIO.LOW:
			    continue
			  while GPIO.input(channel) == GPIO.HIGH:
			    k += 1
			    if k > 100:
			      break
			  if k < 8:
			    data.append(0)
			  else:
			    data.append(1)
			 
			  j += 1
			 
			humidity_bit = data[0:8]
			humidity_point_bit = data[8:16]
			temperature_bit = data[16:24]
			temperature_point_bit = data[24:32]
			check_bit = data[32:40]
			 
			humidity = 0
			humidity_point = 0
			temperature = 0
			temperature_point = 0
			check = 0
			 
			for i in range(8):
			  humidity += humidity_bit[i] * 2 ** (7-i)
			  humidity_point += humidity_point_bit[i] * 2 ** (7-i)
			  temperature += temperature_bit[i] * 2 ** (7-i)
			  temperature_point += temperature_point_bit[i] * 2 ** (7-i)
			  check += check_bit[i] * 2 ** (7-i)
			 
			tmp = humidity + humidity_point + temperature + temperature_point
			 
			if check == tmp:
				now_time = strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				if now_time != last_time:
				  	print  "temperature:",temperature, "huminity:",humidity, now_time
					last_time=now_time
#				print "a",a
		                flag=0
#			        full_name=str(temperature)+" "+str(humidity)+" "+strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			  #s.sendall(full_name)
			else:
#				print "error"
				a=741		
			GPIO.cleanup()
#	timer = threading.Timer(2, DHT11_read)
#	timer.start()
def shuchu():
	global full_name
	print full_name
	timer = threading.Timer(1, shuchu)
	timer.start()
#timer = threading.Timer(1, shuchu)
#timer.start()
while True:
	DHT11_read()
       #	timer = threading.Timer(2, DHT11_read)
#	timer.start()
timer = threading.Timer(1, shuchu)
timer.start()
