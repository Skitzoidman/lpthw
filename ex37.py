#global
def print_char():
	global a
	def A():
		char = "a"
		return char
	a =  A()
	print(a)
print_char()
print(a)

#del
test = ['a', 'b', 'c']
print(test[0], test[1], test[2])
del test[0]
print(test[0], test[1])

#with as statement
#def b():
#	c = "b"
#	return c
#d = b()
#b = "b"

#with d as b:
#	print("kek")

#assert
assert True

e = {'x' : 1, 'y' : 2}
print(e)

print(e['x'])
#yield
#def test():
#	h = "a"
#	yield h
#	test().next()
#	g = "b"
#	return g

#l = test()
#print(repr(l))

#bytes
x = 12
print(hex(x))

#raise ValueError("No")

#finally
#finally:
#	print("korrekt")

