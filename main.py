#Finished on 24 February 2026 02:17:57, Started on 18 January 2026 11:58:21


from vpython import *
import objects
import physics
import input_handler
import images
import state


dt = 0.01
simulation_state = state.simulation_state
restart_state_dict = state.restart_state_dict

energy_graph = graph(title="Energy / Time", 
					xtitle="Time (s)", 
					ytitle="Energy (J)", 
					width=500, height=300,
					align = "left")

curve_kinetic = gcurve(graph=energy_graph, color=color.blue, label="Kinetic")
curve_potential = gcurve(graph=energy_graph, color=color.red, label="Potential")
curve_total = gcurve(graph=energy_graph, color=color.black, label="Total")


def empty_function():
	return

def check_for_inputs(grid):

	scene_focus_index = state.scene_focus_index
	trails_active = state.trails_active
	vectors_active = state.vectors_active
	grid_active = state.grid_active
	dt = state.dt

	object_array = list(objects.object_dict.values())
	res_up = input_handler.key_handler("up", lambda: input_handler.add_scene_focus_index(scene_focus_index))
	res_down = input_handler.key_handler("down", lambda: input_handler.subtract_scene_focus_index(scene_focus_index))
	res_left = input_handler.key_handler("left", lambda: input_handler.subtract_delta_t(dt))
	res_right = input_handler.key_handler("right", lambda: input_handler.add_delta_t(dt))
	res_t = input_handler.key_handler("t", lambda: input_handler.toggle_trail(object_array, trails_active))
	res_v = input_handler.key_handler("v", lambda: input_handler.toggle_vectors(object_array, vectors_active))
	res_g = input_handler.key_handler("g", lambda: input_handler.toggle_grid(grid, grid_active))
	
	if res_t is not None:
		state.trails_active = res_t

	if res_v is not None:
		state.vectors_active = res_v

	if res_g is not None:
		state.grid_active = res_g

	if res_up is not None:
		scene_focus_index = res_up
	if res_down is not None:
		scene_focus_index = res_down
	
	state.scene_focus_index = scene_focus_index % (len(object_array) + 1)

	if res_left is not None:
		state.dt = res_left
	if res_right is not None:
		state.dt = res_right

	input_handler.update_input_state()

def update_UI():
	delta_t_label.text = f"Delta T: {state.dt:.4f}\n"
	scene_focus_index = state.scene_focus_index
	object_array = list(objects.object_dict.values())

	if scene_focus_index == 0:
		focus_label.text = "Focus: Origin\n"
		mass_label.text = ""
		radius_label.text = ""
		pos_label.text = ""
		velocity_label.text = ""
		return vec(0,0,0)

	elif 0 <= scene_focus_index - 1 < len(object_array):
		obj = object_array[scene_focus_index - 1]
		focus_label.text = f"Focus: {obj.name}\n"
		mass_label.text = f"Mass: {obj.mass:g} Kg\n"
		radius_label.text = f"Radius: {obj.radius} km\n"
		pos_label.text = f"Position: {obj.pos} km\n"
		velocity_label.text = f"Speed: {mag(obj.velocity):.2f} km/s\n"
		return obj.pos
	
	return vec(0,0,0)

scene.title = "Solar System Simulator"
scene.append_to_caption("<b>Settings</b>\n")

start_button = button(text="Start", bind= lambda: input_handler.start_simulation(start_button, pause_button, preset_dropdown, create_new_planet_UI))
pause_button = button(text="Reset", bind= lambda: input_handler.pause_simulation(start_button, pause_button, preset_dropdown, objects.object_dict, restart_state_dict,  curve_potential, curve_kinetic, curve_total, create_new_planet_UI))
wtext(text = "\nPresets: ")
presets_names = ["Solar System(Scale)", "Solar System(Reduced)","Saturn", "3 Body Problem", "Empty"]
preset_dropdown = menu(choices = presets_names, bind = input_handler.change_preset)
wtext(text = "\n")

wtext(text = "\n")
delta_t_label = wtext(text=f"Delta T: {dt}\n")
wtext(text = "<b>Object Information</b>\n")
focus_label = wtext(text="Focus: Origin\n")
mass_label = wtext(text="")
radius_label = wtext(text="")
pos_label = wtext(text="")
velocity_label = wtext(text="")

create_new_planet_UI = []

t1 = wtext(text = "\n<b>Object Creation</b>")
create_new_planet_UI.append(t1)

t2 = wtext(text="\nName:   ")
input_name = winput(text = "Earth", bind = empty_function)
create_new_planet_UI.extend([t2, input_name])

t3 = wtext(text="\nMass:   ")
input_mass = winput(text='1e9', type = "string", bind = empty_function)
create_new_planet_UI.extend([t3, input_mass])

t4 = wtext(text="\nRadius: ")
input_radius = winput(text = "0.8", prompt='Radius:', bind=empty_function, type='numeric')
create_new_planet_UI.extend([t4, input_radius])

t5 = wtext(text="\nPosition:\n")
input_pos_x = winput(text = "50", prompt='x:', bind=empty_function, type='numeric')
input_pos_y = winput(text = "0", prompt='y:', bind=empty_function, type='numeric')
input_pos_z = winput(text = "0", prompt='z:', bind=empty_function, type='numeric')
create_new_planet_UI.extend([t5, input_pos_x, input_pos_y, input_pos_z])

t6 = wtext(text="\nVelocity:\n")
input_velocity_x = winput(text = "0", prompt='x:', bind=empty_function, type='numeric')
input_velocity_y = winput(text = "0", prompt='y', bind=empty_function, type='numeric')
input_velocity_z = winput(text = "1.155", prompt='z', bind=empty_function, type='numeric')
create_new_planet_UI.extend([t6, input_velocity_x, input_velocity_y, input_velocity_z])

t7 = wtext(text="\nColor:   ")
input_color = winput(text = "(R,G,B)", prompt='Color', bind=empty_function, type='string')
create_new_planet_UI.extend([t7, input_color])

t8 = wtext(text="\nTexture (Optional): ")
input_texture = winput(text = "None", prompt='Texture', bind=empty_function)
create_new_planet_UI.extend([t8, input_texture])
input_emmisive = checkbox(text = "Emmisive", bind= empty_function)

create_new_planet_UI.append(wtext(text="\n"))

btn_create = button(text="Create Planet", bind= lambda: input_handler.create_new_planet_button(input_name.text, input_emmisive.checked, input_mass.text, input_radius.text, input_pos_x.text, input_pos_y.text, input_pos_z.text, input_velocity_x.text, input_velocity_y.text, input_velocity_z.text, input_color.text))
create_new_planet_UI.append(btn_create)

wtext(text = "\n<b>System Energy</b>")

scene.background = color.black
scene.texture = images.background_image
scene.autoscale = False
scene.align = "left"
scene_focus = vec(0,0,0)

state.t = 0
grid = objects.draw_grid(1000,10, 0.05)
try:
	while True:
		rate(200)
		check_for_inputs(grid)
		dt = state.dt 
		vectors_active = state.vectors_active
		if state.simulation_state:
			object_dict_values = list(objects.object_dict.values())
			calculations_made = 0
			for object_one in object_dict_values:
				gravitacional_pull = vec(0,0,0)
				for object_two in object_dict_values:
					if object_one != object_two and "ring" not in object_two.name:
						gravitacional_pull += physics.law_of_universal_gravitation(object_one, object_two)
						calculations_made += 1
				physics.update_velocity(object_one, gravitacional_pull, dt)
				if vectors_active and "ring" not in object_one.name:
					physics.update_vectors_axis(object_one, gravitacional_pull)
			print(calculations_made)
	
			for object_one in object_dict_values:
				physics.update_position(object_one, dt)
				if vectors_active:
					physics.update_vectors_pos(object_one)

			state.t += dt
			e_kin = physics.calculate_kinetic_energy(object_dict_values)
			e_pot = physics.calculate_potential_energy(object_dict_values)
			e_total = e_kin + e_pot
			curve_kinetic.plot(state.t, e_kin)
			curve_potential.plot(state.t, e_pot)
			curve_total.plot(state.t, e_total)
		scene.center = update_UI()
except Exception as e:
    print("\n" + "="*30)
    print("ERRO DETETADO NO SIMULADOR:")
    print(e)
    import traceback
    traceback.print_exc() # Mostra a linha exata do erro
    print("="*30)
    input("\nO programa crashou. Prime ENTER no terminal para fechar...")