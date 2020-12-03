import csv


def Quit():
    pass


def display():
    #TODO: rangign the list
    for row1 in rows:
        for row2 in rows:
            if int(row1[1]) > int(row2[1]):
                blank = row1
                row1 = row2
                row2 = blank

                # #TODO range name
                # blank = row1[0]
                # row1[0] = row2[0]
                # row1[0] = blank
                # #TODO range year
                # blank = row1[1]
                # row1[1] = row2[1]
                # row1[1] = blank
                # #TODO range type
                # blank = row1[2]
                # row1[2] = row2[2]
                # row1[2] = blank
                # #TODO range w and u
                # blank = row1[3]
                # row1[3] = row2[3]
                # row1[3] = blank

    #TODO: print the list after ranging
    i = 0
    for row in rows:
        if row[3] == 'u':
            print(str(i) + '.{:^3}'.format('*') + '{:40}'.format(row[0]) + '{:2}'.format('-') + '{:>4}'.format(
                row[1]) + ' ({})'.format(row[2]))
        else:
            print(str(i) + '.{:^3}'.format(' ') + '{:40}'.format(row[0]) + '{:2}'.format('-') + '{:>4}'.format(
                row[1]) + ' ({})'.format(row[2]))
        i += 1


def ReadFile():
    global rows, LineCount, RawFile
    # inital varible and array
    rows = []
    LineCount = 0
    # reading the csv file
    with open('movies.csv', 'r') as RawFile:
        Csv_File = csv.reader(RawFile, delimiter=',')

        # changing data in csv file -> array
        # count the line in
        for row in Csv_File:
            rows.append(row)
            LineCount += 1


def main():
    """..."""
    print("Movies To Watch 1.0 - by Ung Ta Hoang Tuan")

    ReadFile()
    print("{} movies loaded".format(LineCount))
    display()


if __name__ == '__main__':
    main()
