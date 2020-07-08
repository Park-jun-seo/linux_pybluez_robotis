import bluetooth as bt
import time

#######################################################
# 검색
#######################################################
#print(bt.discover_devices())

target_name = "ROBOTIS BT-210"   # target device name
target_address = "00:00:00:00:00:00" # target device address
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

#######################################################
# 통신
#######################################################
   
try:
    sock=bt.BluetoothSocket(bt.RFCOMM)
    sock.connect((target_address, port))

    while True:         
        try:
            '''
            ##로보티즈 조종기 패킷##
            0xff, 0x55, 0x00, 0xff, 0x00, 0xff #0
            0xff, 0x55, 0x01, 0xfe, 0x00, 0xff #U
            0xff, 0x55, 0x02, 0xfd, 0x00, 0xff #D
            0xff, 0x55, 0x04, 0xfb, 0x00, 0xff #L
            0xff, 0x55, 0x08, 0xf7, 0x00, 0xff #R
            '''
            data = [0xff,0x55,0x04,0xfb,0x00,0xff]   #L 버튼     
            dataarr = bytes(bytearray(data))         
            sock.send(dataarr)                       #전송           
            time.sleep(1)
        except KeyboardInterrupt:
            print("disconnected")
            sock.close()
            print("all done")
except bt.btcommon.BluetoothError as err:
    print('An error occurred : %s ' % err)
    pass