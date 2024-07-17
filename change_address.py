import serial
import time

serialPort = serial.Serial(
    port="COM4", baudrate=115200
)
serialPort.write(b'AT+ADDRESS=4\r\n')


ser_bytes = serialPort.readline().decode("Ascii")
print(ser_bytes)