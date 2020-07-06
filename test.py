import bluetooth as bt

#######################################################
# Scan
#######################################################
#print(bt.discover_devices())

target_name = "ROBOTIS BT-210"   # target device name
target_address = "B8:63:BC:00:48:C8"
port = 1         # RFCOMM port

nearby_devices = bt.discover_devices()

# scanning for target device
for bdaddr in nearby_devices:
    print(bt.lookup_name( bdaddr ))
    if target_name == bt.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print('device found. target address %s' % target_address)
else:
    print('could not find target bluetooth device nearby')
   
try:
    sock=bt.BluetoothSocket(bt.RFCOMM)
    sock.connect((target_address, port))

    while True:         
        try:
            
            data = b"\xff\x55\x00\xff\x00\xff"
            sock.send(data)
        except KeyboardInterrupt:
            print("disconnected")
            sock.close()
            print("all done")
except bt.btcommon.BluetoothError as err:
    print('An error occurred : %s ' % err)
    pass