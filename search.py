import csv

from prettytable import PrettyTable

import logger


def show_all():

    my_table = PrettyTable()
    with open('Notes.csv', 'r', newline='\n') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if count == 0:
                my_table.field_names = row
                count += 1
            else:
                my_table.add_row(row)
    print(my_table)
    logger.logging.info("Search has done")


def find_record():
    x = input("Enter word for search or date in format yyyy-mm-dd: ")
    if x != "":
        my_table = PrettyTable()
        with open('Notes.csv', 'r', newline='\n') as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if count == 0:
                    my_table.field_names = row
                    count += 1
                else:
                    for i in range(0, len(row)):
                        if x.lower() in row[i].lower():
                            my_table.add_row(row)
        print(my_table)
    else:
        return

    logger.logging.info("Search has done")
