from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="localhost", port=502, unit_id=87, auto_open=True)

# Read Coils
regs = c.read_coils(16, 16)

if regs:
    print(regs)
else:
    print("read error")

# Read Holding Register
regs = c.read_holding_registers(10, 10)

if regs:
    print(regs)
else:
    print("read error")

# Read Discrete Inputs
regs = c.read_discrete_inputs(32,16)

if regs:
    print(regs)
else:
    print("read error")

# Write Single Coil
if c.write_single_coil(18, False):
    print("write ok")
else:
    print("write error")

