"""Handles communications with the RoboVero.
"""

import threading, serial, time, atexit, os, sys
import Queue
import windows

__author__ =      ["Neil MacMunn", "Danny Chan"]
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2012, Gumstix Inc."
__license__ =     "BSD 2-Clause"
__version__ =     "0.2"

def listen():
  """Listen for responses and unsolicited messages (interrupts).
  """
  global robovero
  
  while robovero:
    message = robovero.readline("\r\n")
          
    if message == "":
      robovero.debug.write("[%f] INTERRUPT: " % (time.time() - robovero.start_time))
      IRQn = int(robovero.readline("\r\n"), 16)
      robovero.debug.write("%x\r\n" % IRQn)
      isrthread = threading.Thread(target=isr, args=[IRQn], name="isr")
      isrthread.start()
      
    else:
      robovero.response.put(message)

def getReturn():
  """Get a return value that the listening thread has received.
  """
  global robovero
  return robovero.response.get()

isr_list = {}

def isr(IRQn):
  """When an interrupt occurs, call the ISR then clear and reenable
  the interrupt.
  """
  with robovero.lock:
    if IRQn in isr_list:
      isr_list[IRQn]()
    else:
      robovero.debug.write("[%f] INTERRUPT: unhandled!" % (time.time() - robovero.start_time))
      return
    robocaller("NVIC_ClearPendingIRQ", "void", IRQn)
    robocaller("NVIC_EnableIRQ", "void", IRQn)
  
def robocaller(function, ret_type, *args):
  """Serialize a function and it's arguments and send to device.
  """

  global robovero
  with robovero.lock:

    # Check if index is in dictionary, if not, add it to dictionary
    # Debugging log will only contain indices and not the function name
    # Comment out to restore to normal debug log
    
    if function not in robovero.indices:
      search_string = "search " + function + "\r\n"
      robovero.debug.write("[%f] ADD TO DICTIONARY: %s\r\n" % (time.time() - robovero.start_time, function))
      robovero.serial.write(search_string)
      ret = getReturn()
      robovero.debug.write("[%f] INDEX: %s\r\n" % (time.time() - robovero.start_time, ret))
      robovero.indices[function] = ret
    function = robovero.indices[function]

    for arg in args:
      if type(arg) == list:
        for sub_arg in arg:
          function += " %X" % (sub_arg)
      else:
        function += " %X" % (arg)
    function += "\r\n"
    robovero.debug.write("[%f] REQUEST: %s" % (time.time() - robovero.start_time, function))
    robovero.serial.write(function)
    if ret_type != "void":
      ret = getReturn()
      robovero.debug.write("[%f] RESPONSE: %s\r\n" % (time.time() - robovero.start_time, ret))
      if " " in ret:
        ret = [int(x, 16) for x in ret.split()]
      else:
        ret = int(ret, 16)
      return ret
    else:
      return None

########################################################################
# These functions are for internal use and not part of the NXP
# peripheral library
########################################################################

def getIndex(fcn):
  """Get the table index of a function.
  """
  return robocaller("search %s" % (fcn), "int")
    
def getStatus():
  """Get the error status of the previous function call.
  """
  return robocaller("return", "int")
  
def malloc(size):
  """Allocate memory from the heap.
  """
  return robocaller("malloc", "int", size)
  
def free(ptr):
  """Free previously allocated memory.
  """
  return robocaller("free", "void", ptr)

def deref(ptr, size, val=None):
  """Dereference a pointer.
  """
  if val:
    return robocaller("deref", "void", ptr, size, val)
  else:
    return robocaller("deref", "int", ptr, size)

def resetConfig():
  """Simulate a reset condition without losing the usb connection."""
  return robocaller("resetConfig", "void")

class cstruct(object):
  """A parent class for all structs used by the peripheral library.
  """
  def __init__(self, **kwargs):
    """Allocate some memory on the device for the struct.
    """
    ptr = robocaller("%s_malloc" % self.__class__.__name__, "int")
    if ptr == 0:
      self.__del__()
      return
    self.__dict__["ptr"] = ptr
    for key in kwargs:
      self.__setattr__(key, kwargs[key])

  def __getattr__(self, member):
    """Get the value of a struct member.
    """
    ret = robocaller("%s_%s" % (self.__class__.__name__, member), "int",
                      self.__dict__["ptr"])
    if getStatus():
      print "ERROR: %s not a member of %s" % (member, self.__class__.__name__)
    else:
      return ret

  def __setattr__(self, member, value):
    """Set the value of a struct member.
    """
    robocaller("%s_%s" % (self.__class__.__name__, member), "void",
                self.__dict__["ptr"], value)
    if getStatus():
      print "ERROR: %s not a member of %s" % (member, self.__class__.__name__)

  def __del__(self):
    """Free the memory on the robovero when the struct object goes out
    of scope in Python.
    """
    free((self.__dict__["ptr"]))


class Robovero(object):
  """Store information about the USB connection to the device.
  """  
  def __init__(self):
    """Open a serial connection to the robovero hardware.
    """

    # look for RoboVeros in /dev
    if (sys.platform.startswith("linux")):
      devices = [dev for dev in os.listdir("/dev/") if "ttyACM" in dev]
    elif (sys.platform == "darwin"):
      devices = [dev for dev in os.listdir("/dev/") if "tty.usbmodem" in dev]
    elif (sys.platform == "win32"):
      devices = [portname for portname in windows.enumerateSerialPorts()]
    devices.sort()
    num_devs = len(devices)
    idx = 0

    # determine which device to connect to
    if num_devs == 0:
      exit("No RoboVero hardware found.")
    elif num_devs > 1:
      for dev in devices:
        print "%d) %s" % (idx, devices[idx])
        idx += 1
      try:
        idx = int(raw_input("\r\nwhich device? "))
        if idx >= num_devs:
          raise ValueError
      except:
        exit("Invalid selection")

    # try to connect
    try:
      if (sys.platform != "win32"):
        self.serial = serial.Serial('/dev/%s' % devices[idx])
      else:
        self.serial = serial.Serial(windows.fullPortName(devices[idx][1]))
    except:
      exit("Couldn't open device.")

    self.start_time = time.time()
    self.serial.timeout = None
    # send line terminator, disable console echo and prompt
    self.serial.write("\r\n")
    self.serial.write("promptOff\r\n")
    # pause to let characters arrive on the serial port
    time.sleep(0.1)
    self.serial.flushInput()

    #  a lock for handling incoming serial data
    self.lock = threading.RLock()

    self.response = Queue.Queue()
    self.debug = open("run.log", "w")

    self.indices = {} # initialize dictionary

  def startListening(self):
    """Spawn a new thread to listen for incoming messages.
    """
    self.listener = threading.Thread(target=listen, name="listener")
    self.listener.daemon = True
    self.listener.start()
    
  def readline(self, delim):
    """Get one character at a time until the specified delimiter is found.
    """
    message = ""
    while delim not in message:
      if not robovero:
        exit()
      try:
        message += self.serial.read(1)
      except:
        self.debug.write("[%f] ERROR: USB connection lost\r\n"  % (time.time() - self.start_time))
        exit("error: USB connection lost")
    return message.strip(delim)
        
  def __del__(self):
    """Send any remaining data and close the serial connection.
    """
    self.serial.flush()
    self.serial.close()

# These functions get called once when a peripheral driver module is 
# imported. A serial connection to the device is established.
robovero = Robovero()
robovero.startListening()
atexit.register(resetConfig)
