import random
import asyncio
import time
from kasa import Discover
from kasa import SmartBulb
#kasa library found here -> https://github.com/python-kasa/python-kasa

#devices = asyncio.run(Discover.discover())
#print(type(devices))
#for addr,dev in devices.items():
	#print(addr,dev)

bulb = SmartBulb("192.168.1.204")
asyncio.run(bulb.update())
start = time.time()
if not bulb.is_on:
	asyncio.run(bulb.turn_on())
	#asyncio.run(bulb.update())
delay = 0
changes = 501
#print(on)
for i in range(1,changes):
	#delay = random.randint(0,5000)
	h, s, v = random.randint(0,360), random.randint(0,100), random.randint(0,100)
	brightness = random.randint(0,100)
	order = random.randint(0,10000)
	#if order < 50:
		#asyncio.run(bulb.set_brightness(brightness))
		#asyncio.run(bulb.set_hsv(h, s, v,transition=delay))
	#else:
	asyncio.run(bulb.set_hsv(h, s, v,transition=delay))
		#asyncio.run(bulb.set_brightness(brightness))
	#time.sleep(delay/1000)
	#print(i+1,"changes completed","delay: ", delay)
	#print('h: ', h, 's: ', s, 'v: ',v)
	#print('remaining: ', 5000-i)
	#asyncio.run(bulb.update())
end = time.time()
print('done','run time of ', changes-1, 'changes is ', end-start)
#asyncio.run(bulb.turn_off(transition=delay))
#print(bulb.is_on)