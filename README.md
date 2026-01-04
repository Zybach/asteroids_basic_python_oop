# Asteroids (Python / Pygame)

This project is a small Python-based **Asteroids-style arcade game** implemented using **Pygame**.

It was created for learning and practice purposes, focusing on real-time game loops, sprite-based collision handling, and modular game architecture.

---

## Features

- **Classic Asteroids-style gameplay**
- Player-controlled spaceship with shooting mechanics
- Procedurally managed asteroid field
- Collision detection between:
  - shots and asteroids  
  - player and asteroids
- Fixed-frame game loop (60 FPS)
- Centralized configuration via constants
- Event and state logging for debugging and analysis

---

## How It Works

- Pygame initializes the window and main clock
- Sprite groups are used to separate concerns:
  - `updatable` – game logic updates  
  - `drawable` – rendering  
  - `asteroids` – asteroid entities  
  - `shots` – player projectiles
- The main loop:
  - processes user and system events  
  - updates all game objects using delta time  
  - checks collisions and triggers game logic  
  - renders all visible objects to the screen

---

## Project Structure

- **main.py** – game entry point and main loop  
- **constants.py** – screen size and gameplay constants  
- **player.py** – player ship logic and controls  
- **asteroid.py** – asteroid behavior and splitting logic  
- **asteroidfield.py** – asteroid spawning and field management  
- **shot.py** – projectile behavior  
- **logger.py** – state and event logging utilities  

---

## Gameplay Logic

- The player starts centered on the screen
- Asteroids spawn and move continuously
- Shooting an asteroid:
  - destroys or splits it into smaller parts  
- Collision between player and asteroid:
  - ends the game immediately
- Shot cooldown is handled using delta-time-based timers

---

## Output

- The game renders directly to a Pygame window
- Debug information (delta time, events) is printed to the console
- Game events such as:
  - asteroid hits  
  - player collisions  
  are logged via the logging module

---

## Notes

- The code favors **clarity and explicit logic** over abstraction
- Sprite containers are assigned dynamically to simplify entity management
- Logging is intentionally verbose to support debugging and learning

---

## Disclaimer

This project was written purely for **educational purposes**.  
It is not intended for production use or commercial distribution.
