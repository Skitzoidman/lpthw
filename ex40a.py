import mystuff
mystuff.apple()
MyStuff = {'apple': "I AM APPLES"}

#mystuff = {'apple': "I AM APPLES!"}
#print(mystuff['apple'])

print(mystuff.tangerine)

#mystuff['apple']
mystuff.apple()
mystuff.tangerine

class MyStuff(object):
	def __init__(self):
		self.tangerine = "And now a thousand years between"
	
	def apple(self):
		print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
#print(thing.tangerine)

