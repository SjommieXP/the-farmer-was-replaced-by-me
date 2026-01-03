from farm import *

clear()

while True:
	hay, wood, carrot = get_inventory()
	
	while carrot > 4:
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
				break
	# carrots - while hay and wood are above 2
	while (hay > 2 and wood > 2):
		if get_ground_type() != Grounds.Soil:
			till()			
		harvest()
		plant(Entities.Carrot)
		cycle()
		hay, wood, carrot = get_inventory()
	
	# hay untill there is 144 in storage, if it was under 
	while (hay < 144):
		if get_ground_type() != Grounds.Grassland:
			till()			
		harvest()
		cycle()
		hay = num_items(Items.Hay)
		
	# wood - | | -
	while (wood < 144):
		if get_ground_type() != Grounds.Grassland:
			till()			
		plant(Entities.Bush)
		harvest()
		cycle()
		wood = num_items(Items.wood)