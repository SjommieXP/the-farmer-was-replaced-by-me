from farm import *
from maze import *
clear()
set_world_size(12)
while True:
	# move to origin
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
	
	# Plant maze
	while True:
		plant(Entities.Bush)
		cycle()
		
		if get_pos_x() == 0 and get_pos_y() == 0:
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_substance, substance)
			break

	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
		
		if can_left():
			turn_left()
			forward()
			continue
			
		if can_forward():
			forward()
			continue
			
		if can_right():
			turn_right()
			forward()	
			continue 
			
		if can_back():
			turn_right()
			turn_right()
			forward()
			continue
		
		
	
					
					