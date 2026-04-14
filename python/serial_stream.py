import serial
import time

class XYStreamer:
    def __init__(self, port="COM3", baud=115200):
        self.ser = serial.Serial(port, baud)

    def send(self, xs, ys):
        for x, y in zip(xs, ys):
            msg = f"{int(x*100)} {int(y*100)}\n"
            self.ser.write(msg.encode())
            time.sleep(0.001)
