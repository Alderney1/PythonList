"""
This a try to try to make a list functionality in Python. This class represent a list, and it carries out the basic oeprations of a list.
"""
__author__ = "Mats Larsen"
__copyright__ = "Mats Larsen 2014"
__credits__ = ["Mats Larsen"]
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"

#--------------------------------------------------------------------
#Import
#--------------------------------------------------------------------
from error_display import ErrorDislay as ED # Library to display errors
import traceback
#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 2 # Information level
LOG_ALWAYS = 3 # Always log data
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
        print(str(log_level) + ' : ' + FILE + '.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)
