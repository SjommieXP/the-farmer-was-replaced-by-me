from farm import * 

clear()

cact = {}

while True:
	if get_entity_type() != Entities.Cactus:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		spec_cycle(3,3)
	