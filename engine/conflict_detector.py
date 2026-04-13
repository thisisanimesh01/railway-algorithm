def detect_conflicts(trains):
    conflicts = []

    for i in range(len(trains)):
        for j in range(i + 1, len(trains)):
            t1, t2 = trains[i], trains[j]

            if (
                t1.current_station == t2.current_station and
                t1.next_station == t2.next_station
            ):
                conflicts.append((t1, t2))

    return conflicts