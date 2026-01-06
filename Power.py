from farm import *

clear()
set_world_size(3)

while True:
		
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Sunflower)
	use_item(Items.Water)
	cycle()
	if can_harvest():
		harvest()
