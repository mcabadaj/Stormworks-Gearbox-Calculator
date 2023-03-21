from classes import Gearbox, Direction, Gearing, Transmission
from itertools import permutations as perms, combinations as combs
from pprint import pprint

def main():

    # Number of gearboxes
    N = 3

    # All possible gearbox configurations
    options = []
    for r_on in Gearing:
        for r_off in Gearing:
            for d in Direction:
                options.append(Gearbox(d, r_off, r_on))

    groups = list(set(perms(options, N)))

    transmissions = []
    i = 0
    for group in groups:
        t = Transmission(group)
        t.calculate_ratios()
        if len(set(t._ratios)) != len(t._ratios):
            continue
        print(t)
        # transmissions.append(t)
        
        break


if __name__ == "__main__":
    main()
