"""Demonstrates the use of tone and noTone functions with a simple GUI and
piezo speaker connected to PWM1
"""

from robovero.extras import roboveroConfig
from robovero.arduino import tone, noTone, PWM1
from Tkinter import Tk, Listbox, END

__author__ =      "Neil MacMunn"
__email__ =       "neil@gumstix.com"
__copyright__ =   "Copyright 2010, Gumstix Inc"
__license__ =     "BSD 2-Clause"
__version__ =     "0.1"


def printselection(event):
  global mylist
  selection = int(mylist.curselection()[0])
  if selection == 0:
    noTone(PWM1)
  elif selection < 10:
    tone(PWM1, selection*100, 100)
  else:
    noTone(PWM1)

roboveroConfig()

# draw a listbox
root = Tk()
root.title("Tone Generator")

# populate the list with available frequencies
mylist = Listbox(root)
mylist.insert(END, "OFF")
for freq in range(100, 1000, 100):
   mylist.insert(END, "%d Hz" % freq)
mylist.pack()

# set the callback function for left button clicks
mylist.bind('<ButtonRelease-1>', printselection)

root.mainloop()




