# Import the necessary modules
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import time
from adafruit_mcp3xxx.analog_in import AnalogIn

# Get the PIN numbers
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.CE0)

# Load the PIN numbers
mcp = MCP.MCP3008(spi, cs)

# Read the Channel
channel = AnalogIn(mcp, MCP.P2)

# Print the Voltage
while True:
    print('Raw ADC Value: ', channel.value)
    print('ADC Voltage: ' + str(channel.voltage) + 'V')
    print(channel.voltage)
    time.sleep(0.5)