class TrackManager:
    def __init__(self):
        self.occupied_tracks = set()

    def is_occupied(self, from_station, to_station):
        return (from_station, to_station) in self.occupied_tracks

    def occupy(self, from_station, to_station):
        self.occupied_tracks.add((from_station, to_station))

    def release_all(self):
        self.occupied_tracks.clear()