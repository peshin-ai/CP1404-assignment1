"""
Replace the contents of this module docstring with your own details
Name: Ung Ta Hoang Tuan
Date started: 29/11/2020
GitHub URL: https://github.com/peshin-ai
"""
import csv


def Close():
    print("bye bye")


def WatchedMovies():
    pass


def AddMovies():
    pass


def LoadMovies():
    pass


def Process(char):
    if char == "L":
        LoadMovies()
    elif char == "A":
        AddMovies()
    elif char == "W":
        WatchedMovies()
    else:
        Close()


def Option():
    char = input().upper()
    while char not in ["L", "A", "W", "Q"]:
        char = input()
    Process(char)


def Menu():
    print("L - List movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q- Quit")
    Option()


def main():
    """..."""
    print("Movies To Watch 1.0 - by Ung Ta Hoang Tuan")
    # TODO changing it
    global Line, Csv_File
    RawFile = open('movies.csv', 'r')
    Csv_File = csv.reader(RawFile, delimiter=',')
    Line = len(list(Csv_File))
    print("{} movies loaded".format(Line))
    Menu()

    RawFile.close()


if __name__ == '__main__':
    main()
