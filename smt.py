#!/usr/bin/env python
"""
sms.py - Used to send txt messages.
"""
import serial
import time
 
class TextMessage:
    def __init__(self, recipient="0123456789", message="TextMessage.content not set."):
        self.recipient = recipient
        self.content = message
 
    def setRecipient(self, number):
        self.recipient = number
 
    def setContent(self, message):
        self.content = message
 
    def connectPhone(self):
        self.ser = serial.Serial('COM5', 115200, timeout=5)
        time.sleep(1)
 
    def sendMessage(self):
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)
 
    def disconnectPhone(self):
        self.ser.close()

sms = TextMessage("9840048416","From 3G Modem : using python script ... ")
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()

	
