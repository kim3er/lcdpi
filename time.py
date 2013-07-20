#!/usr/bin/python
# -*- coding: utf-8 -*-

from gpio_lcd import lcd
import time
from datetime import datetime

my_lcd = lcd.Lcd()

if __name__ == "__main__":
	while True:
		my_lcd.write_line(datetime.now().strftime('%T'), lcd.LCD_LINE_2, lcd.center)
		my_lcd.write_line('Oliver smells', lcd.LCD_LINE_3, lcd.center)
		time.sleep(60)
