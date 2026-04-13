class DecisionAgent:
    def resolve(self, conflicts):
        actions = []

        for t1, t2 in conflicts:

            # Decide based on priority
            if t1.priority > t2.priority:
                t2.status = "STOPPED"
                actions.append(f"Train {t2.train_id} stopped (lower priority) vs Train {t1.train_id}")

            elif t2.priority > t1.priority:
                t1.status = "STOPPED"
                actions.append(f"Train {t1.train_id} stopped (lower priority) vs Train {t2.train_id}")

            else:
                # Same priority → fallback rule
                t2.status = "STOPPED"
                actions.append(f"Train {t2.train_id} stopped (tie-breaker) vs Train {t1.train_id}")

        return actions