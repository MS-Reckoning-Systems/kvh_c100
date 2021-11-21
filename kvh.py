import serial

def readline(ser):
    eol = b'\r'
    leneol = len(eol)
    line = bytearray()
    while True:
        c = ser.read(1)
        print(c)
        if c:
            line += c
            if line[-leneol:] == eol:
                break
        else:
            break
    return bytes(line) 

try:
  ser = serial.Serial('/dev/ttyS0', 4800, bytesize=8, parity='N', stopbits=1, timeout=1)
  while ser:
    ser.write(b'=?r\r')
    msg = ser.read(2)
    # print(ser.readline().decode('ascii', errors='replace'))
    print(msg[1], msg[1].hex(), chr(int(msg[1].hex(), 16)), int(msg[1].hex(), 16))
    # print(bytearray.fromhex(ser.read(1).hex()).decode())
    # byte_array = bytearray.fromhex(msg[1].hex())
    # print(byte_array)
    print(str(msg[1],'utf-8'))
except Exception as e:
  print(e)
  ser.close()