class TrackManager:
    def __init__(self):
        self.track_capacity = {}   # (A, B) -> max tracks
        self.track_usage = {}      # (A, B) -> current usage

    def set_capacity(self, from_station, to_station, capacity):
        self.track_capacity[(from_station, to_station)] = capacity
        self.track_capacity[(to_station, from_station)] = capacity

        self.track_usage[(from_station, to_station)] = 0
        self.track_usage[(to_station, from_station)] = 0

    def can_use(self, from_station, to_station):
        return self.track_usage[(from_station, to_station)] < self.track_capacity[(from_station, to_station)]

    def occupy(self, from_station, to_station):
        self.track_usage[(from_station, to_station)] += 1

    def release_all(self):
        for key in self.track_usage:
            self.track_usage[key] = 0