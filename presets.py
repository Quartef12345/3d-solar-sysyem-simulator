from vpython import *
import objects
import state
import images
import random

presets_dict = {
    "Solar System(Scale)": {
            "configs": {
                "range": 4.5e12, # Escala total até Neptuno
                "dt": 10000,     # Passo de tempo largo para ver movimento em anos
                "vector_scaling_velocity": 1e6,
                "vector_scaling_force": 1e30,
                "vector_shaft_width": 5e8
            },
            "planets": [
                # SOL: Raio ~695,700 km
                {"pos": vec(0,0,0), "radius": 6.957e8, "emissive": True, "mass": 1.98847e30, "velocity": vec(0,0,0), "color": vec(1,1,0.8), "name": "Sun", "texture": images.sun_texture},
            
                # MERCÚRIO: 57.9M km | Raio 2,440 km | Vel 47.36 km/s
                {"pos": vec(5.7909e10, 0, 0), "radius": 2.4397e6, "emissive": False, "mass": 3.3011e23, "velocity": vec(0,0,47360), "color": vec(0.7,0.7,0.7), "name": "Mercury", "texture": images.mercury_texture},
            
                # VÉNUS: 108.2M km | Raio 6,051 km | Vel 35.02 km/s
                {"pos": vec(1.08208e11, 0, 0), "radius": 6.0518e6, "emissive": False, "mass": 4.8675e24, "velocity": vec(0,0,35020), "color": vec(0.9,0.8,0.5), "name": "Venus", "texture": images.venus_texture},
            
                # TERRA: 149.6M km | Raio 6,371 km | Vel 29.78 km/s
                {"pos": vec(1.49598e11, 0, 0), "radius": 6.371e6, "emissive": False, "mass": 5.9722e24, "velocity": vec(0,0,29780), "color": vec(0,0.5,1), "name": "Earth", "texture": images.earth_texture},
            
                # LUA: Pos Terra + 384,400 km | Vel Terra + 1.022 km/s
                {"pos": vec(1.49598e11 + 3.844e8, 0, 0), "radius": 1.7371e6, "emissive": False, "mass": 7.3476e22, "velocity": vec(0,0,29780 + 1022), "color": vec(0.8,0.8,0.8), "name": "Moon", "texture": None},
            
                # MARTE: 227.9M km | Raio 3,389 km | Vel 24.07 km/s
                {"pos": vec(2.27939e11, 0, 0), "radius": 3.3895e6, "emissive": False, "mass": 6.39e23, "velocity": vec(0,0,24070), "color": vec(1,0.3,0), "name": "Mars", "texture": images.mars_texture},
            
                # JÚPITER: 778.6M km | Raio 69,911 km | Vel 13.07 km/s
                {"pos": vec(7.7857e11, 0, 0), "radius": 6.9911e7, "emissive": False, "mass": 1.8982e27, "velocity": vec(0,0,13070), "color": vec(0.8,0.7,0.5), "name": "Jupiter", "texture": images.jupiter_texture},
            
                # SATURNO: 1.433B km | Raio 58,232 km | Vel 9.68 km/s
                {"pos": vec(1.4335e12, 0, 0), "radius": 5.8232e7, "emissive": False, "mass": 5.6834e26, "velocity": vec(0,0,9680), "color": vec(0.9,0.8,0.6), "name": "Saturn", "texture": images.saturn_texture},
            
                # ÚRANO: 2.872B km | Raio 25,362 km | Vel 6.80 km/s
                {"pos": vec(2.8725e12, 0, 0), "radius": 2.5362e7, "emissive": False, "mass": 8.681e25, "velocity": vec(0,0,6800), "color": vec(0.6,0.9,1), "name": "Uranus", "texture": images.uranus_texture},
            
                # NEPTUNO: 4.495B km | Raio 24,622 km | Vel 5.43 km/s
                {"pos": vec(4.4951e12, 0, 0), "radius": 2.4622e7, "emissive": False, "mass": 1.0241e26, "velocity": vec(0,0,5430), "color": vec(0.2,0.4,1), "name": "Neptune", "texture": images.neptune_texture}
            ]
        },
    "3 Body Problem": {
        "configs": {
            "range": 15,
            "dt": 0.001,
            "vector_scaling_velocity": 0.5,
            "vector_scaling_force": 0.5,
            "vector_shaft_width": 0.01
        },
        "planets": [
            {"pos": vec(0.97000436, -0.24308753, 0), "radius": 0.05, "emissive": False, "mass": 1 / 6.67430e-11, "velocity": vec(0.46620381, 0.43236573, 0), "color": vec(1,0,0), "name": "A", "texture": None},
            {"pos": vec(-0.97000436, 0.24308753, 0), "radius": 0.05, "emissive": False, "mass": 1 / 6.67430e-11, "velocity": vec(0.46620381, 0.43236573, 0), "color": vec(0,1,0), "name": "B", "texture": None},
            {"pos": vec(0, 0, 0), "radius": 0.05, "emissive": False, "mass": 1 / 6.67430e-11, "velocity": vec(-0.93240762, -0.86473146, 0), "color": vec(0,0,1), "name": "C", "texture": None}
        ]
    },
    "Solar System(Reduced)": {
        "configs": {
            "range": 6e10, 
            "dt": 1000, 
            "vector_scaling_velocity": 5e4, 
            "vector_scaling_force": 1e6, 
            "vector_shaft_width": 2e8
        },
        "planets": [
            {"pos": vec(0,0,0), "radius": 2e9, "emissive": True, "mass": 1.989e30, "velocity": vec(0,0,0), "color": vec(1,1,0), "name": "Sun", "texture": images.sun_texture},
            {"pos": vec(4.5e9, 0, 0), "radius": 3e8, "emissive": False, "mass": 3.301e23, "velocity": vec(0,0,172000), "color": vec(0.7,0.7,0.7), "name": "Mercury", "texture": images.mercury_texture},
            {"pos": vec(6.5e9, 0, 0), "radius": 5e8, "emissive": False, "mass": 4.867e24, "velocity": vec(0,0,143000), "color": vec(0.9,0.8,0.5), "name": "Venus", "texture": images.venus_texture},
            {"pos": vec(8.5e9, 0, 0), "radius": 5.5e8, "emissive": False, "mass": 5.972e24, "velocity": vec(0,0,125000), "color": vec(0,0.5,1), "name": "Earth", "texture": images.earth_texture},
            {"pos": vec(1.2e10, 0, 0), "radius": 4e8, "emissive": False, "mass": 6.39e23, "velocity": vec(0,0,105000), "color": vec(1,0.3,0), "name": "Mars", "texture": images.mars_texture},
            {"pos": vec(2.2e10, 0, 0), "radius": 1.2e9, "emissive": False, "mass": 1.898e27, "velocity": vec(0,0,76000), "color": vec(0.8,0.7,0.5), "name": "Jupiter", "texture": images.jupiter_texture},
            {"pos": vec(3.5e10, 0, 0), "radius": 1e9, "emissive": False, "mass": 5.683e26, "velocity": vec(0,0,62000), "color": vec(0.9,0.8,0.6), "name": "Saturn", "texture": images.saturn_texture},
            {"pos": vec(5.5e10, 0, 0), "radius": 7e8, "emissive": False, "mass": 8.681e25, "velocity": vec(0,0,49000), "color": vec(0.5,0.8,1), "name": "Uranus", "texture": images.uranus_texture},
            {"pos": vec(8e10, 0, 0), "radius": 7e8, "emissive": False, "mass": 1.024e26, "velocity": vec(0,0,41000), "color": vec(0.2,0.4,1), "name": "Neptune", "texture": images.neptune_texture}
        ]
    },
    "Saturn": {
        "configs": {
            "range": 2e9, 
            "dt": 100,
            "vector_scaling_velocity": 1e4,
            "vector_scaling_force": 1e20,
            "vector_shaft_width": 5e6
        },
        "planets": [
            {"pos": vec(0,0,0), "radius": 5.82e7, "emissive": False, "mass": 5.683e26, "velocity": vec(0,0,0), "color": vec(0.9, 0.8, 0.6), "name": "Saturn", "texture": images.saturn_texture},
            {"pos": vec(1.85e8, 0, 0), "radius": 1.98e5, "emissive": False, "mass": 3.75e19, "velocity": vec(0, 0, 14280), "color": vec(0.7, 0.7, 0.7), "name": "Mimas", "texture": None},
            {"pos": vec(2.38e8, 0, 0), "radius": 2.52e5, "emissive": False, "mass": 1.08e20, "velocity": vec(0, 0, 12630), "color": vec(0.9, 0.9, 1), "name": "Enceladus", "texture": None},
            {"pos": vec(2.94e8, 0, 0), "radius": 5.31e5, "emissive": False, "mass": 6.17e20, "velocity": vec(0, 0, 11350), "color": vec(0.8, 0.8, 0.8), "name": "Tethys", "texture": None},
            {"pos": vec(3.77e8, 0, 0), "radius": 5.61e5, "emissive": False, "mass": 1.09e21, "velocity": vec(0, 0, 10030), "color": vec(0.8, 0.8, 0.7), "name": "Dione", "texture": None},
            {"pos": vec(5.27e8, 0, 0), "radius": 7.63e5, "emissive": False, "mass": 2.30e21, "velocity": vec(0, 0, 8480), "color": vec(0.8, 0.8, 0.9), "name": "Rhea", "texture": None},
            {"pos": vec(1.22e9, 0, 0), "radius": 2.57e6, "emissive": False, "mass": 1.345e23, "velocity": vec(0, 0, 5570), "color": vec(1, 0.9, 0.3), "name": "Titan", "texture": None}
        ]
    },

    "Empty": {"configs": {"range": 100, "dt": 0.01, "vector_scaling_velocity": 1, "vector_scaling_force": 1, "vector_shaft_width": 0.05}, "planets": []}
}

def load_preset(key):
    objects.disable_all_objects(objects.object_dict)

    config = presets_dict[key]["configs"]
    state.dt = config["dt"]
    state.vector_scaling_velocity = config["vector_scaling_velocity"]
    state.vector_scaling_force = config["vector_scaling_force"]
    state.vector_shaft_width = config["vector_shaft_width"]
    scene.range = config["range"]

    for planet in presets_dict[key]["planets"]:
        objects.create_new_planet(
            planet["pos"], 
            planet["radius"], 
            planet["color"], 
            planet["emissive"], 
            planet["mass"], 
            planet["velocity"], 
            planet["name"], 
            objects.object_dict, 
            planet["texture"]
        )

    if key == "Saturn":
        # Criar 200 partículas para os anéis
        saturn_mass = 5.683e26
        G = 6.67430e-11
    
        for i in range(1000):

            dist = random.uniform(7e7, 1.4e8) 
            angle = random.uniform(0, 2*pi)
        
            pos_x = dist * cos(angle)
            pos_z = dist * sin(angle)
        
            v_mag = sqrt(G * saturn_mass / dist)
            v_vec = vec(-v_mag * sin(angle), 0, v_mag * cos(angle))
        
            objects.create_new_planet(
                vec(pos_x, 0, pos_z), 
                1e6, # Partículas pequenas
                vec(0.7, 0.6, 0.5), 
                False, 
                1e10, # Massa desprezível
                v_vec, 
                f"ring_part_{i}", 
                objects.object_dict, 
                None
            )

    print(f"Preset {key} carregado com sucesso.")