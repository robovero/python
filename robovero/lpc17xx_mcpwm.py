"""Motor control PWM client library functions. See LPC17xx 
CMSIS-Compliant Standard Peripheral Firmware Driver Library 
documentation."""
from internals import robocaller, cstruct

MCPWM_CHANNEL_EDGE_MODE = ((0))
MCPWM_CHANNEL_CENTER_MODE = ((1))
MCPWM_CHANNEL_PASSIVE_LO = ((0))
MCPWM_CHANNEL_PASSIVE_HI = ((1))
MCPWM_PATENT_A0 = ((1<<0))	
MCPWM_PATENT_B0 = ((1<<1))	
MCPWM_PATENT_A1 = ((1<<2))	
MCPWM_PATENT_B1 = ((1<<3))	
MCPWM_PATENT_A2 = ((1<<4))	
MCPWM_PATENT_B2 = ((1<<5))	

def MCPWM_CON_RUN(n):
	if ((n>=0)and(n<=2)):
		return ((1<<((n*8)+0)))
	else: return (0)		

def MCPWM_CON_CENTER(n):
	if ((n>=0)and(n<=2)):
		return ((1<<((n*8)+1)))
	else: return (0)
	
def MCPWM_CON_POLAR(n):
	if ((n>=0)and(n<=2)):
		return ((1<<((n*8)+2)))
	else: return (0)

def MCPWM_CON_DTE(n):
	if ((n>=0)and(n<=2)):
		return ((1<<((n*8)+3)))
	else: return (0)		

def MCPWM_CON_DISUP(n):
	if ((n>=0)and(n<=2)):
		return ((1<<((n*8)+4)))
	else: return (0)		

MCPWM_CON_INVBDC = ((1<<29))										
MCPWM_CON_ACMODE = ((1<<30))										
MCPWM_CON_DCMODE = ((1<<31))				
						
def MCPWM_CAPCON_CAPMCI_RE(cap,mci):
	if ((cap>=0)and(cap<=2)and(mci>=0)and(mci<=2)):
		return ((1<<((cap*6)+(mci*2)+0)))
	else: return (0)

def MCPWM_CAPCON_CAPMCI_FE(cap,mci):
	if ((cap>=0)and(cap<=2)and(mci>=0)and(mci<=2)):
		return ((1<<((cap*6)+(mci*2)+1)))
	else: return (0)

def MCPWM_CAPCON_RT(n):
	if ((n>=0)and(n<=2)):
		return ((1<<(18+(n))))
	else: return (0)

def MCPWM_CAPCON_HNFCAP(n):
	if ((n>=0)and(n<=2)):
		return ((1<<(21+(n))))
	else: return (0)

def MCPWM_INT_ILIM(n):
	if ((n>=0)and(n<=2)):
		return ((1<<((n*4)+0)))
	else: return (0)

def MCPWM_INT_IMAT(n):
	if ((n>=0)and(n<=2)):
		return ((1<<((n*4)+1)))
	else: return (0)

def MCPWM_INT_ICAP(n):
	if ((n>=0)and(n<=2)):
		return ((1<<((n*4)+2)))
	else: return (0)

MCPWM_INT_ABORT = ((1<<15))

def MCPWM_CNTCON_TCMCI_RE(tc,mci):
	if ((tc>=0)and(tc<=2)and(mci>=0)and(mci<=2)):
		return ((1<<((6*tc)+(2*mci)+0)))
	else: return (0)
	
def MCPWM_CNTCON_TCMCI_FE(tc,mci):
	if ((tc>=0)and(tc<=2)and(mci>=0)and(mci<=2)):
		return ((1<<((6*tc)+(2*mci)+1)))
	else: return (0)
	
def MCPWM_CNTCON_CNTR(n):
	if ((n>=0)and(n<=2)):
		return ((1<<(29+n)))
	else: return (0)

def MCPWM_DT(n,x):
	if ((n>=0)and(n<=2)):
		return (((x&0x3FF)<<(n*10)))
	else: return (0)
	
MCPWM_CP_A0 = ((1<<0))	
MCPWM_CP_B0 = ((1<<1))	
MCPWM_CP_A1 = ((1<<2))	
MCPWM_CP_B1 = ((1<<3))	
MCPWM_CP_A2 = ((1<<4))	
MCPWM_CP_B2 = ((1<<5))

def MCPWM_CAPCLR_CAP(n):
	if ((n>=0)and(n<=2)):
		return ((1<<n))
	else: return (0)

MCPWM_INTFLAG_LIM0 = MCPWM_INT_ILIM(0)
MCPWM_INTFLAG_MAT0 = MCPWM_INT_IMAT(0)
MCPWM_INTFLAG_CAP0 = MCPWM_INT_ICAP(0)
MCPWM_INTFLAG_LIM1 = MCPWM_INT_ILIM(1)
MCPWM_INTFLAG_MAT1 = MCPWM_INT_IMAT(1)
MCPWM_INTFLAG_CAP1 = MCPWM_INT_ICAP(1)
MCPWM_INTFLAG_LIM2 = MCPWM_INT_ILIM(2)
MCPWM_INTFLAG_MAT2 = MCPWM_INT_IMAT(2)
MCPWM_INTFLAG_CAP2 = MCPWM_INT_ICAP(2)
MCPWM_INTFLAG_ABORT = MCPWM_INT_ABORT

class MCPWM_CHANNEL_CFG_Type(cstruct):
	pass

class MCPWM_COUNT_CFG_Type(cstruct):
	pass

class MCPWM_CAPTURE_CFG_Type(cstruct):
	pass

def MCPWM_ConfigCapture(MCPWMx, channelNum, captureConfig):
	return robocaller("MCPWM_ConfigCapture", "void", MCPWMx, channelNum, captureConfig)

def MCPWM_IntConfig(MCPWMx, ulIntType, NewState):
	return robocaller("MCPWM_IntConfig", "void", MCPWMx, ulIntType, NewState)

def MCPWM_ACMode(MCPWMx, acMode):
	return robocaller("MCPWM_ACMode", "void", MCPWMx, acMode)

def MCPWM_Init(MCPWMx):
	return robocaller("MCPWM_Init", "void", MCPWMx)

def MCPWM_GetIntStatus(MCPWMx, ulIntType):
	return robocaller("MCPWM_GetIntStatus", "FlagStatus", MCPWMx, ulIntType)

def MCPWM_Stop(MCPWMx, channel0, channel1, channel2):
	return robocaller("MCPWM_Stop", "void", MCPWMx, channel0, channel1, channel2)

def MCPWM_Start(MCPWMx, channel0, channel1, channel2):
	return robocaller("MCPWM_Start", "void", MCPWMx, channel0, channel1, channel2)

def MCPWM_GetCapture(MCPWMx, captureChannel):
	return robocaller("MCPWM_GetCapture", "uint32_t", MCPWMx, captureChannel)

def MCPWM_IntSet(MCPWMx, ulIntType):
	return robocaller("MCPWM_IntSet", "void", MCPWMx, ulIntType)

def MCPWM_ConfigChannel(MCPWMx, channelNum, channelSetup):
	return robocaller("MCPWM_ConfigChannel", "void", MCPWMx, channelNum, channelSetup)

def MCPWM_ClearCapture(MCPWMx, captureChannel):
	return robocaller("MCPWM_ClearCapture", "void", MCPWMx, captureChannel)

def MCPWM_DCMode(MCPWMx, dcMode, outputInvered, outputPattern):
	return robocaller("MCPWM_DCMode", "void", MCPWMx, dcMode, outputInvered, outputPattern)

def MCPWM_CountConfig(MCPWMx, channelNum, countMode, countConfig):
	return robocaller("MCPWM_CountConfig", "void", MCPWMx, channelNum, countMode, countConfig)

def MCPWM_WriteToShadow(MCPWMx, channelNum, channelSetup):
	return robocaller("MCPWM_WriteToShadow", "void", MCPWMx, channelNum, channelSetup)

def MCPWM_IntClear(MCPWMx, ulIntType):
	return robocaller("MCPWM_IntClear", "void", MCPWMx, ulIntType)

