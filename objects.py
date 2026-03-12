from vpython import *
import state

def draw_grid(xmax, dx, r):
	curve_lines = []
	for x in range(-xmax, xmax, dx):
		curve_x = curve(pos=[vec(x, 0, -xmax), vec(x, 0, xmax)], color=color.white, radius = r)
		curve_y = curve(pos=[vec(-xmax, 0, x), vec(xmax, 0, x)], color=color.white, radius = r)
		curve_lines.append(curve_x)
		curve_lines.append(curve_y)
	return curve_lines


object_dict = {}

for obj in object_dict.values():
	obj.velocity_vector = arrow(pos=obj.pos, axis=obj.velocity * 2, color=color.green, shaftwidth=0.1)
	obj.acceleration_vector = arrow(pos=obj.pos, axis=vec(0,0,0), color=color.red, shaftwidth=0.05)

def disable_all_objects(object_dict):
	for obj in object_dict.values():
		obj.visible = False
		obj.velocity_vector.visible = False
		obj.acceleration_vector.visible = False
		obj.clear_trail()
	object_dict.clear()
	print(object_dict)

def create_new_planet(planet_position, planet_radius, planet_color, emmisive, planet_mass, planet_velocity, planet_name, object_dict, planet_texture):
	base_name = planet_name.lower().replace(" ", "_")

	clean_name = base_name
	counter = 2
	while clean_name in object_dict:
		clean_name = f"{base_name}_{counter}"
		counter += 1

	new_planet = sphere(pos = planet_position, make_trail=True, radius = planet_radius, trail_color = planet_color, emissive = emmisive)
	new_planet.mass = planet_mass
	new_planet.velocity = planet_velocity
	new_planet.name = planet_name

	new_planet.velocity_vector = arrow(pos=new_planet.pos, axis=new_planet.velocity * 2, color=color.green, shaftwidth = state.vector_shaft_width)
	new_planet.acceleration_vector = arrow(pos=new_planet.pos, axis=vec(0,0,0), color=color.red, shaftwidth = state.vector_shaft_width)

	if planet_texture == None:
		new_planet.color = planet_color
	else:
		new_planet.texture = planet_texture

	object_dict[clean_name] = new_planet


