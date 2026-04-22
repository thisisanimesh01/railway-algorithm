from engine.conflict_detector import detect_conflicts
from agent.decision_agent import DecisionAgent
from engine.track_manager import TrackManager
from state.state_manager import StateManager


class Simulator:
    def __init__(self, trains, network):
        self.trains = trains
        self.agent = DecisionAgent()
        self.network = network
        self.track_manager = TrackManager()

        self.state_manager = StateManager()
        self.state_manager.trains = self.trains

    def step(self):
        self.track_manager.release_all()

        state = self.state_manager.get_state()

        action = self.agent.choose_action(state)

        for train in self.trains:

            if train.status == "STOPPED":
                train.move()
                continue

            if train == action and train.next_station:

                if self.track_manager.can_use(train.current_station, train.next_station):
                    self.track_manager.occupy(train.current_station, train.next_station)
                    train.move()

                else:
                    train.status = "STOPPED"
                    train.wait_time = 1
                    print(f"Train {train.train_id} waiting (no free track)")

            else:
                train.status = "STOPPED"
                train.wait_time += 1