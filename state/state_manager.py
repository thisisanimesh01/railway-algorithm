class Train:
    def __init__(self, train_id, current_station, route, priority):
        self.train_id = train_id
        self.current_station = current_station
        self.route = route
        self.next_station = route[1] if len(route) > 1 else None
        self.speed = 1
        self.status = "RUNNING"
        self.priority = priority
        self.wait_time = 0  # NEW

    def move(self):
        if self.status == "STOPPED":
            if self.wait_time > 0:
                self.wait_time -= 1
                print(f"Train {self.train_id} waiting... ({self.wait_time} left)")
                return

            # Resume happens here clearly
            self.status = "RUNNING"
            print(f"Train {self.train_id} resumed")

        if self.next_station:
            self.current_station = self.next_station
            idx = self.route.index(self.current_station)
            if idx + 1 < len(self.route):
                self.next_station = self.route[idx + 1]
            else:
                self.next_station = None