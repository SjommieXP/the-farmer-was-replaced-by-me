# do maze
facing = 0
dirs = [North, East, South, West]
def turn_right():
	global facing 
	facing = (facing + 1) %4
	
def turn_left():
	global facing 
	facing = (facing - 1) %4
	
def forward():
	move(dirs[facing])
	
def can_forward():
	return can_move(dirs[facing])

def can_left():
	return can_move(dirs[(facing - 1) % 4])
	
def can_right():
	return can_move(dirs[(facing + 1) % 4])

def can_back():
	return can_move(dirs[(facing + 2) % 4])
	
def maze_solve():
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
	
def maze_solve2():
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
		
		if can_right():
			turn_right()
			forward()
			continue
		
		if can_forward():
			forward()
			continue
			
		if can_left():
			turn_left()
			forward()	
			continue 
			
		if can_back():
			turn_right()
			turn_right()
			forward()
			continue
	
def maze_summon():
	if get_pos_x() == 0 and get_pos_y() == 0:
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_substance, substance)

				