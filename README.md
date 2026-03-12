# 3D Solar System Simulator

3D solar system simulator with real-time N-body gravitational physics, energy graphs, and custom planet creation. Built with Python and VPython.

---

## Features

- Real-time N-body gravitational physics simulation
- Live energy tracking (kinetic, potential and total) with graphs
- Multiple presets: Solar System (scaled & reduced), Saturn, 3-Body Problem
- Custom planet creation with mass, radius, position, velocity, color and texture
- Interactive controls: camera focus, trail toggles, vector visualization, grid and adjustable time step
- Pause, reset and restart simulation at any time

---

## Requirements

- Python 3.x
- VPython

Install dependencies:

```bash
pip install vpython
```

---

## How to Run

```bash
python main.py
```

---

## Controls

| Key | Action |
|-----|--------|
| `↑` / `↓` | Cycle camera focus between objects |
| `←` / `→` | Decrease / increase time step (delta T) |
| `T` | Toggle object trails |
| `V` | Toggle velocity/force vectors |
| `G` | Toggle grid |

---

## Project Structure

```
├── main.py           # Entry point and main simulation loop
├── objects.py        # Celestial body definitions and grid
├── physics.py        # Gravitational physics calculations
├── input_handler.py  # Keyboard input and UI controls
├── images.py         # Background textures
└── state.py          # Global simulation state
```

---

## Presets

- **Solar System (Scale)** — realistic scale solar system
- **Solar System (Reduced)** — scaled-down version for easier viewing
- **Saturn** — Saturn with ring system
- **3 Body Problem** — Classic infinite 8 system
- **Empty** — blank canvas to build your own system

---

## Custom Planet Creation

Use the in-app UI panel to create custom planets with:
- Name, mass and radius
- Initial position (x, y, z)
- Initial velocity (x, y, z)
- Color (R, G, B)
- Optional texture
- Emissive toggle (for stars)
