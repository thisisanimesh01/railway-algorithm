from graph.network import RailwayNetwork
from state.state_manager import Train
from simulator.simulation import Simulator

# Create network
network = RailwayNetwork()
network.add_station("A")
network.add_station("B")
network.add_station("C")

network.add_track("A", "B", 5)
network.add_track("B", "C", 5)

# Create trains with priority
train1 = Train(1, "A", ["A", "B", "C"], priority=3)  # Express
train2 = Train(2, "A", ["A", "B", "C"], priority=1)  # Goods

sim = Simulator([train1, train2], network)

# Set track capacities
sim.track_manager.set_capacity("A", "B", 1)  # single track
sim.track_manager.set_capacity("B", "C", 2)  # double track

# Run simulation for 10 steps
for step in range(10):
    print(f"Step {step + 1}")
    sim.step()
    print(f"Train 1: {train1.status}, Train 2: {train2.status}\n")