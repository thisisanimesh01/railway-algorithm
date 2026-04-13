from engine.conflict_detector import detect_conflicts
from agent.decision_agent import DecisionAgent
from engine.track_manager import TrackManager

class Simulator:
    def __init__(self, trains):
        self.trains = trains
        self.agent = DecisionAgent()
        self.track_manager = TrackManager()

    def step(self):
        self.track_manager.release_all()  # reset each step

        for train in self.trains:

            if train.status == "RUNNING" and train.next_station:

                if not self.track_manager.is_occupied(train.current_station, train.next_station):
                    self.track_manager.occupy(train.current_station, train.next_station)
                    train.move()

                else:
                    train.status = "STOPPED"
                    train.wait_time = 1
                    print(f"Train {train.train_id} stopped (track occupied)")

            else:
                train.move()