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
        """
        action = which train to allow / which decision to take
        """

        reward = 0

        current_trains = self.state_manager.trains
        conflicts = self.conflict_detector.check(current_trains)
        conflict = len(conflicts) > 0

        if conflict:
            reward -= 10  # penalty
        else:
            success = self.track_manager.assign(action)

            if success:
                reward += 5
            else:
                reward -= 2

        self.state_manager.update(action)

        self.time_step += 1

        if self.time_step > 50:
            self.done = True

        next_state = self.get_state()

        return next_state, reward, self.done