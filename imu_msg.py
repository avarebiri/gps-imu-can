import can

def process_message(msg):
    
    can_id = 0x600   
    data = msg.data
    
    if len(msg.data) < 6:
        print("veri yok")
        
    else:      
        if msg.arbitration_id == can_id:     
            print("x:", data[0])
            print("y:", data[1])
            print("z:", data[2])
            print("raw:", data[3])
            print("pitch:", data[4])
            print("yaw:", data[5])

# Set up the listener to receive messages on the bus
bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000)

notifier =can.Notifier(bus, [process_message])


while True:
    pass