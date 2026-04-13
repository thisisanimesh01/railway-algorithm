class TrackManager:
    def __init__(self):
        self.track_capacity = {}
        self.track_usage = {}

    def reset(self):
        # reset usage but keep capacity
        for key in self.track_usage:
            self.track_usage[key] = 0

    def set_capacity(self, from_station, to_station, capacity):
        self.track_capacity[(from_station, to_station)] = capacity
        self.track_capacity[(to_station, from_station)] = capacity

        self.track_usage[(from_station, to_station)] = 0
        self.track_usage[(to_station, from_station)] = 0

    def can_use(self, from_station, to_station):
        return self.track_usage.get((from_station, to_station), 0) < self.track_capacity.get((from_station, to_station), 1)

    def assign(self, train):
        if train is None or train.next_station is None:
            return False

        from_station = train.current_station
        to_station = train.next_station

        if (from_station, to_station) not in self.track_capacity:
            self.set_capacity(from_station, to_station, 2)

        if self.can_use(from_station, to_station):
            self.track_usage[(from_station, to_station)] += 1
            return True

        return False

    def release_all(self):
        for key in self.track_usage:
            self.track_usage[key] = 0