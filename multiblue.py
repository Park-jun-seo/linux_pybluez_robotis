import bluetooth as bt
import time

#######################################################
# 검색
#######################################################
taget_num = 2
target_address1 = "B8:63:BC:00:48:C8" # target device address
target_address2 = "B8:63:BC:00:76:47" # target device address
address_arr = []
address_arr.append(target_address1)
address_arr.append(target_address2)
port = 1         # RFCOMM port


while True :
    nearby_devices = bt.discover_devices()
    arr=[]
    find_address=[]
    for i in range(len(address_arr)):
        arr.append(address_arr[i])
    print("in arr : %s"%arr)
    
    for i in range(taget_num) :
        if nearby_devices.count(address_arr[i]) !=0  :
            find_address.append(address_arr[i])
            del arr[arr.index(address_arr[i])]
    if len(arr) == 0:
        print("all find!")
        print(find_address)
        break
    elif len(arr) != 0:
        print("all not find : %s"%arr)


#######################################################
# 통신
#######################################################
'''
##로보티즈 조종기 패킷##
0xff,0x55,0x00,0xff,0x00,0xff #0
0xff,0x55,0x01,0xfe,0x00,0xff #U
0xff,0x55,0x02,0xfd,0x00,0xff #D
0xff,0x55,0x04,0xfb,0x00,0xff #L
0xff,0x55,0x08,0xf7,0x00,0xff #R
'''
Z = [0xff,0x55,0x00,0xff,0x00,0xff]   #0 버튼    
U = [0xff,0x55,0x01,0xfe,0x00,0xff]   #U 버튼  
D = [0xff,0x55,0x02,0xfd,0x00,0xff]   #D 버튼  
R = [0xff,0x55,0x08,0xf7,0x00,0xff]   #R 버튼  
L = [0xff,0x55,0x04,0xfb,0x00,0xff]   #L 버튼  

try:
    sock1=bt.BluetoothSocket(bt.RFCOMM)
    sock2=bt.BluetoothSocket(bt.RFCOMM)
    sock1.connect((address_arr[0], port))
    sock2.connect((address_arr[1], port))
    while True:         
        try:
                
            dataarrL = bytes(bytearray(L))   
            dataarrU = bytes(bytearray(U))        
            sock1.send(dataarrU)    #전송   
            sock2.send(dataarrL)    #전송           
            
            dataarrZ = bytes(bytearray(Z))         
            sock1.send(dataarrZ)    #전송   
            sock2.send(dataarrZ)    #전송    
            time.sleep(3)
        except KeyboardInterrupt:
            print("disconnected")
            sock1.close()
            sock2.close()
            print("all done")
except bt.btcommon.BluetoothError as err:
    print('An error occurred : %s ' % err)
    pass