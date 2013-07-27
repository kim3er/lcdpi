#!/usr/bin/python
# -*- coding: utf-8 -*-

from gpio_lcd import lcd
import time
from datetime import datetime
import urllib2
import json
import logging

log_file = '/home/pi/lcd_error.log'
logging.basicConfig(filename=log_file,level=logging.DEBUG,)

my_lcd = lcd.Lcd()

if __name__ == "__main__":
	logging.debug('Script started: ' + datetime.now().strftime('%T'))

	while True:
		try:
			text = urllib2.urlopen('http://www.dogma.co.uk/lcd.html').read()
			obj = json.loads(text)
			my_lcd.write_line(obj['1'], lcd.LCD_LINE_1, lcd.center)
			my_lcd.write_line(datetime.now().strftime('%T'), lcd.LCD_LINE_2, lcd.center)
			my_lcd.write_line(obj['3'], lcd.LCD_LINE_3, lcd.center)
			my_lcd.write_line(obj['4'], lcd.LCD_LINE_4, lcd.center)
			time.sleep(60)
		except:
			logging.exception('Got exception on main handler' + datetime.now().strftime('%T'))
			raise
