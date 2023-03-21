from classes import TransmissionGenerator
from pprint import pprint

def print_trans(trans):
    for t in trans:
        print(t, "\n")
        
def main():
    tg = TransmissionGenerator()
    trans = tg.generate_transmissions(2)
    print_trans(trans)
    input("Waiting...")
    trans = tg.sort_trans(tg.SortOrder.SPEED)
    print_trans(trans)
    input("Waiting...")
    trans = tg.sort_trans(tg.SortOrder.TORQUE)
    print_trans(trans)


if __name__ == "__main__":
    main()
