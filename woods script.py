from farm import *


#clear()

while True:
	
	if can_harvest():
		harvest()

	if (get_pos_x() % 2 == 0 and get_pos_y() % 2 == 1) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 0):
		plant(Entities.Tree)
		water()
		cycle()
	else:
		plant(Entities.Bush)
		cycle()