import timingDecorator

@profile
def isMultipleOfThreeOrFive(n):
	return n % 3 == 0 or n % 5 == 0

@profile
def ex1():
	print sum([n for n in range(1,1000) if isMultipleOfThreeOrFive(n)])

ex1()
