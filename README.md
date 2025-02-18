# Lift Simulation

## Overview
This program simulates a lift system using Pygame. It includes multiple floors and lifts that respond to user input, allowing for an interactive simulation of lift movement. Users can request lifts by clicking on floor buttons, and the program handles lift allocation efficiently.

## Features
- Multiple floors and lifts.
- Real-time lift movement and floor interaction.
- Smooth scrolling for better navigation.
- Dynamic button interaction to request lifts.
- Countdown timer showing estimated lift arrival time.

## Installation
### Requirements
Ensure you have Python installed, along with the required dependencies:
```sh
pip install pygame
```

### Running the Program
To start the simulation, execute the following command in your terminal:
```sh
python main.py
```

## Files Overview
- **main.py** - The entry point of the simulation, handles rendering and user interaction.
- **building.py** - Manages floors and lifts, assigns lifts to calls.
- **lift.py** - Controls lift movement and stopping behavior.
- **floor.py** - Handles individual floor behavior, including button interactions and timers.
- **config.py** - Stores global constants such as colors, dimensions, and simulation settings.

## How to Use
1. Run `main.py`.
2. Use the mouse to click floor buttons to call a lift.
3. The closest available lift will be allocated and will move toward the requested floor.
4. Scroll up or down if necessary to navigate between floors.
5. The simulation will continue running until the window is closed.

## Future Enhancements
- Improve visual aesthetics with animations.

## Author
Developed by Efi Goldberg

