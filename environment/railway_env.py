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
        # Reset everything
        self.track_manager.reset()
        self.state_manager.reset()

        self.time_step = 0
        self.done = False

        return self.get_state()

    def get_state(self):
        # Return current system state
        return self.state_manager.get_state()

    def step(self, action):
        reward = 0

        current_trains = self.state_manager.trains

        conflicts = self.conflict_detector.check(current_trains)

        if conflicts:
            reward -= 15
        else:
            reward += 10

        success = self.track_manager.assign(action)

        if success:
            reward += 20
        else:
            reward -= 5

        if action:
            reward += action.priority * 5

        for train in current_trains:
            if train != action:
                reward -= train.wait_time * 0.1

        self.state_manager.update(action)

        self.time_step += 1

        if self.time_step > 50:
            self.done = True

        next_state = self.get_state()

        return next_state, reward, self.done