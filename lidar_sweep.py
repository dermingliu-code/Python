#!/usr/bin/env python
# esc_start.py
# 2015-04-14
# Public Domain
#
# Sends the servo pulses needed to initialise some ESCs
#
# Requires the pigpio daemon to be running
#
# sudo pigpiod
import time
import pigpio
SERVO = 16
try:
        while True:
                pi = pigpio.pi() # Connect to local Pi.
                for i in range(500,2500,5):
                        print  ('i = %d ns' % i)
                        pi.set_servo_pulsewidth(SERVO, i) # Minimum throttle.
                        time.sleep(0.01)
                for i in range(2500,500,-5):
                        print  ('i = %d ns' % i)
                        pi.set_servo_pulsewidth(SERVO, i) # Minimum throttle.
                        time.sleep(0.01)
except KeyboardInterrupt:
        pi.set_servo_pulsewidth(SERVO, 0)
        pi.stop()

