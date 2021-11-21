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
    # ser.write(b'd0\r')
    msg = bytearray(["64", "30"])
    print(msg)
    ser.write(msg)
    print(ser.read(19).decode('ascii', errors='replace'))
    # print(ser.read(19))
    # print(int(ser.read(1).hex(), 16))
    # print(bytearray.fromhex(ser.read(1).hex()).decode())
except Exception as e:
  print(e)
  ser.close()