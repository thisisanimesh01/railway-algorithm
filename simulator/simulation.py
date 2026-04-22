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

        action_type, train_id = action if action else (None, None)

        selected_train = None
        for t in self.trains:
            if t.train_id == train_id:
                selected_train = t
                break

        for train in self.trains:
            train.status = "STOPPED"

        if action_type == "MOVE" and selected_train:
            if selected_train.next_station and self.track_manager.can_use(
                selected_train.current_station, selected_train.next_station
            ):
                self.track_manager.occupy(
                    selected_train.current_station,
                    selected_train.next_station
                )
                selected_train.status = "RUNNING"
                selected_train.move()
                selected_train.wait_time = 0
            else:
                selected_train.wait_time += 1

        elif action_type == "STOP" and selected_train:
            selected_train.wait_time += 1

        # increase wait time for others
        for train in self.trains:
            if train != selected_train:
                train.wait_time += 1