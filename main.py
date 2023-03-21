from classes import Transmission
from pprint import pprint

def print_trans(trans):
    for t in trans:
        print(t, "\n")
        
def main():
    tg = Transmission
    tg.generate_transmissions(3, inplace=True)
    tg.sort_trans(tg.SortOrder.SPEED, inplace=True)
    tg.write_to_file("./data/data.csv")
    print_trans(tg.get_transmissions())


if __name__ == "__main__":
    main()
