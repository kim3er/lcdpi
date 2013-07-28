#!/usr/bin/python
# -*- coding: utf-8 -*-

from gpio_lcd import lcd
import time
from datetime import datetime
import urllib2
import json
import logging
import pystache
import atexit

log_file = '/home/pi/lcd_error.log'
logging.basicConfig(filename=log_file,level=logging.DEBUG,)

my_lcd = lcd.Lcd()

def log(text, type = 'exception'):
	getattr(logging, type)('[' + datetime.now().strftime('%T') + '] ' + text)

def stache(text, context):
	return pystache.render(text, context)

def goodbye():
	log('Goodbye', 'debug')
	my_lcd.__del__()

atexit.register(goodbye)

if __name__ == "__main__":
	log('Script started', 'debug')

	try:
		while True:
			try:
				text = urllib2.urlopen('http://www.dogma.co.uk/lcd.html').read()
			except:
				log('Unable to contact server')
				continue

			try:
				obj = json.loads(text)
			except:
				log('Invalid JSON returned from server')
				continue

			context = { 'd': datetime.now().strftime('%T') }

			my_lcd.write_line(stache(obj['1'], context), lcd.LCD_LINE_1, lcd.center)
			my_lcd.write_line(stache(obj['2'], context), lcd.LCD_LINE_2, lcd.center)
			my_lcd.write_line(stache(obj['3'], context), lcd.LCD_LINE_3, lcd.center)
			my_lcd.write_line(stache(obj['4'], context), lcd.LCD_LINE_4, lcd.center)

			time.sleep(60)
	except:
		log('Got exception on main handler')
		raise

