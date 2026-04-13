class DecisionAgent:
    def resolve(self, conflicts):
        actions = []

        for t1, t2 in conflicts:

            if t1.priority > t2.priority:
                t2.status = "STOPPED"
                t2.wait_time = 2  # wait for 2 steps
                actions.append(f"Train {t2.train_id} stopped for 2 steps (lower priority)")

            elif t2.priority > t1.priority:
                t1.status = "STOPPED"
                t1.wait_time = 2
                actions.append(f"Train {t1.train_id} stopped for 2 steps (lower priority)")

            else:
                t2.status = "STOPPED"
                t2.wait_time = 1
                actions.append(f"Train {t2.train_id} stopped (tie-breaker)")

        return actions