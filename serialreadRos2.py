'''
This is an example of how to connect via python to the serial port. For example, you can connect an arduino and read what it posts via the serial port.
author : Maarten Dequanter
'''


import serial

ser = serial.Serial(
        port='/dev/ttyUSB1',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while True:
    # Reading all bytes available bytes till EOL
    line = ser.readline() 
    if line:
        # Converting Byte Strings into unicode strings
        string = line.decode()  
        # Converting Unicode String into integer
        print(string)

ser.close()