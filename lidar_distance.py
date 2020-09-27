#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import serial
ser = serial.Serial(
 port='/dev/ttyS0',
 baudrate = 19200,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)
counter=0
while 1:
 ser.write("O")
 y=ser.readline()
 time.sleep(0.05)
 ser.write("D")
 dist=ser.readline()
 dd = round(float(dist[3:8]),2)
 k=int(dd/10)
 print(k)
 print(dd)
 time.sleep(0.5)



