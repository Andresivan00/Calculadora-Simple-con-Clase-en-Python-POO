'''
# ============================================
# DEFINITION OF A "Calculator" CLASS
# ============================================
'''
class Calculator:  
  '''
   Class constructor method
   Executes automatically when creating a Calculator object
  '''
  def __init__(self, a, b):
    '''
     Saves the received values as internal variables (object attributes)
     Uses underscore to indicate they are "private" (Python convention)
    '''
    self._a = a  
    self._b = b
        
  # Method to add the two numbers
  def add(self):
    r = self._a + self._b  # Adds attributes a and b
    return r  # Returns the result
    
  # Method to subtract the two numbers
  def subtract(self):
    r = self._a - self._b  # Subtracts a - b
    return r  # Returns the result

  # Method to multiply the two numbers
  def multiply(self):
    r = self._a * self._b  # Multiplies a and b
    return r  # Returns the result
    
  # Method to divide the two numbers
  def divide(self):
    r = self._a / self._b  # Divides a by b
    return r  # Returns the result
    
'''
 ============================================
 CREATION OF A Calculator CLASS OBJECT
 ============================================
'''
# Here a "instance" of Calculator is created with values 5 and 8
op = Calculator(5, 8)

'''
 ============================================
 USING THE CLASS METHODS
 ============================================
'''
# Calls the functions defined in the class and displays the results
print("The sum is:", op.add())              # Calls the add() method
print("The subtraction is:", op.subtract()) # Calls the subtract() method
print("The multiplication is:", op.multiply())  # Calls the multiply() method
print("The division is:", op.divide())       # Calls the divide() method
