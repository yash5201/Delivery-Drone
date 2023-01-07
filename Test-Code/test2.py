import serial

# Set up the serial connection to the Arduino board
ser = serial.Serial('COM7', 115200)

def read_sensors():
  # Read the sensor data from the Arduino
  data = ser.readline()
  # Split the data into a list of values
  values = data.split(',')
  # Convert the values to floats
  values = [float(v) for v in values]
  return values

while True:
  # Read the sensor data
  sensor_data = read_sensors()
  # Print the data to the console
  print(sensor_data)
