"""Example application that outputs accelerometer, compass and gyro readings.
"""

from robovero.extras import Array, roboveroConfig
from robovero.lpc17xx_i2c import I2C_M_SETUP_Type, I2C_MasterTransferData, \
														I2C_TRANSFER_OPT_Type
from robovero.lpc17xx_gpio import GPIO_ReadValue
from robovero.LPC17xx import LPC_I2C0
from robovero.lpc_types import Status
import time

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

accel_ctrl_reg1 = 0x20
accel_x_low = 0x28
accel_x_high = 0x29
accel_y_low = 0x2A
accel_y_high = 0x2B
accel_z_low = 0x2C
accel_z_high = 0x2D

compass_mr_reg = 0x02
compass_x_high = 0x03
compass_x_low = 0x04
compass_y_high = 0x05
compass_y_low = 0x06
compass_z_high = 0x07
compass_z_low = 0x08

gyro_ctrl_reg1 = 0x20
gyro_ctrl_reg2 = 0x21
gyro_ctrl_reg3 = 0x22
gyro_ctrl_reg4 = 0x23
gyro_ctrl_reg5 = 0x24
gyro_status_reg = 0x27
gyro_x_low = 0x28
gyro_x_high = 0x29
gyro_y_low = 0x2A
gyro_y_high = 0x2B
gyro_z_low = 0x2C
gyro_z_high = 0x2D
gyro_fifo_ctrl_reg = 0x2E

class I2CDevice(object):
	def __init__(self, address):
		self.config = I2C_M_SETUP_Type()
		self.tx_data = Array(2, 1)
		self.rx_data = Array(1, 1)
		self.config.sl_addr7bit = address
		self.config.tx_data = self.tx_data.ptr
		self.config.retransmissions_max = 3

	def readReg(self, register):
		self.tx_data[0] = register
		self.config.tx_length = 1
		self.config.rx_data = self.rx_data.ptr
		self.config.rx_length = 1	
		ret = I2C_MasterTransferData(LPC_I2C0, self.config.ptr,
																	I2C_TRANSFER_OPT_Type.I2C_TRANSFER_POLLING)
		if ret == Status.ERROR:
			exit("I2C Read Error")		
		return self.rx_data[0]
		
	def writeReg(self, register, value):
		self.tx_data[0] = register
		self.tx_data[1] = value
		self.config.tx_length = 2
		self.config.rx_data = 0
		self.config.rx_length = 0
		ret = I2C_MasterTransferData(LPC_I2C0, self.config.ptr,
																	I2C_TRANSFER_OPT_Type.I2C_TRANSFER_POLLING)
		if ret == Status.ERROR:
			exit("I2C Write Error")
		if self.readReg(register) != value:
			exit("I2C Verification Error")
		return None

# Initialize pin select registers
roboveroConfig()

# configure accelerometer
accelerometer = I2CDevice(0x18)
accelerometer.writeReg(accel_ctrl_reg1, 0x27)

# configure compass
compass = I2CDevice(0x1E)
compass.writeReg(compass_mr_reg, 0)	# continuous measurement mode

# configure the gyro
# from the L3G4200D Application Note:
# 1. Write CTRL_REG2
# 2. Write CTRL_REG3
# 3. Write CTRL_REG4
# 4. Write CTRL_REG6
# 5. Write Reference
# 6. Write INT1_THS
# 7. Write INT1_DUR
# 8. Write INT1_CFG
# 9. Write CTRL_REG
# 10. Write CTRL_REG
gyro = I2CDevice(0x68)
gyro.writeReg(gyro_ctrl_reg3, 0x08) # enable DRDY
gyro.writeReg(gyro_ctrl_reg4, 0x80) # enable block data read mode
gyro.writeReg(gyro_ctrl_reg1, 0x0F)	# normal mode, enable all axes

def twosComplement(low_byte, high_byte):
	"""Unpack 16-bit twos complement representation of the result.
	"""
	return (((low_byte + (high_byte << 8)) + 2**15) % 2**16 - 2**15)

while True:
	print "a [x, y, z]: ",
	print [
		twosComplement(accelerometer.readReg(accel_x_low), accelerometer.readReg(accel_x_high)),
		twosComplement(accelerometer.readReg(accel_y_low), accelerometer.readReg(accel_y_high)),
		twosComplement(accelerometer.readReg(accel_z_low), accelerometer.readReg(accel_z_high))
	]

	print "c [x, y, z]: ",
	print [
		twosComplement(compass.readReg(compass_x_low), compass.readReg(compass_x_high)),
		twosComplement(compass.readReg(compass_y_low), compass.readReg(compass_y_high)),
		twosComplement(compass.readReg(compass_z_low), compass.readReg(compass_z_high))
	]
	
	print "g [x, y, z]: ",
	print [
		twosComplement(gyro.readReg(gyro_x_low), gyro.readReg(gyro_x_high)),
		twosComplement(gyro.readReg(gyro_y_low), gyro.readReg(gyro_y_high)),
		twosComplement(gyro.readReg(gyro_z_low), gyro.readReg(gyro_z_high))
	]
	
	print ""
	time.sleep(1)


