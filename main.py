from classes import Transmission
from pprint import pprint


def main():
    trans = Transmission.generate_transmissions(2)
    for t in trans:
        print(t, "\n")


if __name__ == "__main__":
    main()
