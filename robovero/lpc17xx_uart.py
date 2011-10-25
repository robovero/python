"""UART client library functions. Find implementation details in LPC17xx 
CMSIS-Compliant Standard Peripheral Firmware Driver Library documentation.
"""

from internals import robocaller, cstruct

__author__ =      "Neil MacMunn"
__credits__ =     ["Neil MacMunn", "NXP MCU SW Application Team"]
__maintainer__ =  "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2011, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"

# UART time-out definitions in case of using Read() and Write function with 
# Blocking Flag mode
UART_BLOCKING_TIMEOUT = (0xFFFFFFFF)

# End of auto-baud interrupt
UART_IIR_ABEO_INT = ((1<<8))   
# Auto-baud time-out interrupt
UART_IIR_ABTO_INT = ((1<<9))

# Line status register: Receive data ready
UART_LSR_RDR = ((1<<0))   
# Line status register: Overrun error
UART_LSR_OE = ((1<<1))   
# Line status register: Parity error
UART_LSR_PE = ((1<<2))   
# Line status register: Framing error
UART_LSR_FE = ((1<<3))   
# Line status register: Break interrupt
UART_LSR_BI = ((1<<4))   
# Line status register: Transmit holding register empty
UART_LSR_THRE = ((1<<5))   
# Line status register: Transmitter empty
UART_LSR_TEMT = ((1<<6))   
# Error in RX FIFO
UART_LSR_RXFE = ((1<<7))

# Set upon state change of input CTS
UART1_MSR_DELTA_CTS = ((1<<0))  
# Set upon state change of input DSR
UART1_MSR_DELTA_DSR = ((1<<1))  
# Set upon low to high transition of input RI
UART1_MSR_LO2HI_RI = ((1<<2))  
# Set upon state change of input DCD
UART1_MSR_DELTA_DCD = ((1<<3))  
# Clear To Send State
UART1_MSR_CTS = ((1<<4))  
# Data Set Ready State
UART1_MSR_DSR = ((1<<5))  
# Ring Indicator State
UART1_MSR_RI = ((1<<6))  
# Data Carrier Detect State
UART1_MSR_DCD = ((1<<7)) 

class UART_AB_MODE_Type:
  '''UART Auto-baudrate mode type definition.
  
  UART_AUTOBAUD_MODE0:  UART Auto baudrate Mode 0
  UART_AUTOBAUD_MODE1:  UART Auto baudrate Mode 1
  
  '''
  UART_AUTOBAUD_MODE0 = 0
  UART_AUTOBAUD_MODE1 = 1

class UART1_RS485_CTRLCFG_Type(cstruct):
  '''UART1 Full modem -  RS485 Control configuration type.
  
  NormalMultiDropMode_State:  Normal MultiDrop mode State:
                              - ENABLE: Enable this function.
                              - DISABLE: Disable this function.
  Rx_State: Receiver State:
            - ENABLE: Enable Receiver.
            - DISABLE: Disable Receiver.
  AutoAddrDetect_State: Auto Address Detect mode state:
                        - ENABLE: ENABLE this function.
                        - DISABLE: Disable this function.
  AutoDirCtrl_State:  Auto Direction Control State:
                      - ENABLE: Enable this function.
                      - DISABLE: Disable this function.
  DirCtrlPin: If direction control is enabled, state:
              - UART1_RS485_DIRCTRL_RTS: pin RTS is used for direction control.
              - UART1_RS485_DIRCTRL_DTR: pin DTR is used for direction control.
  DirCtrlPol_Level: Polarity of the direction control signal on  the RTS (or DTR)
                    pin:
                    - RESET:  The direction control pin will be driven to logic 
                              "0" when the transmitter has data to be sent.
                    - SET:  The direction control pin will be driven to logic
                            "1" when the transmitter has data to be sent.
  MatchAddrValue: address match value for RS-485/EIA-485 mode, 8-bit long
  DelayValue: delay time is in periods of the baud clock, 8-bit long
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class UART_IrDA_PULSE_Type:
  '''UART IrDA Control type Definition.
  
  UART_IrDA_PULSEDIV2:  Pulse width = 2 * Tpclk
                        - Configures the pulse when FixPulseEn = 1
  UART_IrDA_PULSEDIV4:  Pulse width = 4 * Tpclk
                        - Configures the pulse when FixPulseEn = 1
  UART_IrDA_PULSEDIV8:  Pulse width = 8 * Tpclk
                      - Configures the pulse when FixPulseEn = 1
  UART_IrDA_PULSEDIV16: Pulse width = 16 * Tpclk
                        - Configures the pulse when FixPulseEn = 1
  UART_IrDA_PULSEDIV32: Pulse width = 32 * Tpclk
                        - Configures the pulse when FixPulseEn = 1
  UART_IrDA_PULSEDIV64: Pulse width = 64 * Tpclk
                        - Configures the pulse when FixPulseEn = 1
  UART_IrDA_PULSEDIV128:  Pulse width = 128 * Tpclk
                          - Configures the pulse when FixPulseEn = 1
  UART_IrDA_PULSEDIV256:  Pulse width = 256 * Tpclk
                          - Configures the pulse when FixPulseEn = 1

  '''
  UART_IrDA_PULSEDIV2 = 0
  UART_IrDA_PULSEDIV4 = 1
  UART_IrDA_PULSEDIV8 = 2
  UART_IrDA_PULSEDIV16 = 3
  UART_IrDA_PULSEDIV32 = 4
  UART_IrDA_PULSEDIV64 = 5
  UART_IrDA_PULSEDIV128 = 6
  UART_IrDA_PULSEDIV256 = 7

class UART_MODEM_PIN_Type:
  '''Modem output pin type definition.
  
  UART1_MODEM_PIN_DTR: Source for modem output pin DTR
  UART1_MODEM_PIN_RTS:  Source for modem output pin RTS
  
  '''
  UART1_MODEM_PIN_DTR = 0
  UART1_MODEM_PIN_RTS = 1

class UART_FIFO_CFG_Type(cstruct):
  '''UART FIFO Configuration Structure definition.
  
  FIFO_ResetRxBuf:  Reset Rx FIFO command state , should be:
                    - ENABLE: Reset Rx FIFO in UART
                    - DISABLE: Do not reset Rx FIFO  in UART
  FIFO_ResetTxBuf:  Reset Tx FIFO command state , should be:
                  - ENABLE: Reset Tx FIFO in UART
                  - DISABLE: Do not reset Tx FIFO  in UART
  FIFO_DMAMode: DMA mode, should be:
                - ENABLE: Enable DMA mode in UART
                - DISABLE: Disable DMA mode in UART
  FIFO_Level: Rx FIFO trigger level, should be:
              - UART_FIFO_TRGLEV0: UART FIFO trigger level 0: 1 character
              - UART_FIFO_TRGLEV1: UART FIFO trigger level 1: 4 character
              - UART_FIFO_TRGLEV2: UART FIFO trigger level 2: 8 character
              - UART_FIFO_TRGLEV3: UART FIFO trigger level 3: 14 character
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).

  '''
  pass

class UART_STOPBIT_Type:
  '''UART Stop bit type definitions.
  
  UART_STOPBIT_1: UART 1 Stop Bits Select
  UART_STOPBIT_2: UART Two Stop Bits Select
  
  '''
  UART_STOPBIT_1 = (0)
  UART_STOPBIT_2 = 1

class UART_ABEO_Type:
  '''UART End of Auto-baudrate type definition.  
  
  UART_AUTOBAUD_INTSTAT_ABEO: UART End of auto-baud interrupt
  UART_AUTOBAUD_INTSTAT_ABTO: UART Auto-baud time-out interrupt
  
  '''
  UART_AUTOBAUD_INTSTAT_ABEO = UART_IIR_ABEO_INT
  UART_AUTOBAUD_INTSTAT_ABTO = UART_IIR_ABTO_INT

class UART_RS485_DIRCTRL_PIN_Type:
  '''UART Direction Control Pin type definition.
  
  UART1_RS485_DIRCTRL_RTS:  Pin RTS is used for direction control
  UART1_RS485_DIRCTRL_DTR:  Pin DTR is used for direction control
  
  '''
  UART1_RS485_DIRCTRL_RTS = 0
  UART1_RS485_DIRCTRL_DTR = 1

class UART1_SignalState:
  '''UART1 Full modem -  Signal states definition.
  
  INACTIVE: In-active state
  ACTIVE: Active state
  
  '''
  INACTIVE = 0
  ACTIVE = 1

class UART_CFG_Type(cstruct):
  '''UART Configuration Structure definition.
  
  Baud_rate:  UART baud rate
  Parity: Parity selection, should be:
          - UART_PARITY_NONE: No parity
          - UART_PARITY_ODD: Odd parity
          - UART_PARITY_EVEN: Even parity
          - UART_PARITY_SP_1: Forced "1" stick parity
          - UART_PARITY_SP_0: Forced "0" stick parity
  Databits: Number of data bits, should be:
            - UART_DATABIT_5: UART 5 bit data mode
            - UART_DATABIT_6: UART 6 bit data mode
            - UART_DATABIT_7: UART 7 bit data mode
            - UART_DATABIT_8: UART 8 bit data mode
  Stopbits: Number of stop bits, should be:
            - UART_STOPBIT_1: UART 1 Stop Bits Select
            - UART_STOPBIT_2: UART 2 Stop Bits Select
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).          
  '''
  pass

class UART_AB_CFG_Type(cstruct):
  '''Auto Baudrate mode configuration type definition.
  
  ABMode: Autobaudrate mode
  AutoRestart:  Auto Restart state
  ptr:  LPC1769 memory address where structure is stored. Use this in place of
        the C reference operator (&).
        
  '''
  pass

class UART_MODEM_MODE_Type:
  '''UART Modem mode type definition.
  
  UART1_MODEM_MODE_LOOPBACK:  Loop back mode select
  UART1_MODEM_MODE_AUTO_RTS:  Enable Auto RTS flow-control
  UART1_MODEM_MODE_AUTO_CTS:  Enable Auto CTS flow-control
  
  '''
  UART1_MODEM_MODE_LOOPBACK = 0
  UART1_MODEM_MODE_AUTO_RTS = 1
  UART1_MODEM_MODE_AUTO_CTS = 2

class UART_FITO_LEVEL_Type:
  '''FIFO Level type definitions.
  
  UART_FIFO_TRGLEV0:  UART FIFO trigger level 0: 1 character
  UART_FIFO_TRGLEV1:  UART FIFO trigger level 1: 4 character
  UART_FIFO_TRGLEV2:  UART FIFO trigger level 2: 8 character
  UART_FIFO_TRGLEV3:  UART FIFO trigger level 3: 14 character
  
  '''
  UART_FIFO_TRGLEV0 = 0
  UART_FIFO_TRGLEV1 = 1
  UART_FIFO_TRGLEV2 = 2
  UART_FIFO_TRGLEV3 = 3

class UART_INT_Type:
  '''UART Interrupt Type definitions.
  
  UART_INTCFG_RBR:  RBR Interrupt enable
  UART_INTCFG_THRE: THR Interrupt enable
  UART_INTCFG_RLS:  RX line status interrupt enable
  UART1_INTCFG_MS:  Modem status interrupt enable (UART1 only)
  UART1_INTCFG_CTS: CTS1 signal transition interrupt enable (UART1 only)
  UART_INTCFG_ABEO: Enables the end of auto-baud interrupt
  UART_INTCFG_ABTO: Enables the auto-baud time-out interrupt
  
  '''
  UART_INTCFG_RBR = 0
  UART_INTCFG_THRE = 1
  UART_INTCFG_RLS = 2
  UART1_INTCFG_MS = 3
  UART1_INTCFG_CTS = 4
  UART_INTCFG_ABEO = 5
  UART_INTCFG_ABTO = 6

class UART_LS_Type:
  '''UART Line Status Type definition.
  
  UART_LINESTAT_RDR: Line status register: Receive data ready
  UART_LINESTAT_OE: Line status register: Overrun error
  UART_LINESTAT_PE: Line status register: Parity error
  UART_LINESTAT_FE: Line status register: Framing error
  UART_LINESTAT_BI: Line status register: Break interrupt
  UART_LINESTAT_THRE: Line status register: Transmit holding register empty
  UART_LINESTAT_TEMT: Line status register: Transmitter empty
  UART_LINESTAT_RXFE: Error in RX FIFO
    
  '''
  UART_LINESTAT_RDR = UART_LSR_RDR
  UART_LINESTAT_OE = UART_LSR_OE
  UART_LINESTAT_PE = UART_LSR_PE
  UART_LINESTAT_FE = UART_LSR_FE
  UART_LINESTAT_BI = UART_LSR_BI
  UART_LINESTAT_THRE = UART_LSR_THRE
  UART_LINESTAT_TEMT = UART_LSR_TEMT
  UART_LINESTAT_RXFE = UART_LSR_RXFE

class UART_DATABIT_Type:
  '''UART Databit type definitions.
  
  UART_DATABIT_5: UART 5 bit data mode
  UART_DATABIT_6: UART 6 bit data mode
  UART_DATABIT_7: UART 7 bit data mode
  UART_DATABIT_8: UART 8 bit data mode
  
  '''
  UART_DATABIT_5 = 0
  UART_DATABIT_6 = 1
  UART_DATABIT_7 = 2
  UART_DATABIT_8 = 3

class UART_MODEM_STAT_type:
  '''UART modem status type definition.
  
  UART1_MODEM_STAT_DELTA_CTS: Set upon state change of input CTS
  UART1_MODEM_STAT_DELTA_DSR: Set upon state change of input DSR
  UART1_MODEM_STAT_LO2HI_RI:  Set upon low to high transition of input RI
  UART1_MODEM_STAT_DELTA_DCD: Set upon state change of input DCD
  UART1_MODEM_STAT_CTS: Clear To Send State
  UART1_MODEM_STAT_DSR: Data Set Ready State
  UART1_MODEM_STAT_RI:  Ring Indicator State
  UART1_MODEM_STAT_DCD: Data Carrier Detect State
    
  '''
  UART1_MODEM_STAT_DELTA_CTS = UART1_MSR_DELTA_CTS
  UART1_MODEM_STAT_DELTA_DSR = UART1_MSR_DELTA_DSR
  UART1_MODEM_STAT_LO2HI_RI = UART1_MSR_LO2HI_RI
  UART1_MODEM_STAT_DELTA_DCD = UART1_MSR_DELTA_DCD
  UART1_MODEM_STAT_CTS = UART1_MSR_CTS
  UART1_MODEM_STAT_DSR = UART1_MSR_DSR
  UART1_MODEM_STAT_RI = UART1_MSR_RI
  UART1_MODEM_STAT_DCD = UART1_MSR_DCD

class UART_PARITY_Type:
  '''UART Parity type definitions.
  
  UART_PARITY_NONE: No parity
  UART_PARITY_ODD:  Odd parity
  UART_PARITY_EVEN: Even parity
  UART_PARITY_SP_1: Forced "1" stick parity
  UART_PARITY_SP_0: Forced "0" stick parity
    
  '''
  UART_PARITY_NONE = 0
  UART_PARITY_ODD = 1
  UART_PARITY_EVEN = 2
  UART_PARITY_SP_1 = 3
  UART_PARITY_SP_0 = 4

def UART_RS485SendSlvAddr(UARTx, SlvAddr):
  '''Send Slave address frames on RS485 bus.
  
  UARTx:  LPC_UART1 (only)
  SlvAddr:  Slave Address.

  '''
  return robocaller("UART_RS485SendSlvAddr", "void", UARTx, SlvAddr)

def UART_ABClearIntPending(UARTx, ABIntType):
  '''Clear Autobaud Interrupt Pending.
  
  UARTx:  UART peripheral selected, should be
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  ABIntType:  type of auto-baud interrupt, should be:
              - UART_AUTOBAUD_INTSTAT_ABEO: End of Auto-baud interrupt
              - UART_AUTOBAUD_INTSTAT_ABTO: Auto-baud time out interrupt
  
  '''
  return robocaller("UART_ABClearIntPending", "void", UARTx, ABIntType)

def UART_IrDAPulseDivConfig(UARTx, PulseDiv):
  '''Configure Pulse divider for IrDA function on UART peripheral.
  
  UARTx: UART peripheral selected, should be LPC_UART3 (only)
  PulseDiv: Pulse Divider value from Peripheral clock, should be one of the
            following:
            - UART_IrDA_PULSEDIV2   : Pulse width = 2 * Tpclk
            - UART_IrDA_PULSEDIV4   : Pulse width = 4 * Tpclk
            - UART_IrDA_PULSEDIV8   : Pulse width = 8 * Tpclk
            - UART_IrDA_PULSEDIV16   : Pulse width = 16 * Tpclk
            - UART_IrDA_PULSEDIV32   : Pulse width = 32 * Tpclk
            - UART_IrDA_PULSEDIV64   : Pulse width = 64 * Tpclk
            - UART_IrDA_PULSEDIV128 : Pulse width = 128 * Tpclk
            - UART_IrDA_PULSEDIV256 : Pulse width = 256 * Tpclk
            
  '''
  return robocaller("UART_IrDAPulseDivConfig", "void", UARTx, PulseDiv)

def UART_RS485Config(UARTx, RS485ConfigStruct):
  '''Configure UART peripheral in RS485 mode according to the specified 
  parameters in the RS485ConfigStruct.
  
  UARTx:  LPC_UART1 (only)
  RS485ConfigStruct:  Pointer to a UART1_RS485_CTRLCFG_Type structure that 
                      contains the configuration information for specified UART
                      in RS485 mode.
  
  '''
  return robocaller("UART_RS485Config", "void", UARTx, RS485ConfigStruct)

def UART_Receive(UARTx, rxbuf, buflen, flag):
  '''Receive a block of data via UART peripheral.
  
  UARTx:  Selected UART peripheral used to send data,
          should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  rxbuf:  Pointer to Received buffer
  buflen: Length of Received buffer
  flag: Flag mode, should be NONE_BLOCKING or BLOCKING
  return: Number of bytes received
  
  '''
  return robocaller("UART_Receive", "uint32_t", UARTx, rxbuf, buflen, flag)

def UART_ReceiveByte(UARTx):
  '''Receive a single data from UART peripheral.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  return: Data received
  
  '''
  return robocaller("UART_ReceiveByte", "uint8_t", UARTx)

def UART_GetIntId(UARTx):
  '''Get Interrupt Identification value.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  return: Current value of UART UIIR register in UART peripheral.
  
  '''
  return robocaller("UART_GetIntId", "uint32_t", UARTx)

def UART_ForceBreak(UARTx):
  '''Force BREAK character on UART line, output pin UARTx TXD is forced to logic
  0.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral

  '''
  return robocaller("UART_ForceBreak", "void", UARTx)

def UART_FIFOConfig(UARTx, FIFOCfg):
  '''Configure FIFO function on selected UART peripheral.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  FIFOCfg:  Pointer to a UART_FIFO_CFG_Type Structure that contains specified
            information about FIFO configuration
  
  '''
  return robocaller("UART_FIFOConfig", "void", UARTx, FIFOCfg)

def UART_DeInit(UARTx):
  '''De-initializes the UARTx peripheral registers to their default reset 
  values.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  
  '''
  return robocaller("UART_DeInit", "void", UARTx)

def UART_Send(UARTx, txbuf, buflen, flag):
  '''Send a block of data via UART peripheral.
  
  UARTx:  Selected UART peripheral used to send data, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  txbuf:  Pointer to Transmit buffer
  buflen:  Length of Transmit buffer
  flag: Flag used in  UART transfer, should be NONE_BLOCKING or BLOCKING
  return: Number of bytes sent.
  
  '''
  return robocaller("UART_Send", "uint32_t", UARTx, txbuf, buflen, flag)

def UART_FIFOConfigStructInit(UART_FIFOInitStruct):
  '''Fills each UART_FIFOInitStruct member with its default value.
  
  - FIFO_DMAMode = DISABLE
  - FIFO_Level = UART_FIFO_TRGLEV0
  - FIFO_ResetRxBuf = ENABLE
  - FIFO_ResetTxBuf = ENABLE
  - FIFO_State = ENABLE 
  
  UART_FIFOInitStruct:  Pointer to a UART_FIFO_CFG_Type structure which will be
                        initialized.
                        
  '''
  return robocaller("UART_FIFOConfigStructInit", "void", UART_FIFOInitStruct)

def UART_FullModemForcePinState(UARTx, Pin, NewState):
  '''Force pin DTR/RTS corresponding to given state (Full modem mode).
  
  UARTx: LPC_UART1 (only)
  Pin:  Pin that NewState will be applied to, should be:
        - UART1_MODEM_PIN_DTR: DTR pin.
        - UART1_MODEM_PIN_RTS: RTS pin.
  NewState: New State of DTR/RTS pin, should be:
            - INACTIVE: Force the pin to inactive signal.
            - ACTIVE: Force the pin to active signal.

  '''
  return robocaller("UART_FullModemForcePinState", "void", UARTx, Pin, NewState)

def UART_RS485ReceiverCmd(UARTx, NewState):
  '''Enable/Disable receiver in RS485 module in UART1.
  
  UARTx:  LPC_UART1 (only)
  NewState: New State of command, should be:
            - ENABLE: Enable this function.
            - DISABLE: Disable this function.
            
  '''
  return robocaller("UART_RS485ReceiverCmd", "void", UARTx, NewState)

def UART_CheckBusy(UARTx):
  '''Check whether UART is busy or not.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  return: RESET if UART is not busy, otherwise return SET.
  
  '''
  return robocaller("UART_CheckBusy", "FlagStatus", UARTx)

def UART_SendByte(UARTx, Data):
  '''Transmit a single data through UART peripheral.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  Data: Data to transmit (must be 8-bit long)
  
  '''
  return robocaller("UART_SendByte", "void", UARTx, Data)

def UART_ABCmd(UARTx, ABConfigStruct, NewState):
  '''Start/Stop Auto Baudrate activity.
  
  Auto-baudrate mode enable bit will be cleared once this mode completed.
 
  UARTx:  UART peripheral selected, should be
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  ABConfigStruct: A pointer to UART_AB_CFG_Type structure that contains 
                  specified information about UART auto baudrate configuration
  NewState: New State of Auto baudrate activity, should be:
            - ENABLE: Start this activity
            - DISABLE: Stop this activity
  
  '''
  return robocaller("UART_ABCmd", "void", UARTx, ABConfigStruct, NewState)

def UART_GetLineStatus(UARTx):
  '''Get current value of Line Status register in UART peripheral.
  
  The return value of this function must be ANDed with each member in 
  UART_LS_Type enumeration to determine current flag status corresponding to 
  each Line status type. Because some flags in Line Status register will be 
  cleared after reading, the next reading Line Status register could not be 
  correct. So this function used to read Line status register in one time only,
  then the return value used to check all flags.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  return: Current value of Line Status register in UART peripheral
  
  '''
  return robocaller("UART_GetLineStatus", "uint8_t", UARTx)

def UART_FullModemConfigMode(UARTx, Mode, NewState):
  '''Configure Full Modem mode for UART peripheral.
  
  UARTx  LPC_UART1 (only)
  Mode: Full Modem mode, should be:
        - UART1_MODEM_MODE_LOOPBACK: Loop back mode.
        - UART1_MODEM_MODE_AUTO_RTS: Auto-RTS mode.
        - UART1_MODEM_MODE_AUTO_CTS: Auto-CTS mode.
  NewState: New State of this mode, should be:
            - ENABLE: Enable this mode.
            - DISABLE: Disable this mode.
  
  '''
  return robocaller("UART_FullModemConfigMode", "void", UARTx, Mode, NewState)

def UART_FullModemGetStatus(UARTx):
  '''Get current status of modem status register.
  
  UARTx:  LPC_UART1 (only)
  return: Current value of modem status register
  
  '''
  return robocaller("UART_FullModemGetStatus", "uint8_t", UARTx)

def UART_Init(UARTx, UART_ConfigStruct):
  '''Initializes the UARTx peripheral according to the specified parameters in 
  the UART_ConfigStruct.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  UART_ConfigStruct:  Pointer to a UART_CFG_Type structure that contains the 
                      configuration information for the specified UART 
                      peripheral.
                      
  '''
  return robocaller("UART_Init", "void", UARTx, UART_ConfigStruct)

def UART_IrDACmd(UARTx, NewState):
  '''Enable or disable IrDA function on UART peripheral.
  
  UARTx:  UART peripheral selected, should be LPC_UART3 (only)
  NewState: New state of IrDA function, should be:
            - ENABLE: Enable this function.
            - DISABLE: Disable this function.

  '''
  return robocaller("UART_IrDACmd", "void", UARTx, NewState)

def UART_TxCmd(UARTx, NewState):
  '''Enable/Disable transmission on UART TxD pin.
  
  UARTx:  UART peripheral selected, should be:
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  NewState: New State of Tx transmission function, should be:
            - ENABLE: Enable this function
            - DISABLE: Disable this function.

  '''
  return robocaller("UART_TxCmd", "void", UARTx, NewState)

def UART_ConfigStructInit(UART_InitStruct):
  '''Fills each UART_InitStruct member with its default value.
  
  - 9600 bps
  - 8-bit data
  - 1 Stopbit
  - None Parity
  
  UART_InitStruct: Pointer to a UART_CFG_Type structure which will be
  initialized.
  
  '''
  return robocaller("UART_ConfigStructInit", "void", UART_InitStruct)

def UART_IntConfig(UARTx, UARTIntCfg, NewState):
  '''Enable or disable specified UART interrupt.
  
  UARTx:  UART peripheral selected, should be
          - LPC_UART0: UART0 peripheral
          - LPC_UART1: UART1 peripheral
          - LPC_UART2: UART2 peripheral
          - LPC_UART3: UART3 peripheral
  UARTIntCfg: Specifies the interrupt flag, should be one of the following:
              - UART_INTCFG_RBR:  RBR Interrupt enable
              - UART_INTCFG_THRE:  THR Interrupt enable
              - UART_INTCFG_RLS:  RX line status interrupt enable
              - UART1_INTCFG_MS:  Modem status interrupt enable (UART1 only)
              - UART1_INTCFG_CTS:  CTS1 signal transition interrupt enable (UART1 only)
              - UART_INTCFG_ABEO:  Enables the end of auto-baud interrupt
              - UART_INTCFG_ABTO:  Enables the auto-baud time-out interrupt
  NewState: New state of specified UART interrupt type, should be:
            - ENABLE: Enable this UART interrupt type.
            - DISABLE: Disable this UART interrupt type.

  '''
  return robocaller("UART_IntConfig", "void", UARTx, UARTIntCfg, NewState)

def UART_IrDAInvtInputCmd(UARTx, NewState):
  '''Enable or disable inverting serial input function of IrDA on UART
  peripheral.
  
  UARTx:  UART peripheral selected, should be LPC_UART3 (only)
  NewState: New state of inverting serial input, should be:
            - ENABLE: Enable this function.
            - DISABLE: Disable this function.
  
  '''
  return robocaller("UART_IrDAInvtInputCmd", "void", UARTx, NewState)

def UART_RS485SendData(UARTx, pData, size):
  '''Send Data frames on RS485 bus.
  
  UARTx:  LPC_UART1 (only)
  pData:  Pointer to data to be sent.
  size: Size of data frame to be sent.
  return: 
  
  '''
  return robocaller("UART_RS485SendData", "uint32_t", UARTx, pData, size)

