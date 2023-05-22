from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="localhost", port=502, unit_id=87, auto_open=True)

# Read Discrete Inputs
print("Read Discrete Inputs\n\t",end="")
regs = c.read_discrete_inputs(32,16)
if regs:
    print(regs)
else:
    print("read error")

# Read Coils
print("Read Coils\n\t",end="")
regs = c.read_coils(16, 16)
if regs:
    print(regs)
else:
    print("read error")

# Read Input Registers
print("Read Input Registers\n\t",end="")
regs = c.read_input_registers(20, 10)
if regs:
    print(regs)
else:
    print("read error")

# Read Holding Register
print("Read Holding Register\n\t",end="")
regs = c.read_holding_registers(10, 10)
if regs:
    print(regs)
else:
    print("read error")


c.close()