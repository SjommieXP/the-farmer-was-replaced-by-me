from farm import *

clear()
while True:
	

	ready = 0
	#cycle and plant
	while get_ground_type() == Grounds.Grassland or get_entity_type() == None:
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Pumpkin)
		cycle()
	
	#stand in the corner and wait for alive pumpkin and grab sample
	while get_pos_x() == 0 and get_pos_y() == 0:
		if get_entity_type() == Entities.Dead_Pumpkin:
			harvest()
			plant(Entities.Pumpkin)
			continue
		if get_entity_type() == Entities.Pumpkin and can_harvest():
			pumpkin_id = measure()
			ready = 1
			cycle()
		break
	
	while ready == 1:
		if get_entity_type() == Entities.Dead_Pumpkin:
			harvest()
			plant(Entities.Pumpkin)
			cycle()
		else:
			cycle()
		
		if get_pos_x() == (get_world_size() -1) and get_pos_y() == (get_world_size() -1):
			sample = measure()
			if sample == pumpkin_id:
				pumpkinssaved = num_items(Items.Pumpkin)
				harvest()
				cycle()
				break
		