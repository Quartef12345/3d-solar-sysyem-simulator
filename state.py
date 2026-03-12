from vpython import *

simulation_state = False
restart_state_dict = {}
t = 0
dt = 0.01
vector_scaling_velocity = 2
vector_scaling_force = 500
vector_shaft_width = 0.5
camera_range = 100

scene_focus_index = 0
trails_active = True
vectors_active = True
grid_active = True