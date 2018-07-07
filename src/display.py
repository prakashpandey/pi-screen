#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import display_conf
import utils

lcd = display_conf.get_lcd()

def show_msg(msg, how_long):
    lcd.message(msg)
    time.sleep(how_long)
    lcd.clear()


if __name__ == "__main__":
    now = utils.get_time()
    ip = utils.get_host_ip()
    msg = now + "\n" + ip

    show_msg(msg, 10)
