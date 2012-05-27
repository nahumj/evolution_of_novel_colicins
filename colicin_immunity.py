"""
*a colicin is represented by a single number
*immunity is represented by another number 
*colicin binding to immunity is represented by the abs-difference being less than 
a threshold
"""
import random

class Colicin(object):
	def __init__(self, id):
		self.id = id
		
	def __repr__(self):
		return 'Colicin({})'.format(self.id)
	
	def duplicate(self):
		duplicate =  Colicin(self.id)
		return duplicate
		
	def mutate(self):
		diff = 0
		while diff == 0:
			diff = random.randint(-2, 2)
		self.id += diff
		
class Immunity(object):
	def __init__(self, id, binding_range):
		self.id = id
		self.binding_range = binding_range
		
	def __repr__(self):
		return 'Immunity({}, {})'.format(self.id, self.binding_range)
		
	#0 or immunity objects- pass a colicin (ask can you bind!)
	
	def can_bind(self, colicin):
		dif = colicin.id - self.id
		abs_dif = abs(dif)
		return abs_dif < self.binding_range
		
	def duplicate(self):
		duplicate =  Immunity(self.id, self.binding_range)
		return duplicate
		
	#write mutate and test for Immunity