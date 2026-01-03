from farm import *

clear()

plants = {}

while True: 
	# 1; get ground type and till if it's not soil
	while get_ground_type() != Grounds.Soil:
		till()
		plant(Entities.Pumpkin)
		cycle()	
	
	# 2; while cycle / while moving:
	while cycle():
		plant_type = get_entity_type() # add entity to plant_type var
		if plant_type not in plants:   # if plant_type not in plants dict, insert it 
			plants[plant_type] = 0     # make the newly added plant_type 0 
		plants[plant_type] += 1        # count the plant_type just added
		
	# 3; if the entity is dead pumpkin, harvest, plant, subtract from dict
	if get_entity_type() == Entities.Dead_Pumpkin:
		harvest() 
		plant(Entities.Pumpkin)
		if Entities.Dead_Pumpkin in plants:
			plants[Entities.Dead_Pumpkin] -= 1
	
	# 4; harvests if the whole field is pumpkin
	if Entities.Pumpkin in plants:
		#if Entities.Pumpkin > 0:
			harvest()
			plants = {} 
	