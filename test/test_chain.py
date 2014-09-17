__author__ = "Mats Larsen"
__copyright__ = "SINTEF, NTNU 2013"
__credits__ = ["Morten Lind"]
__license__ = "GPL"
__maintainer__ = "Mats Larsen"
__email__ = "matsla@{ntnu.no}"
__status__ = "Development"
#--------------------------------------------------------------------
#File: test_chain.py
#Module Description
"""
This module test the chain class.
"""
#--------------------------------------------------------------------
#IMPORT
#--------------------------------------------------------------------
import traceback
import numpy as np
from math3d.vector import Vector
from chain import Chain

#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 2 # Information level
#--------------------------------------------------------------------
#METHODS
#--------------------------------------------------------------------
def log(msg, log_level=LOG_LEVEL):
    """
    Print a message, and track, where the log is invoked
    Input:
    -msg: message to be printed, ''
    -log_level: informationlevel, i
    """
    global LOG_LEVEL
    if log_level <= LOG_LEVEL:
        print(str(log_level) + ' : test_chain.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)

log('Testing Chain Class with numbers', 2)
a =  np.array([1,2,3,4])
chain = Chain(name='test Chain',elements = a)
print(chain)
chain.add_front(5)
print(chain)

chain.add_tail(50)
print(chain)

print(chain.data)
print(chain.get_data(2))

log('Testing Chain Class with Vectors', 2)
v =[Vector(1,1,1),Vector(2,2,2),Vector(3,3,3),Vector(4,4,4)]
c = Chain(name='test Chain Vectors',elements = v)
print(c)
c.add_front(Vector(1,2,3))
print(c)

c.add_tail(Vector(5,6,7))
print(c)
c.set_current(0)
print(c.get_data())
print(c.get_data(1))
s = c.get_element(1)
print(s.next)

print(c.get_next(number=1,forward=2))
print(c.get_prev(number=1))
