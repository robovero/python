"""General purpose IO client library functions. See LPC17xx 
CMSIS-Compliant Standard Peripheral Firmware Driver Library 
documentation."""
from internals import robocaller, cstruct
from LPC17xx import LPC_GPIO0_BASE, LPC_GPIO1_BASE, LPC_GPIO2_BASE, \
										LPC_GPIO3_BASE, LPC_GPIO4_BASE

GPIO0_Byte = ((LPC_GPIO0_BASE))
GPIO1_Byte = ((LPC_GPIO1_BASE))
GPIO2_Byte = ((LPC_GPIO2_BASE))
GPIO3_Byte = ((LPC_GPIO3_BASE))
GPIO4_Byte = ((LPC_GPIO4_BASE))
GPIO0_HalfWord = ((LPC_GPIO0_BASE))
GPIO1_HalfWord = ((LPC_GPIO1_BASE))
GPIO2_HalfWord = ((LPC_GPIO2_BASE))
GPIO3_HalfWord = ((LPC_GPIO3_BASE))
GPIO4_HalfWord = ((LPC_GPIO4_BASE))

class GPIO_Byte_TypeDef(cstruct):
	pass

class GPIO_HalfWord_TypeDef(cstruct):
	pass

def FIO_IntCmd(portNum, bitValue, edgeState):
	return robocaller("FIO_IntCmd", "void", portNum, bitValue, edgeState)

def GPIO_ClearInt(portNum, bitValue):
	return robocaller("GPIO_ClearInt", "void", portNum, bitValue)

def GPIO_GetIntStatus(portNum, pinNum, edgeState):
	return robocaller("GPIO_GetIntStatus", "FunctionalState", portNum, pinNum, edgeState)

def FIO_HalfWordClearValue(portNum, halfwordNum, bitValue):
	return robocaller("FIO_HalfWordClearValue", "void", portNum, halfwordNum, bitValue)

def GPIO_IntCmd(portNum, bitValue, edgeState):
	return robocaller("GPIO_IntCmd", "void", portNum, bitValue, edgeState)

def FIO_ClearInt(portNum, pinNum):
	return robocaller("FIO_ClearInt", "void", portNum, pinNum)

def FIO_ByteSetValue(portNum, byteNum, bitValue):
	return robocaller("FIO_ByteSetValue", "void", portNum, byteNum, bitValue)

def GPIO_ReadValue(portNum):
	return robocaller("GPIO_ReadValue", "uint32_t", portNum)

def FIO_ByteSetDir(portNum, byteNum, bitValue, dir):
	return robocaller("FIO_ByteSetDir", "void", portNum, byteNum, bitValue, dir)

def FIO_HalfWordSetDir(portNum, halfwordNum, bitValue, dir):
	return robocaller("FIO_HalfWordSetDir", "void", portNum, halfwordNum, bitValue, dir)

def FIO_SetValue(portNum, bitValue):
	return robocaller("FIO_SetValue", "void", portNum, bitValue)

def FIO_GetIntStatus(portNum, pinNum, edgeState):
	return robocaller("FIO_GetIntStatus", "FunctionalState", portNum, pinNum, edgeState)

def FIO_HalfWordSetValue(portNum, halfwordNum, bitValue):
	return robocaller("FIO_HalfWordSetValue", "void", portNum, halfwordNum, bitValue)

def FIO_ByteClearValue(portNum, byteNum, bitValue):
	return robocaller("FIO_ByteClearValue", "void", portNum, byteNum, bitValue)

def FIO_ByteReadValue(portNum, byteNum):
	return robocaller("FIO_ByteReadValue", "uint8_t", portNum, byteNum)

def GPIO_ClearValue(portNum, bitValue):
	return robocaller("GPIO_ClearValue", "void", portNum, bitValue)

def FIO_ClearValue(portNum, bitValue):
	return robocaller("FIO_ClearValue", "void", portNum, bitValue)

def FIO_SetDir(portNum, bitValue, dir):
	return robocaller("FIO_SetDir", "void", portNum, bitValue, dir)

def FIO_SetMask(portNum, bitValue, maskValue):
	return robocaller("FIO_SetMask", "void", portNum, bitValue, maskValue)

def FIO_HalfWordReadValue(portNum, halfwordNum):
	return robocaller("FIO_HalfWordReadValue", "uint16_t", portNum, halfwordNum)

def FIO_ByteSetMask(portNum, byteNum, bitValue, maskValue):
	return robocaller("FIO_ByteSetMask", "void", portNum, byteNum, bitValue, maskValue)

def FIO_ReadValue(portNum):
	return robocaller("FIO_ReadValue", "uint32_t", portNum)

def GPIO_SetValue(portNum, bitValue):
	return robocaller("GPIO_SetValue", "void", portNum, bitValue)

def FIO_HalfWordSetMask(portNum, halfwordNum, bitValue, maskValue):
	return robocaller("FIO_HalfWordSetMask", "void", portNum, halfwordNum, bitValue, maskValue)

def GPIO_SetDir(portNum, bitValue, dir):
	return robocaller("GPIO_SetDir", "void", portNum, bitValue, dir)

