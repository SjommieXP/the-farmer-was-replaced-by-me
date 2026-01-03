from farm import *

#set world size 3x3
set_world_size(3)
clear()
companion = 0 

#move to middle
move(North)
move(East)
	
while True:
	move_to_pos(1,1)
	plant_type, (x, y) = get_companion()
	
		
		
	move_to_pos(x,y)
	if plant_type == Entities.Carrot and get_ground_type() == Grounds.Grassland:
		till()
	plant(plant_type)	
		
		
	while True:
		move_to_pos(1,1)
		if can_harvest() and get_entity_type() == Entities.Grass:
			harvest()
	