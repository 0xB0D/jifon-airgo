#!/usr/bin/env python3
import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 2, mode = 'rtu')  # port name, slave address (in decimal)
instrument.serial.timeout = 1.0

# All register values appear as +1 in the datasheet
#instrument.write_register(3014, 19.8, 1)
htemperature = instrument.read_register(1004, 1)  # Registernumber, number of decimals
wtemperature = instrument.read_register(1006, 1)  # Registernumber, number of decimals
alarms = instrument.read_register(1900, 0)
c1_run_hour = instrument.read_register(8104, 0)
heater_run_hour = instrument.read_register(8105, 0)
setpoint = instrument.read_register(3014, 1)
high_water_set = instrument.read_register(3017, 1)
enable_motor_protection = instrument.read_register(3007, 1)
digital_input_bitmask = instrument.read_register(1000, 0)
digital_output_bitmask = instrument.read_register(1002, 0)

print('Hall temperature = %f' % htemperature)
print('Setpoint = %f' % setpoint)
print('Water temperature = %f' % wtemperature)
print('High water tempterature control = %f' % high_water_set)
print('Enable Motor protection = %d' % enable_motor_protection)
print('Compressor Runtime = %d hours' % c1_run_hour)
print('Backup heater Runtime = %d hours' % heater_run_hour)

print('Digital input bitmask %x' % digital_input_bitmask)
if digital_input_bitmask & 0x100:
    print('\tHigh pressure')
if digital_input_bitmask & 0x200:
    print('\tLow pressure')
if digital_input_bitmask & 0x400:
    print('\tMotor protection')

print('Digital output bitmask %x' % digital_output_bitmask)
if digital_output_bitmask & 0x100:
    print('\tHeat pump active')
if digital_output_bitmask & 0x200:
    print('\tBackup Heater active')
if digital_output_bitmask & 0x1000:
    print('\tAlarm active')

print('Alarms = %x' % alarms)
if alarms & 0x100:
    print('\tRoom temperature sensor error')
if alarms & 0x200:
    print('\tWater outlet temperature sensor error')
if alarms & 0x400:
    print('\tLow pressure alarm')
if alarms & 0x800:
    print('\tHigh pressure alarm')
if alarms & 0x1000:
    print('\tMotor Protection')
if alarms & 0x2000:
    print('\tHigh water temp alarm')

## Change temperature setpoint (SP) ##
#NEW_TEMPERATURE = 95
#instrument.write_register(24, NEW_TEMPERATURE, 1)  #
