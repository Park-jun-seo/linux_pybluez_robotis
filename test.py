import bluetooth as bt
import time


nearby_devices = bt.discover_devices()
print(nearby_devices)