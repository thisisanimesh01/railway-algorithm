class Train:
    def __init__(self, train_id, current_station, route, priority):
        self.train_id = train_id
        self.current_station = current_station
        self.route = route
        self.next_station = route[1] if len(route) > 1 else None
        self.speed = 1
        self.status = "RUNNING"
        self.priority = priority
        self.wait_time = 0

    def move(self):
        if self.status == "STOPPED":
            return

        if self.next_station:
            self.current_station = self.next_station
            idx = self.route.index(self.current_station)

            if idx + 1 < len(self.route):
                self.next_station = self.route[idx + 1]
            else:
                self.next_station = None


class StateManager:
    def __init__(self):
        self.trains = []

    def reset(self):
        self.trains = [
            Train(1, "A", ["A", "B", "C"], priority=3),
            Train(2, "A", ["A", "B", "D"], priority=1),
            Train(3, "B", ["B", "C", "D"], priority=2),
        ]

    def get_state(self):
        state = []

        for t in self.trains:
            route_index = t.route.index(t.current_station)

            state.append({
                "id": t.train_id,
                "current": t.current_station,
                "next": t.next_station,
                "priority": t.priority,
                "wait_time": t.wait_time,
                "remaining_stops": len(t.route) - route_index - 1
            })

        return {
            "trains": state
        }

    def update(self, action):
        # no forced update (RL decides movement)
        pass