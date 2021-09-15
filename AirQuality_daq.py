import serial
port=serial.Serial("/dev/serial0",baudrate=9600,timeout=1.5)
text=port.read(32)
int.from_bytes(text[5:7],byteorder="big")
int.from_bytes(text[7:9],byteorder="big")
int.from_bytes(text[9:11],byteorder="big")
