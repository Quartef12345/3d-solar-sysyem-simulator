from vpython import *
import state
import objects
import presets

last_keys = []

def key_handler(condition_key, function):
	global last_keys
	keys = keysdown()
	if condition_key in keys and condition_key not in last_keys:
		return function()
	return None

def update_input_state():
    global last_keys
    last_keys = keysdown()

def add_scene_focus_index(current_scene_focus_index):
	new_scene_focus_index = current_scene_focus_index + 1
	return new_scene_focus_index

def subtract_scene_focus_index(current_scene_focus_index):
	new_scene_focus_index = current_scene_focus_index - 1
	return new_scene_focus_index

def add_delta_t(delta_t):
	new_delta_t = delta_t + 0.01
	return new_delta_t

def subtract_delta_t(delta_t):
	new_dt = delta_t - 0.01
	return max(0.001, new_dt)

def toggle_trail(object_array, current_state):
	new_state = not current_state
	for obj in object_array:
		obj.make_trail = new_state
		if new_state == False:
			obj.clear_trail()
	return new_state

def toggle_vectors(object_array, current_state):
    new_state = not current_state
    for obj in object_array:
        obj.velocity_vector.visible = new_state
        obj.acceleration_vector.visible = new_state
    return new_state

def toggle_grid(object_array, current_state):
    new_state = not current_state
    for obj in object_array:
        obj.visible = current_state
    return new_state

def disable_UI(elements_array, is_disabled):
	for element in elements_array:
		element.disabled = is_disabled

def start_simulation(start_button, pause_button, preset_dropdown, UI_array):
	restart_state_dict = state.restart_state_dict

	object_dict = objects.object_dict
	pause_button.text = "Pause"
	for key in object_dict.keys():
		velocity_key_name = key + "_velocity"
		position_key_name = key + "_position"

		restart_state_dict[position_key_name] = vec(object_dict[key].pos)
		restart_state_dict[velocity_key_name] = vec(object_dict[key].velocity)
	
	state.simulation_state = True
	start_button.disabled = True
	preset_dropdown.disabled = True

	disable_UI(UI_array, True)

	return True

def pause_simulation(start_button, pause_button, preset_dropdown, object_dict, restart_state_dict, curve_potential, curve_kinetic, curve_total, UI_array):

	start_button.disabled = False
	preset_dropdown.disabled = False
	if state.simulation_state:
		state.simulation_state = not state.simulation_state
		pause_button.text = "Reset"
	else:
		curve_total.delete()
		curve_kinetic.delete()
		curve_potential.delete()
		for key in object_dict.keys():
			object_dict[key].clear_trail()
		state.t = 0
		for key in object_dict.keys():
			velocity_key_name = key + "_velocity"
			position_key_name = key + "_position"

			object_dict[key].velocity = restart_state_dict[velocity_key_name]
			object_dict[key].pos = restart_state_dict[position_key_name]
			pause_button.text = "Pause"

		disable_UI(UI_array, False)

def create_new_planet_button(name, emmisive,mass, radius, px, py, pz, vx, vy, vz, color, texture= "None"):
	try:
		radius = float(radius)
		px = float(px)
		py = float(py)
		pz = float(pz)
		vx = float(vx)
		vy = float(vy)
		vz = float(vz)
		mass = float(mass)
	except Exception as e:
		print(e)
		return
	position_vector = vec(px,py,pz)
	velocity_vector = vec(vx, vy, vz)

	color = color.replace("(", "").replace(")", "")

	color_array = color.split(",")	
	try:
		color_x = int(color_array[0])/255
		color_y = int(color_array[1])/255
		color_z = int(color_array[2])/255
	except Exception as e:
		print(e)
		return
	if color_x >= 0 and color_y >= 0 and color_z >= 0:
		color_vector = vec(color_x, color_y, color_z)
	else:
		return
	objects.create_new_planet(position_vector, radius, color_vector, emmisive, mass, velocity_vector, name, objects.object_dict, None)


def change_preset(evt):
	objects.disable_all_objects(objects.object_dict)
	
	presets.load_preset(evt.selected)
