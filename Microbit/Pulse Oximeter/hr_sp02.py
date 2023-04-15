import serial

from firebase import firebase

myDB = firebase.FirebaseApplication("https://lcbrief-default-rtdb.firebaseio.com/")

import serial.tools.list_ports as myPorts
for port in myPorts.comports():
    print(port)
    
mySer=serial.Serial()
mySer.baudrate = 115200
mySer.port = "COM3"

mySer.open()

while True:
    data = str(mySer.readline())
    data = data.replace(" ", " ")
    data = data.replace("'", " ")
    data = data.replace("b", " ")
    data = data.replace("\\r\\n ", " ")
    if len(data) > 1:
        myDataIn = data.split(":")
        spo2 = myDataIn[0]
        hr = myDataIn[1]
        print("\n\n")
       
        csvFile = open("spo2_micro.csv","a")
        csvFile.write(spo2 +"\n")
        csvFile.close()
        
        csvFile = open("hr_micro.csv","a")
        csvFile.write(hr +"\n")
        csvFile.close()
        
        csvFile = open("allData.csv","a")
        csvFile.write(spo2 + ","  + hr + "\n")
        csvFile.close()
        
        
        
        record = {
            "microbithr" : hr
            }
        record2 = {
            "microbitspo2" : spo2
            }
        myDB.post("/microbit1/", record)
        myDB.post("/microbit2/", record2)
        
        

