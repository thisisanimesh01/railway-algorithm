class ConflictDetector:
    def __init__(self):
        pass

    def check(self, trains):
        conflicts = []

        for i in range(len(trains)):
            for j in range(i + 1, len(trains)):
                t1, t2 = trains[i], trains[j]

                # Same direction conflict
                if (
                    t1.current_station == t2.current_station and
                    t1.next_station == t2.next_station
                ):
                    conflicts.append((t1, t2))

                # Head-on collision
                if (
                    t1.current_station == t2.next_station and
                    t1.next_station == t2.current_station
                ):
                    conflicts.append((t1, t2))

        return conflicts


def detect_conflicts(trains):
    detector = ConflictDetector()
    return detector.check(trains)