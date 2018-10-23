import threading
import time
from time import strftime,asctime,ctime,gmtime,mktime
def fun_timer():
	print strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	global timer 
	timer = threading.Timer(1,fun_timer)  
	timer.start()    
timer = threading.Timer(1,fun_timer)  
timer.start()
