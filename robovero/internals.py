"""Handles communications with the RoboVero.
"""

import threading, serial, time, atexit

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"

isr_list = {
  16 : 'INT_GPIOA_HANDLER()',
}

def listen():
	"""Listen for responses and unsolicited messages (interrupts).
	"""
	global robovero
	while robovero:
		
		message = ""
		while "\r\n" not in message:
			if not robovero:
				exit()
			try:
				message += robovero.serial.read(1)
			except:
				robovero.debug.write("ERROR: USB connection lost\r\n")
				exit("error: USB connection lost")
					
		if message == "\r\n":
			robovero.debug.write("INTERRUPT: ")
			robovero.serial.timeout = None
			int_num = int(robovero.serial.readline(), 16)
			robovero.debug.write("%d\r\n" % int_num)
			robovero.serial.timeout = 0
			isrthread = threading.Thread(target=isr, args=[int_num], name="isr")
			isrthread.start()
			
		else:
			robovero.response = message

def getReturn():
	"""Get a return value that the listening thread has received.
	"""
	global robovero
	while robovero.response == None:
		time.sleep(0)
	ret = robovero.response
	robovero.response = None
	return ret


def isr(int_num):
	"""When an interrupt occurs, call the ISR then clear and reenable
	the interrupt.
	"""
	global robovero
	print "Interrupt!"
# TODO
#	with robovero.lock:
#		exec(isr_list[int_num])
#		IntPendClear(int_num)
#		IntEnable(int_num)
	
def robocaller(function, ret_type, *args):
	"""Serialize a function and it's arguments and send to device.
	"""
	# TODO: get function indices with getIndex to speed up remote function calls
	global robovero
	with robovero.lock:
		for arg in args:
			function += " %X" % (arg)
		function += "\r\n"
		robovero.debug.write("REQUEST: %s" % function)
		robovero.serial.write(function)
		if ret_type != "void":	
			ret = int(getReturn(), 16)
			robovero.debug.write("RESPONSE: %X\r\n" % ret)
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
			print "ERROR: %s not a member of %s" % (member, 
																								self.__class__.__name__)
		else:
			return ret

	def __setattr__(self, member, value):
		"""Set the value of a struct member.
		"""
		robocaller("%s_%s" % (self.__class__.__name__, member), "void",
								self.__dict__["ptr"], value)
		if getStatus():
			print "ERROR: %s not a member of %s" % (member, 
																								self.__class__.__name__)

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
		self.serial = serial.Serial('/dev/ttyACM0')
		self.serial.timeout = 0
		# send line terminator, disable console echo and prompt
		self.serial.write("\r\n")
		self.serial.write("promptOff\r\n")
		# pause to let characters arrive on the serial port
		time.sleep(0.1)
		self.serial.flushInput()

		#	a lock for handling incoming serial data
		self.lock = threading.RLock()

		self.response = None
		self.debug = open("run.log", "w")
		
	def startListening(self):
		"""Spawn a new thread to listen for incoming messages.
		"""
		self.listener = threading.Thread(target=listen, name="listener")
		self.listener.daemon = True
		self.listener.start()
	
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
