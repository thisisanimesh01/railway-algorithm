import random


class DecisionAgent:
    def __init__(self):
        pass

    def resolve(self, conflicts):
        actions = []

        for t1, t2 in conflicts:

            if t1.priority > t2.priority:
                t2.status = "STOPPED"
                t2.wait_time = 2
                actions.append(f"Train {t2.train_id} stopped for 2 steps")

            elif t2.priority > t1.priority:
                t1.status = "STOPPED"
                t1.wait_time = 2
                actions.append(f"Train {t1.train_id} stopped for 2 steps")

            else:
                t2.status = "STOPPED"
                t2.wait_time = 1
                actions.append(f"Train {t2.train_id} stopped (tie)")

        return actions

    def choose_action(self, state):
        trains = state["waiting_trains"]

        if not trains:
            return None

        best_train = None
        best_score = -999

        for train in trains:
            if train.status == "STOPPED":
                continue

            score = (train.priority * 10) + train.wait_time

            if score > best_score:
                best_score = score
                best_train = train

        if best_train is None:
            return random.choice(trains)

        return best_train