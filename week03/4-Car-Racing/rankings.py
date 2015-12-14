from random import uniform
from random import choice


class Race:

    def __init__(self, drivers):
        self._chance = 0
        self._sorted_rank = []
        self._race_out = []
        self._result = {}
        self._drivers = drivers
        self._points = [8, 6, 4]
        self._out_count = 0
        self._rankings = {}

    def chance(self):
        self._chance = round(uniform(0, 1), 2)

    def out_count(self):
        if 0.25 >= self._chance >= 0:
            pass
        elif 0.5 >= self._chance > 0.25:
            self._out_count = 1
        elif 0.75 >= self._chance > 0.5:
            self._out_count = 2
        elif self._chance > 0.75:
            self._out_count = 3

    def get_ranking(self):
        self._rankings = {hash(self._drivers[i]._name + self._drivers[i]._car + self._drivers[i]._model + str(
            self._drivers[i]._max_speed) + str(self._chance)): self._drivers[i]._name for i in range(len(self._drivers))}
        self._sorted_rank = list(sorted(self._rankings.keys(), reverse=True))

    def drop_out(self):
        if self._out_count == 0:
            pass
        else:
            for looser in range(self._out_count):
                self._race_out.append(choice(self._sorted_rank))
            for outer in self._race_out:
                self._sorted_rank.remove(outer)

    def points(self):
        for i in range(len(self._sorted_rank)):
            self._result.update({self._rankings[self._sorted_rank[i]]: self._points[i]})
        for j in self._rankings.values():
            if j not in self._result.keys():
                self._result.update({j: 0})
            else:
                pass

    def standings(self):
