from pyModbusTCP.client import ModbusClient
import time

# Replace these values with your Schneider PLC configuration
PLC_IP_ADDRESS = '172.20.20.10'
PLC_PORT = 502
UNIT_ID = 0x1

# Modbus addresses for read and write operations
READ_ADDRESS = 1300  # Replace with the actual Modbus address for reading
WRITE_ADDRESS = 2000  # Replace with the actual Modbus address for writing

# Create a Modbus TCP client
client = ModbusClient()

# Specify the PLC's IP address and port
client.host = PLC_IP_ADDRESS
client.port = PLC_PORT

try:
    # Open the connection to the PLC
    if client.open():
        print(f"Connected to {PLC_IP_ADDRESS}")

        # Read data from the PLC
        read_data = client.read_holding_registers(READ_ADDRESS, 1)
        if read_data:
            print(f"Read data from address {READ_ADDRESS}: {read_data[0]}")
        else:
            print(f"Failed to read data from address {READ_ADDRESS}")

        # Write data to the PLC
        write_data = 456  # Replace with the data you want to write
        if client.write_single_register(WRITE_ADDRESS, write_data):
            print(f"Write data {write_data} to address {WRITE_ADDRESS}")
        else:
            print(f"Failed to write data to address {WRITE_ADDRESS}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection to the PLC
    client.close()
    print("Connection closed")
