from engine.track_manager import TrackManager
from engine.conflict_detector import ConflictDetector
from state.state_manager import StateManager


class RailwayEnv:
    def __init__(self):
        self.track_manager = TrackManager()
        self.conflict_detector = ConflictDetector()
        self.state_manager = StateManager()

        self.time_step = 0
        self.done = False

    def reset(self):
        self.track_manager.reset()
        self.state_manager.reset()

        self.time_step = 0
        self.done = False

        return self.get_state()

    def get_state(self):
        return self.state_manager.get_state()

    def step(self, action):
        reward = 0
        trains = self.state_manager.trains

        action_type, train_id = action if action else (None, None)

        selected_train = None
        for t in trains:
            if t.train_id == train_id:
                selected_train = t
                break

        #  Conflict penalty (reduced but still important)
        conflicts = self.conflict_detector.check(trains)
        if conflicts:
            reward += 60

        #  MOVE action only
        if action_type == "MOVE" and selected_train:
            success = self.track_manager.assign(selected_train)

            if success:
                selected_train.move()
                reward += 40
            else:
                selected_train.wait_time += 1
                reward -= t.wait_time * 0.05  #  Waiting penalty for failed move (reduced)

        #  Waiting penalty (reduced)
        for t in trains:
            reward -= t.wait_time * 0.1

        #  Priority reward
        if selected_train:
            reward += selected_train.priority * 3

        # Destination reward (very important)
        if selected_train and selected_train.next_station is None:
            reward += 100

        self.time_step += 1

        if self.time_step > 50:
            self.done = True

        next_state = self.get_state()

        return next_state, reward, self.done