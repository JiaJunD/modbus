from pyModbusTCP.client import ModbusClient
import random
c = ModbusClient(host="localhost", port=502, unit_id=87, auto_open=True)


# Write Single Coil
# if c.write_single_coil(32, False):
if c.write_single_coil(32, False):
    print("write ok")
else:
    print("write error")

    
# Write Multiple Coils
write_coil_data = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
# write_coil_data = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
if c.write_multiple_coils(48, write_coil_data):
    print("write ok")
else:
    print("write error")


# Write Single Register 
c.write_single_register
if c.write_single_register(30, random.randint(0,65535)):
    print("write ok")
else:
    print("write error")

    
# Write Multiple Registers
if c.write_multiple_registers(40, random.sample(range(0, 65535), 10)):
    print("write ok")
else:
    print("write error")


