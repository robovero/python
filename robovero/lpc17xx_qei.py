"""Quadrature encoder interface client library functions. Find implementation
details in LPC17xx CMSIS-Compliant Standard Peripheral Firmware Driver Library
documentation."""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"


# QEI Reset types
# Reset position counter
QEI_RESET_POS = (1)
# Reset Position Counter on Index
QEI_RESET_POSOnIDX = (2)
# Reset Velocity
QEI_RESET_VEL = (4)
# Reset Index Counter
QEI_RESET_IDX  = (8)

# QEI Direction Invert Type Option
# Direction is not inverted
QEI_DIRINV_NONE = (0)
# Direction is complemented
QEI_DIRINV_CMPL = (1)

# QEI Signal Mode Option
# Signal operation: Quadrature phase mode
QEI_SIGNALMODE_QUAD = (0)
# Signal operation: Clock/Direction mode
QEI_SIGNALMODE_CLKDIR = (1)

# QEI Capture Mode Option
# Capture mode: Only Phase-A edges are counted (2X)
QEI_CAPMODE_2X = (0)
# Capture mode: BOTH PhA and PhB edges are counted (4X)
QEI_CAPMODE_4X = (1)

# QEI Invert Index Signal Option
# Invert Index signal option: None
QEI_INVINX_NONE = (0)
# Invert Index signal option: Enable
QEI_INVINX_EN = (1)

# QEI timer reload option
# Reload value in absolute value
QEI_TIMERRELOAD_TICKVAL = (0)  
# Reload value in microsecond value
QEI_TIMERRELOAD_USVAL = (1)  

# QEI Flag Status type 
# Direction status
QEI_STATUS_DIR = (1<<0)  

# QEI Compare Position channel option
# QEI compare position channel 0
QEI_COMPPOS_CH_0 = (0)
# QEI compare position channel 1
QEI_COMPPOS_CH_1 = (1)
# QEI compare position channel 2
QEI_COMPPOS_CH_2 = (2)

# QEI interrupt flag type
# index pulse was detected interrupt
QEI_INTFLAG_INX_Int = (1<<0)  
# Velocity timer over flow interrupt
QEI_INTFLAG_TIM_Int = (1<<1)  
# Capture velocity is less than compare interrupt
QEI_INTFLAG_VELC_Int = (1<<2)  
# Change of direction interrupt
QEI_INTFLAG_DIR_Int = (1<<3)  
# An encoder phase error interrupt
QEI_INTFLAG_ERR_Int = (1<<4)  
# An encoder clock pulse was detected interrupt
QEI_INTFLAG_ENCLK_Int = (1<<5)  
# position 0 compare value is equal to the current position interrupt
QEI_INTFLAG_POS0_Int = (1<<6)  
# position 1 compare value is equal to the current position interrupt
QEI_INTFLAG_POS1_Int = (1<<7)  
# position 2 compare value is equal to the current position interrupt
QEI_INTFLAG_POS2_Int = (1<<8)  
# Index compare value is equal to the current index count interrupt
QEI_INTFLAG_REV_Int = (1<<9)  
# Combined position 0 and revolution count interrupt
QEI_INTFLAG_POS0REV_Int = (1<<10)  
# Combined position 1 and revolution count interrupt
QEI_INTFLAG_POS1REV_Int = (1<<11)  
# Combined position 2 and revolution count interrupt
QEI_INTFLAG_POS2REV_Int = (1<<12)


class QEI_CFG_Type(cstruct):
  '''QEI Configuration structure type definition.
  
   DirectionInvert:  1-bit Direction invert option:
                    - QEI_DIRINV_NONE: QEI Direction is normal
                    - QEI_DIRINV_CMPL: QEI Direction is complemented
  SignalMode: 1-bit Signal mode Option:
              - QEI_SIGNALMODE_QUAD: Signal is in Quadrature phase mode
              - QEI_SIGNALMODE_CLKDIR: Signal is in Clock/Direction mode
  CaptureMode:  1-bit Capture Mode Option:
                - QEI_CAPMODE_2X: Only Phase-A edges are counted (2X)
                - QEI_CAPMODE_4X: BOTH Phase-A and Phase-B edges are counted (4X)
  InvertIndex:  1-bit Invert Index Option:
                - QEI_INVINX_NONE: the sense of the index input is normal
                - QEI_INVINX_EN: inverts the sense of the index input
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
  
  '''
  pass

class QEI_RELOADCFG_Type(cstruct):
  '''Timer Reload Configuration structure type definition.
  
   ReloadOption: Velocity Timer Reload Option, should be:
                - QEI_TIMERRELOAD_TICKVAL: Reload value in absolute value
                - QEI_TIMERRELOAD_USVAL: Reload value in microsecond value
  ReloadValue:  Velocity Timer Reload Value, 32-bit long, should be matched
                with Velocity Timer Reload Option
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

def QEI_GetTimer(QEIx):
  '''Get current timer counter in QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  return: Current timer counter in QEI peripheral
  
  '''
  return robocaller("QEI_GetTimer", "uint32_t", QEIx)

def QEI_DeInit(QEIx):
  '''De-initializes the QEI peripheral registers to their default reset values.
  
  QEIx: QEI peripheral, should be LPC_QEI
  
  '''
  return robocaller("QEI_DeInit", "void", QEIx)

def QEI_GetPosition(QEIx):
  '''Get current position value in QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  return: Current position value of QEI peripheral
  
  '''
  return robocaller("QEI_GetPosition", "uint32_t", QEIx)

def QEI_GetStatus(QEIx, ulFlagType):
  '''Check whether if specified flag status is set or not.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulFlagType: Status Flag Type, should be one of the following:
              - QEI_STATUS_DIR: Direction Status
  return: New Status of this status flag (SET or RESET)
  
  '''
  return robocaller("QEI_GetStatus", "FlagStatus", QEIx, ulFlagType)

def QEI_Reset(QEIx, ulResetType):
  '''Resets value for each type of QEI value, such as velocity, counter, 
  position, etc.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulResetType: QEI Reset Type, should be one of the following:
              - QEI_RESET_POS: Reset Position Counter
              - QEI_RESET_POSOnIDX: Reset Position Counter on Index signal
              - QEI_RESET_VEL: Reset Velocity
              - QEI_RESET_IDX: Reset Index Counter
  
  '''
  return robocaller("QEI_Reset", "void", QEIx, ulResetType)

def QEI_SetMaxPosition(QEIx, ulMaxPos):
  '''Set max position value for QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulMaxPos: Max position value to set
  
  '''
  return robocaller("QEI_SetMaxPosition", "void", QEIx, ulMaxPos)

def QEI_GetVelocity(QEIx):
  '''Get current velocity pulse counter in current time period.
  
  QEIx: QEI peripheral, should be LPC_QEI
  return: Current velocity pulse counter value
  
  '''
  return robocaller("QEI_GetVelocity", "uint32_t", QEIx)

def QEI_GetVelocityCap(QEIx):
  '''Get the most recently measured velocity of the QEI. When the Velocity timer
  in QEI is over-flow, the current velocity value will be loaded into Velocity 
  Capture register..
  
  QEIx: QEI peripheral, should be LPC_QEI
  return: The most recently measured velocity value
  
  '''
  return robocaller("QEI_GetVelocityCap", "uint32_t", QEIx)

def QEI_SetPositionComp(QEIx, bPosCompCh, ulPosComp):
  '''Set position compare value for QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  bPosCompCh: Compare Position channel, should be:
               - QEI_COMPPOS_CH_0: QEI compare position channel 0
               - QEI_COMPPOS_CH_1: QEI compare position channel 1
               - QEI_COMPPOS_CH_2: QEI compare position channel 2
  ulPosComp:  Compare Position value to set
    
  '''
  return robocaller("QEI_SetPositionComp", "void", QEIx, bPosCompCh, ulPosComp)

def QEI_SetDigiFilter(QEIx, ulSamplingPulse):
  '''Set value of sampling count for the digital filter in QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulSamplingPulse: Value of sampling count to set
  
  '''
  return robocaller("QEI_SetDigiFilter", "void", QEIx, ulSamplingPulse)

def QEI_IntSet(QEIx, ulIntType):
  '''Sets (forces) specified interrupt in QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulIntType:  Interrupt Flag Status type, should be:
              - QEI_INTFLAG_INX_Int: index pulse was detected interrupt
              - QEI_INTFLAG_TIM_Int: Velocity timer over flow interrupt
              - QEI_INTFLAG_VELC_Int: Capture velocity is less than compare
                interrupt
              - QEI_INTFLAG_DIR_Int: Change of direction interrupt
              - QEI_INTFLAG_ERR_Int: An encoder phase error interrupt
              - QEI_INTFLAG_ENCLK_Int: An encoder clock pulse was detected
                interrupt
              - QEI_INTFLAG_POS0_Int: position 0 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_POS1_Int: position 1 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_POS2_Int: position 2 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_REV_Int: Index compare value is equal to the current
                index count interrupt
              - QEI_INTFLAG_POS0REV_Int: Combined position 0 and revolution 
                count interrupt
              - QEI_INTFLAG_POS1REV_Int: Combined position 1 and revolution 
                count interrupt
              - QEI_INTFLAG_POS2REV_Int: Combined position 2 and revolution 
                count interrupt
  
  '''
  return robocaller("QEI_IntSet", "void", QEIx, ulIntType)

def QEI_GetIndex(QEIx):
  '''Get current index counter of QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  return: Current value of QEI index counter
  
  '''
  return robocaller("QEI_GetIndex", "uint32_t", QEIx)

def QEI_SetTimerReload(QEIx, QEIReloadStruct):
  '''Set timer reload value for QEI peripheral. When the velocity timer is
  over-flow, the value that set for Timer Reload register will be loaded
  into the velocity timer for next period. The calculated velocity in RPM
  therefore will be affect by this value..
  
  QEIx: QEI peripheral, should be LPC_QEI
  QEIReloadStruct: QEI reload structure
  
  '''
  return robocaller("QEI_SetTimerReload", "void", QEIx, QEIReloadStruct)

def QEI_ConfigStructInit(QIE_InitStruct):
  '''Fills each QIE_InitStruct member with its default value.
  
  - DirectionInvert = QEI_DIRINV_NONE
  - SignalMode = QEI_SIGNALMODE_QUAD
  - CaptureMode = QEI_CAPMODE_4X
  - InvertIndex = QEI_INVINX_NONE.
  
  QIE_InitStruct: Pointer to a QEI_CFG_Type structure which will be 
                  initialized.
  
  '''
  return robocaller("QEI_ConfigStructInit", "void", QIE_InitStruct)

def QEI_SetVelocityComp(QEIx, ulVelComp):
  '''Set Velocity Compare value for QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulVelComp:  Compare Velocity value to set
    
  '''
  return robocaller("QEI_SetVelocityComp", "void", QEIx, ulVelComp)

def QEI_Init(QEIx, QEI_ConfigStruct):
  '''Initializes the QEI peripheral according to the specified parameters in the
  QEI_ConfigStruct.
  
  QEIx: QEI peripheral, should be LPC_QEI
  QEI_ConfigStruct: Pointer to a QEI_CFG_Type structure that contains the 
                    configuration information for the specified QEI peripheral
    
  '''
  return robocaller("QEI_Init", "void", QEIx, QEI_ConfigStruct)

def QEI_IntCmd(QEIx, ulIntType, NewState):
  '''Enable/Disable specified interrupt in QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulIntType:  Interrupt Flag Status type, should be:
              - QEI_INTFLAG_INX_Int: index pulse was detected interrupt
              - QEI_INTFLAG_TIM_Int: Velocity timer over flow interrupt
              - QEI_INTFLAG_VELC_Int: Capture velocity is less than compare
                interrupt
              - QEI_INTFLAG_DIR_Int: Change of direction interrupt
              - QEI_INTFLAG_ERR_Int: An encoder phase error interrupt
              - QEI_INTFLAG_ENCLK_Int: An encoder clock pulse was detected
                interrupt
              - QEI_INTFLAG_POS0_Int: position 0 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_POS1_Int: position 1 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_POS2_Int: position 2 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_REV_Int: Index compare value is equal to the current
                index count interrupt
              - QEI_INTFLAG_POS0REV_Int: Combined position 0 and revolution 
                count interrupt
              - QEI_INTFLAG_POS1REV_Int: Combined position 1 and revolution 
                count interrupt
              - QEI_INTFLAG_POS2REV_Int: Combined position 2 and revolution 
                count interrupt
  NewState: New function state, should be:
            - DISABLE
            - ENABLE
  
  '''
  return robocaller("QEI_IntCmd", "void", QEIx, ulIntType, NewState)

def QEI_IntClear(QEIx, ulIntType):
  '''Clear (force) specified interrupt (pending) in QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulIntType:  Interrupt Flag Status type, should be:
              - QEI_INTFLAG_INX_Int: index pulse was detected interrupt
              - QEI_INTFLAG_TIM_Int: Velocity timer over flow interrupt
              - QEI_INTFLAG_VELC_Int: Capture velocity is less than compare
                interrupt
              - QEI_INTFLAG_DIR_Int: Change of direction interrupt
              - QEI_INTFLAG_ERR_Int: An encoder phase error interrupt
              - QEI_INTFLAG_ENCLK_Int: An encoder clock pulse was detected
                interrupt
              - QEI_INTFLAG_POS0_Int: position 0 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_POS1_Int: position 1 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_POS2_Int: position 2 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_REV_Int: Index compare value is equal to the current
                index count interrupt
              - QEI_INTFLAG_POS0REV_Int: Combined position 0 and revolution 
                count interrupt
              - QEI_INTFLAG_POS1REV_Int: Combined position 1 and revolution 
                count interrupt
              - QEI_INTFLAG_POS2REV_Int: Combined position 2 and revolution 
                count interrupt
  
  '''
  return robocaller("QEI_IntClear", "void", QEIx, ulIntType)

def QEI_GetIntStatus(QEIx, ulIntType):
  '''Check whether if specified interrupt flag status in QEI peripheral
  is set or not.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulIntType:  Interrupt Flag Status type, should be:
              - QEI_INTFLAG_INX_Int: index pulse was detected interrupt
              - QEI_INTFLAG_TIM_Int: Velocity timer over flow interrupt
              - QEI_INTFLAG_VELC_Int: Capture velocity is less than compare
                interrupt
              - QEI_INTFLAG_DIR_Int: Change of direction interrupt
              - QEI_INTFLAG_ERR_Int: An encoder phase error interrupt
              - QEI_INTFLAG_ENCLK_Int: An encoder clock pulse was detected
                interrupt
              - QEI_INTFLAG_POS0_Int: position 0 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_POS1_Int: position 1 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_POS2_Int: position 2 compare value is equal to the
                current position interrupt
              - QEI_INTFLAG_REV_Int: Index compare value is equal to the current
                index count interrupt
              - QEI_INTFLAG_POS0REV_Int: Combined position 0 and revolution 
                count interrupt
              - QEI_INTFLAG_POS1REV_Int: Combined position 1 and revolution 
                count interrupt
              - QEI_INTFLAG_POS2REV_Int: Combined position 2 and revolution 
                count interrupt 
  return: New State of specified interrupt flag status (SET or RESET)
  
  '''
  return robocaller("QEI_GetIntStatus", "FlagStatus", QEIx, ulIntType)

def QEI_CalculateRPM(QEIx, ulVelCapValue, ulPPR):
  '''Calculates the actual velocity in RPM passed via velocity capture value and
  Pulse Per Round (of the encoder) value parameter input.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulVelCapValue:  Velocity capture input value from QEI_GetVelocityCap() 
                  function
  ulPPR:  Pulse per round of encoder
  return: The actual value of velocity in RPM (revolutions per minute)
  
  '''
  return robocaller("QEI_CalculateRPM", "uint32_t", QEIx, ulVelCapValue, ulPPR)

def QEI_SetIndexComp(QEIx, ulIndexComp):
  '''Set value for index compare in QEI peripheral.
  
  QEIx: QEI peripheral, should be LPC_QEI
  ulIndexComp:  Compare Index Value to set
  
  '''
  return robocaller("QEI_SetIndexComp", "void", QEIx, ulIndexComp)
