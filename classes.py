from enum import Enum
from itertools import permutations as perms


class Direction(Enum):
    FROM = 1
    TO = -1


Gearing = {
    "1:1": 1.0,
    "6:5": 1.2,
    "3:2": 1.5,
    "9:5": 1.8,
    "2:1": 2.0,
    "5:2": 2.5,
    "3:1": 3.0,
    # "-1:1": -1.0,
}


class Gearbox:
    def __init__(self, direction: Direction, gearing_off="1:1", gearing_on="1:1"):
        self._dir = direction
        self._g_off = gearing_off
        self._g_on = gearing_on

    def flip(self):
        self._dir = -self._dir

    @property
    def g_off(self):
        return Gearing[self._g_off] ** self._dir.value

    @g_off.setter
    def g_off(self, gearing_off="1:1"):
        self._g_off = gearing_off

    @property
    def g_on(self):
        return Gearing[self._g_on] ** self._dir.value

    @g_on.setter
    def g_on(self, gearing_on="1:1"):
        self._g_on = gearing_on

    def __str__(self) -> str:
        d = "<" if self._dir == Direction.TO else ">"
        return f"{d}({self._g_off}|{self._g_on})"


class Transmission:
    def __init__(self, gearboxes: list[Gearbox], final="1:1") -> None:
        self.gearboxes = gearboxes
        self.final = Gearing[final]
        self.calculate_ratios()
        self.max_gears = len(self._ratios)

    def calculate_ratios(self):
        n = len(self.gearboxes)
        settings = sorted(list(set(perms([False, True] * n, n))))
        self._ratios: list[float]
        self._order: list[tuple[bool]]
        totals = {setting: self.total(setting) for setting in settings}
        totals = sorted(totals.items(), key=lambda x: x[1])
        self._ratios = [r for _, r in totals]
        self._order = [s for s, _ in totals]

    @property
    def ratios(self) -> list:
        return self._ratios

    @property
    def order(self) -> list:
        return self._order

    def total(self, setting: tuple[bool | int]) -> float:
        total = self.final
        for box, on in zip(self.gearboxes, setting):
            total *= box.g_on if on else box.g_off
        return round(total, 3)

    def deltas(self) -> list:
        r = self._ratios
        return [round(r[i + 1] - r[i], 3) for i in range(len(r) - 1)]

    def average(self) -> list:
        sum(self._ratios) / self.max_gears

    def drop(self, gear: int):
        del self._ratios[gear - 1]
        del self._order[gear - 1]

    def __str__(self) -> str:
        res = "\n".join(
            [
                "".join([str(g) for g in self.gearboxes]),
                "\n".join([f"{n}:"+f"{c}"[1:-1] for n, c in enumerate(zip(self.order, self.ratios), 1)]),
            ]
        )
        return res
