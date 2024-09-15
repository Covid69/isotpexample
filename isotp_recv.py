import isotp
import logging
import can
import time

# Set up logging for ISO-TP errors
logging.basicConfig(level=logging.WARNING)
def my_error_handler(error):
    logging.warning('ISO-TP error happened: %s - %s' % (error.__class__.__name__, str(error)))

# Initialize the CAN bus
bus = can.interface.Bus(interface='socketcan', channel='vcan1', bitrate=500000)

# Configure ISO-TP address
addr = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=0x456, txid=0x123)

# Create ISO-TP stack
stack = isotp.CanStack(bus, address=addr, params={"stmin": 0x7F})

# Main loop for receiving
while True:
    stack.process()
    if stack.available():
        try:
            payload = stack.recv()
            print("Received payload: %s" % payload)
            break
        except Exception as e:
            logging.error("Failed to receive payload: %s" % str(e))
    time.sleep(0.01)  # Adding a small delay to avoid busy-waiting
