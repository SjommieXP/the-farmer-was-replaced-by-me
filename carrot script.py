from farm import *

while True: 
	hay, wood, carrot = get_inventory()
	# carrots - while hay and wood are above 2
	while hay > 64 and wood > 64:
		if get_ground_type() != Grounds.Soil:
			harvest()
			till()			
		harvest()
		hay, wood, carrot = get_inventory()
		plant(Entities.Carrot)
		cycle()
	
	# hay untill there is 144 in storage, if it was under 
	while (hay < get_world_size() **2):
		harvest()
		if get_ground_type() != Grounds.Grassland:
			till()					
		cycle()
		hay = num_items(Items.Hay)
		
	# wood - | | -
	while (wood < get_world_size() **2):
		if get_ground_type() != Grounds.Grassland:
			till()			
		plant(Entities.Bush)
		harvest()
		cycle()
		wood = num_items(Items.wood)