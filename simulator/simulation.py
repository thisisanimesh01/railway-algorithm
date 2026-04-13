from engine.conflict_detector import detect_conflicts
from agent.decision_agent import DecisionAgent

class Simulator:
    def __init__(self, trains):
        self.trains = trains
        self.agent = DecisionAgent()

    def step(self):
        # Move trains
        for train in self.trains:
                train.move()

        # Detect conflicts
        conflicts = detect_conflicts(self.trains)

        # Resolve conflicts
        if conflicts:
            actions = self.agent.resolve(conflicts)
            for act in actions:
                print(act)