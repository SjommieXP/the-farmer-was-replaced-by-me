from farm import *
from mymove import *

change_hat(Hats.Traffic_Cone_Stack)
harvest()
clear()
while True:  # main loop 
	if get_entity_type() != Entities.Pumpkin: # if anything else then a pumpkin
		if get_ground_type() == Grounds.Grassland:	# if it's grassland, till to soil
			till() # turns grass to soil and vice versa
		plant(Entities.Pumpkin) 
		
	if get_entity_type() == Entities.Dead_Pumpkin:
		harvest()
		plant(Entities.Pumpkin)
		continue
	else:
		cycle()
		
	harvest()
	