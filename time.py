#!/usr/bin/python
# -*- coding: utf-8 -*-

from gpio-lcd import lcd
import time
from datetime import datetime

my_lcd = lcd.Lcd()

while True:
	my_lcd.write_line(datetime.now().strftime('%T'), lcd.LCD_LINE_2, lcd.center)
	my_lcd.write_line('Oliver smells', lcd.LCD_LINE_3, lcd.center)
	time.sleep(60)