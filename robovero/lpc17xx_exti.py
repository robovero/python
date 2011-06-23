"""External interrupt client library functions. See LPC17xx CMSIS-Compliant
Standard Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc"
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

EXTI_EINT0_BIT_MARK = 0x01
EXTI_EINT1_BIT_MARK = 0x02
EXTI_EINT2_BIT_MARK = 0x04
EXTI_EINT3_BIT_MARK = 0x08

class EXTI_MODE_ENUM:
	EXTI_MODE_LEVEL_SENSITIVE = 0
	EXTI_MODE_EDGE_SENSITIVE = 1

class EXTI_InitTypeDef(cstruct):
	pass

class EXTI_POLARITY_ENUM:
	EXTI_POLARITY_LOW_ACTIVE_OR_FALLING_EDGE = 0
	EXTI_POLARITY_HIGH_ACTIVE_OR_RISING_EDGE = 1

class EXTI_LINE_ENUM:
	EXTI_EINT0 = 0
	EXTI_EINT1 = 1
	EXTI_EINT2 = 2
	EXTI_EINT3 = 3

def EXTI_Init():
	return robocaller("EXTI_Init", "void", )

def EXTI_ClearEXTIFlag(EXTILine):
	return robocaller("EXTI_ClearEXTIFlag", "void", EXTILine)

def EXTI_Config(EXTICfg):
	return robocaller("EXTI_Config", "void", EXTICfg)

def EXTI_SetMode(EXTILine, mode):
	return robocaller("EXTI_SetMode", "void", EXTILine, mode)

def EXTI_DeInit():
	return robocaller("EXTI_DeInit", "void", )

def EXTI_SetPolarity(EXTILine, polarity):
	return robocaller("EXTI_SetPolarity", "void", EXTILine, polarity)

