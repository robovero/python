"""Nested vector interrupt controller client library functions. See 
LPC17xx CMSIS-Compliant Standard Peripheral Firmware Driver Library 
documentation."""
from internals import robocaller, cstruct

def NVIC_SetVTOR(offset):
	return robocaller("NVIC_SetVTOR", "void", offset)

def NVIC_SCBDeInit():
	return robocaller("NVIC_SCBDeInit", "void", )

def NVIC_DeInit():
	return robocaller("NVIC_DeInit", "void", )

