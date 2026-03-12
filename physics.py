from vpython import *
import constants
import state
		
def law_of_universal_gravitation(object_one, object_two):
    G = constants.gravitacional_constant
    r_vector = object_two.pos - object_one.pos
    distance = mag(r_vector)
    if distance == 0: 
        return vec(0,0,0)
    force_magnitude = G * (object_one.mass * object_two.mass) / (distance**2)
    gravitational_force = force_magnitude * hat(r_vector)
    
    return gravitational_force
   
def update_velocity(obj, force, dt):
    acceleration = vec(0,0,0)
    acceleration = force/obj.mass

    obj.velocity += acceleration * dt

def update_position(obj, dt):
    obj.pos += obj.velocity * dt

def update_vectors_axis(obj, gravitacional_pull):

    obj.velocity_vector.axis = obj.velocity * state.vector_scaling_velocity
    obj.acceleration_vector.axis = gravitacional_pull/obj.mass * state.vector_scaling_force

def update_vectors_pos(obj):
    obj.velocity_vector.pos = obj.pos
    obj.acceleration_vector.pos = obj.pos

def calculate_kinetic_energy(objects):
    kinetic_energy = 0
    for obj in objects:
        obj_kinetic_energy = obj.mass * mag2(obj.velocity) * 1/2
        kinetic_energy += obj_kinetic_energy
    return kinetic_energy

def calculate_potential_energy(objects):
    potential_energy = 0
    calculated_obj = []
    for object_one in objects:
        for object_two in objects:
            if object_two not in calculated_obj and object_two is not object_one and "ring" not in object_two.name:
                couple_potential_energy = - (constants.gravitacional_constant * object_one.mass * object_two.mass / mag(object_two.pos - object_one.pos))
                potential_energy += couple_potential_energy
        calculated_obj.append(object_one)
    return potential_energy

