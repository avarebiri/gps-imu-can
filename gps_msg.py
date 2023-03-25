import can
import math

def process_message(msg):
    
    can_id = 0x175   
    data = msg.data


    if len(msg.data) < 2:
        print("veri yok")
        
    else:           
        longitude = data[0]
        latitude = data[1]
        longitude_in_meters = longitude*111319,9*math.cos(latitude*(math.pi/180))
        latitude_in_meters = latitude*113319,9
         
        print("longitude:", longitude)
        print("latitude:", latitude)
        print("longitude in meters", longitude_in_meters)
        print("latitude in meters:", latitude_in_meters)
        
        
# Set up the listener to receive messages on the bus
bus = can.interface.Bus(bustype='socketcan_native', channel='vcan0', bitrate=250000)

notifier =can.Notifier(bus, [process_message])


while True:
    pass