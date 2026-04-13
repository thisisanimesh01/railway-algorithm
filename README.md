# Railway Algorithm
This project implements a simple railway scheduling algorithm using a priority-based approach. The algorithm ensures that higher-priority trains (e.g., express) are given precedence over lower-priority trains (e.g., goods) when scheduling tracks, thus minimizing delays and optimizing track usage.

## Key Features
- **Track Management**: The system allows for the creation of tracks between stations with specified travel times.
- **Train Scheduling**: Trains are scheduled based on their priority, ensuring that express trains are given precedence over goods trains.
- **Conflict Detection**: The simulator detects and resolves conflicts when multiple trains attempt to use the same track simultaneously.

## Usage
1. Define the railway network by adding tracks between stations.
2. Create trains with specified routes and priorities.
3. Run the simulation to see how trains are scheduled and moved across the network.

## STILL LIMITATIONS
- The current implementation is a simplified model and may not cover all real-world scenarios (e.g., track maintenance, varying train speeds, etc.).
- The conflict resolution strategy is basic and may need enhancement for more complex networks.

## Future Enhancements
- Implement more sophisticated scheduling algorithms (e.g., shortest path, dynamic scheduling).
- Add support for more complex train behaviors (e.g., varying speeds, stops at stations).
- Integrate a graphical interface for better visualization of the railway network and train movements.