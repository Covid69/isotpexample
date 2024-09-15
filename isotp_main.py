import isotp
import logging
import time
import can
#from can.interfaces.vector import VectorBus
# def my_error_handler(error):
# logging.warning('IsoTp error happened : %s - %s' % (error.__class__.__name__, str(error)))   

def my_error_handler(error):
    # Called from a different thread, needs to be thread safe
    logging.warning('IsoTp error happened : %s - %s' % (error.__class__.__name__, str(error)))
    
bus = can.interface.Bus(interface='socketcan', channel='vcan0', bitrate=500000)
addr = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=0x123, txid=0x456)
stack = isotp.CanStack(bus, address=addr, error_handler=my_error_handler)

try:
    stack.start()

    stack.send(b'Hello, this is a long payload sent in small chunks')    # Non-blocking send, does not raise exception.
    while stack.transmitting():
        time.sleep(0.005)

    print("Payload transmission done.") # May have failed, use the error_handler to know
finally:
    stack.stop()
    bus.shutdown()