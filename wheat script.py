from farm import *
clear()
while True:
	harvest()
	if get_ground_type() == Grounds.Soil:
		till()
	cycle()

#Hello 
#How are you today?
#I'm good, how are you?
