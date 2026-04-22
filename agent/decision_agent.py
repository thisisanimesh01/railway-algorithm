import random


class DecisionAgent:
    def __init__(self):
        self.q_table = {}

        self.epsilon = 1.0
        self.min_epsilon = 0.05
        self.decay = 0.98

        self.alpha = 0.1
        self.gamma = 0.9

    def get_state_key(self, state):
        return tuple(
            (
                t["id"],
                t["current"],
                t["next"],
                t["priority"],
                t["wait_time"],
                t["remaining_stops"]
            )
            for t in state["trains"]
        )

    def choose_action(self, state):
        actions = []

        for t in state["trains"]:
            actions.append(("MOVE", t["id"]))
            actions.append(("STOP", t["id"]))

        if not actions:
            return None

        if random.random() < self.epsilon:
            return random.choice(actions)

        state_key = self.get_state_key(state)

        if state_key not in self.q_table:
            self.q_table[state_key] = {}

        best_action = None
        best_value = -999

        for action in actions:
            value = self.q_table[state_key].get(action, 0)

            if value > best_value:
                best_value = value
                best_action = action

        return best_action if best_action else random.choice(actions)

    def update_q(self, state, action, reward, next_state):
        if action is None:
            return

        state_key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        if state_key not in self.q_table:
            self.q_table[state_key] = {}

        if next_key not in self.q_table:
            self.q_table[next_key] = {}

        current_q = self.q_table[state_key].get(action, 0)

        max_next_q = 0
        if self.q_table[next_key]:
            max_next_q = max(self.q_table[next_key].values())

        new_q = current_q + self.alpha * (
            reward + self.gamma * max_next_q - current_q
        )

        self.q_table[state_key][action] = new_q

    def decay_epsilon(self):
        if self.epsilon > self.min_epsilon:
            self.epsilon *= self.decay