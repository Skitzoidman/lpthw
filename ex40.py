class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
class Math(object):
	
	def __init__(self, content):
		self.content = content
		
	def display_content(self):
		for line in self.content:
			print(line)

	def sum_content(self):
		i = 0
		old_buffer = 0
		list = self.content.copy()
		print(list.__len__())
		if (list.__len__() % 2) != 0:
			while i < ((list.__len__() /2) - 1):
				first_buffer = list.pop()
				second_buffer = list.pop()
				curr_buffer = int(first_buffer) + int(second_buffer)
				buffer = int(old_buffer) + int(curr_buffer)
				old_buffer = buffer
		else:
			while i < (list.__len__() / 2):
				first_buffer = list.pop()
				second_buffer = list.pop()
				curr_buffer = int(first_buffer) + int(second_buffer)
				buffer = int(old_buffer) + int(curr_buffer)
				old_buffer = buffer

		print("Summe: ", old_buffer)
		
numbers = ['0',
		   '1',
		   '2',
		   '3',
		   '4',
		   '5',
		   '6',
		   '7',
		   '8',
		   '9',
		   ]
			
count = Math(numbers)
	
#happy_bday = Song(["Happy birthday to you",
#				   "I don't want to get sued",
#				   "So I'll stop right there"])

#bulls_on_parade = Song(["They rally around tha family",
#						"With pockets full of shells"])

count.display_content()

count.sum_content()

#count.sum_content()
#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()
	



