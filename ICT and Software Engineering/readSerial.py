import serial

# Note: replace "COM1" with the COM port of your Arduino
ser = serial.Serial("COM4", baudrate=9600, timeout=1)

while True:
    # Check how many characters are in the serial buffer
    bytes_serial = ser.inWaiting()

    # Only read if data is available
    if bytes_serial > 0:
        # Read the byte array, decode it to a string, and remove newline characters
        data = ser.readline().decode().strip()
        print(data)
