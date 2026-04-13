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

sim = Simulator([train1, train2])

# Run simulation
for _ in range(5):
    print("\n--- STEP ---")
    sim.step()