			
def get_inventory():
	# returns numbers "id" a, b, and c
	return num_items(Items.Hay), num_items(Items.Wood), num_items(Items.Carrot)
	
def water(): # waters if I have water and tile isn't watered
	if get_water() == 0 and num_items(Items.Water) > 1:
		use_item(Items.Water) 

def fertilize():
	use_item(Items.Fertilizer)
	
def cycle():
	if get_pos_x() == get_world_size() - 1:
		move(North)
	move(East)
	return get_pos_x() == 0 and get_pos_y() == 0
	
def rcycle():
	if get_pos_x() == get_world_size() - 22:
		move(South)
	move(West)
	
def get_pos():
	x = get_pos_x()
	y = get_pos_y()
	return x, y

def move_to_pos(x,y):
	cur_x = get_pos_x()
	cur_y = get_pos_y()
	
	while x > cur_x:
		move(East)
		cur_x = get_pos_x()
	while x < cur_x:
		move(West)
		cur_x = get_pos_x()
	while y > cur_y:
		move(North)
		cur_y = get_pos_y()
	while y < cur_y:
		move(South)
		cur_y = get_pos_y()
		
	new_x = get_pos_x()
	new_y = get_pos_y()
	
	return new_x, new_y