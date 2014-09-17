__author__ = "Mats Larsen"
__copyright__ = "SINTEF, NTNU 2013"
__credits__ = ["Morten Lind"]
__license__ = "GPL"
__maintainer__ = "Mats Larsen"
__email__ = "matsla@{ntnu.no}"
__status__ = "Development"
#--------------------------------------------------------------------
#File: plane.py
#Module Description
"""
This module represent a chain list and the functionalities for a chain
"""
#--------------------------------------------------------------------
#IMPORT
#--------------------------------------------------------------------
import traceback
import numpy as np
import copy


#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 1 # Information level
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
        print(str(log_level) + ' : chain.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)

class Chain(object):
    """ Class represent a chain."""
    class Error(Exception):
        """Exception class."""
        def __init__(self, message):
            self.message = message
            Exception.__init__(self, self.message)
        def __repr__(self):
            return self.message
    class Element(object):
        """ A Element is in the chain, and contain all the information. """
        def __init__(self,name=None,next_element=None,previous_element=None, data=None):
            if next_element==None or previous_element==None:
                raise self.Error(
                'Could not make a element on arguments : '
                + '"{}"'.format(previous_element))
            self._next = next_element # next element in the chain
            self._prev = previous_element # the prevoius element in the chain
            self._data = data # data of the element
            self._name = 'Element' + str(name)

        def get_name(self):
            """Return the name of the element."""
            return self._name
        name = property(get_name, 'Name Property')

        def get_next(self):
            """ Return the next element. """
            return self._next
        next = property(get_next,'Next Property')
        def set_next(self, element):
            """ Set the next element. """
            self._next = element
        next = property(get_next,set_next, 'Next Property')

        def get_prev(self):
            """ Return the prevoius element. """
            return self._prev

        def set_prev(self, element):
            """ Set the prevoius element. """
            self._prev = element
        prev = property(get_prev,set_prev, 'Prevoius Property')

        def get_data(self):
            """ Return the data from the element. """
            return self._data
        data = property(get_data,'Data Property')
        def set_data(self,data):
            """ Set the data of the element."""
            self._data = data
        data = property(get_data, set_data, 'Data Property')

        def __repr__(self):
            """ print the object. """
            return (
                'Element: "{self.name}", Data: "{self._data}"' ).format(self=self)

    def __init__(self,name='chain', elements=None,data_type=None, log_level=2):
        """ It make a dobelt linked chain from elements.
        Inputs:
        name:string -> name of the object.
        elements: List  [] -> contain all the elements.
        log_level:int -> level of information """
        log('Chain is created with chain', log_level)
        self._name = name # name of the chain
        self._data_type = data_type # type of the elements
        self._log_level = log_level # log level
        if elements == None: # if elements not are given
            self._elements = [] # empty list
        else: # when elements are given
            self._elements = []
            #print(len(elements))
            for i in range(0,len(elements)):
                self.add_tail(element = elements[i])
        if elements != None:
            # set current if elements exist
            self._current = self._elements[0] # set the current to the first element

    def copy(self):
        """Make copy of this instance, plus objects that are associacted with it."""
        new = copy.deepcopy(self)
        return new
    copy = property(copy,'Copy Property')
    
    def get_name(self):
        """ Return name of the chain. """
        return self._name
    name = property(get_name, 'Name Property')

    def get_data_type(self):
        """Return the data type of the elements."""
        return self._data_type

    def set_data_type(self, data_type):
        """Set a new data_type."""
        self._data_type = data_type
    data_type = property(get_data_type, set_data_type, 'Data Type Property')

    def get_length(self):
        """ Return the length of the chain. """
        return int(len(self._elements))
    len = property(get_length, 'Length Property')

    def add_front(self,element):
        """ Add element in the front of the chain. Here it depends if
        the chain is empty or not.
        Inputs:
        element:any type -> the element that has to be insert. """
        log('Performing add front in chain ' +  self._name, self._log_level)
        if self.len == 0:
            # if the chain is empty
            self._elements[0] = self.Element(element,element,element) # first element
            self._elements[0].next = self._elements[0]
            self._elements[0].prev = self._elements[0]
            self._current = self._elements[0] # update current
        else:
            #when chain is not empty
            e = self.Element(self._elements[0],self._elements[self.len-1],element)
            self._elements[0].prev = e
            self._elements[self.len-1].next = e
            self._elements.insert(0,e)

    def add_tail(self,element):
        """ Add element in the back of the chain. Here it depends if
        the chain is empty or not.
        Inputs:
        element:any type -> the element that has to be insert. """
        log('Performing add back in chain ' + self._name, self._log_level)
        if self.len == 0:
            # if the chain is empty
            self._elements.append( self.Element(self.len,element,element,element)) # first element
            self._elements[0].next = self._elements[0]
            self._elements[0].prev = self._elements[0]
            self._current = self._elements[0]
        else:
            # if the chain is not empty
            e = self.Element(self.len,self._elements[0],self._elements[self.len-1],element)
            self._elements[0].prev = e
            self._elements[self.len-1].next = e
            self._elements.append(e)

    def add_chain(self,other):
        """Add another chain to this."""
        for i in range(0,other.len):
            self.add_tail(element=other.get_data(i))

    def get_current(self):
        """ Return the current element. """
        return self._current

    def set_current(self,number):
        """ Set the current element to a element in the chain
        given the the number.
        Inputs:
        number:int -> number of the element in the chain. """
        log('Set current element to number ' + str(number) + 'in the chain.',self._log_level)
        self._current = self._elements[number]
    current = property(get_current,set_current,'Current Property')

    def get_next(self,number=None,forward=None):
        """ Return the next element. If number is not given, then
        the current element is used. forward to loop ahead.
        Input:
        number-> the number in the chain.
        forward -> number of specific number to loop forward """
        if number== None:
            # number is not given, then use current
            element = self._current
        else:
            # element from given number
            element = self._elements[number]

        if forward == None:
            # return next element
            return element.next
        else:
            # return given element from loop
            for i in range(forward):
                element = element.next
        self._current = element # update current
        return element
    next = property(get_next, 'Next Property')

    def get_prev(self, number,backward=None):
        """ Return the prevoius element. If number is not given, then
        the current element is used. forward to loop ahead.
        Input:
        number-> the number in the chain.
        backward -> number of specific number to loop backwards """
        if number== None:
            # number is not given, use current instead
            element = current
        else:
            # use element with a given number
            element = self._elements[number]

        if backward == None:
            # return next element
            return element.prev
        else:
            # return given element from loop
            for i in range(backward):
                element = element.prev
        current = element # update current
        return element
    prev = property(get_prev, 'Prevoius Property')

    def get_tail(self):
        """Return the data in the last element."""
        return self._elements[self.len - 1].data
    tail = property(get_tail,'Tail Property')

    def get_data(self, number=None):
        """ Return the data of the element.
        Input:
        number:int -> the number in the chain. """
        #log('Get data from chain ' + self._name, self._log_level)
        if number== None:
            # number is not given, use current instead.
            return self._current.data
        else:
            # number is given.
            return self._elements[number].data

    def set_data(self,number=None,data=None):
        """Set the data in a element."""
        self._elements[number].set_data(data)
    data = property(get_data, 'Data Property')

    def get_element(self, number=None):
        """ Return the element.
        Input:
        number:int -> the number in the chain. """
        log('Get data from chain ' + self.name, self._log_level)
        if number== None:
            # number is not given, use current instead.
            return self._current
        else:
            # number is given.
            return self._elements[number]
    data = property(get_element, 'Data Property')

    def convert(self,to_type):
        """Make a converting to the to_type in arguments."""
        if to_type == 'array':
            x = np.zeros([])
            for i in range(0,self.len):
                x=np.append(x,self.get_data(i))
        return x


    def get_all_elements(self):
        """Return all elements."""
        return self._elements
    all_elements = property(get_all_elements, 'All Elements Property')

    def delete_elements(self):
        """Delete all elements."""
        self._elements = []
    delete = property(delete_elements, 'Delete Property')

    def to_list(self):
        s= '[ '
        for i in self.all_elements:
            s = s + str(i.data) + ' ,'
        s = s + ' ]'
        return s
    list = property(to_list, 'Property To List')

    def __repr__(self):
        """ Print the chain."""
        return (
            'Chain: "{self._name}" with length "{self.len}" '
            'with elements "{self._elements}"' + ' \n' ).format(self=self)
