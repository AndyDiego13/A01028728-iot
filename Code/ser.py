#fd = open("hola.txt","w")
#fd.readline()
#for line in fd:
    #print(line)
#a se salta porque es la linea 1
#b
#c

import serial

ser = serial.Serial("/dev/cu.usbmodem14101",9600)
while(1):
    lineBytes=ser.readline()
    line=lineBytes.decode("ascii")
    if line[0:2] != "HR":
        continue
    #QUITAMOS EL /N/R
    line=line.rstrip()#HR:118;ML:1704
    medidas = line.split(";")#["HR:118", "ML:1704"]
    hr = int(medidas[0].split(":")[1])#SE SEPARA EL HR DEL VALOR NUMERICO ["HR", "118"] toma el 118, lo convierte a int y lo guarda
    milis = int(medidas[1].split(":")[1])#["ML", "1704"]
    print(hr)