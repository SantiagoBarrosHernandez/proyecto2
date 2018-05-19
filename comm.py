import  serial

puerto =serial.Serial('/dev/tty.usbmodem1421')

while(True) :
    datos = str (serial.Serial.readline(puerto))
    print(datos)