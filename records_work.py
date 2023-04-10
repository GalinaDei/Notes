import csv
import datetime
import os
from prettytable import PrettyTable
import logger


def csv_create():
    with open('ID.txt', 'r') as f:
        id = f.readline()

    if id == "":
        with open("Notes.csv", "a") as data:
            names = ["ID", "Theme", "Note", 'Date']
            file_writer = csv.DictWriter(data, fieldnames=names)
            file_writer.writeheader()
    logger.logging.info("New record")


def record_to_add(dict):
    with open("Notes.csv", "a") as data:
        names = list(dict.keys())
        file_writer = csv.DictWriter(data, fieldnames=names)
        file_writer.writerow(dict)
        logger.logging.info("New record")


def delete_record():
    x = input("Enter word for search or date in format yyyy-mm-dd: ")
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
                        count += 1
    print(my_table)
    if count >= 2:
        y = input("Enter ID to confirm deletion or Enter to exit: ")
        with open('Notes.csv', 'r') as inp, open('Notes1.csv', 'w') as out:
            writer = csv.writer(out)
            count1 = 1
            for row in csv.reader(inp):
                count1 += 1
                if count1 % 2 == 0:
                    if row[0] != y:
                        writer.writerow(row)
            print("Record has updated.")

        os.remove('Notes.csv')
        os.rename('Notes1.csv', 'Notes.csv')
        logger.logging.info("Records update")
        return
    else:
        return


def edit_record():
    x = input("Enter word for search or date in format yyyy-mm-dd: ")
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
                        count += 1
    print(my_table)
    if count >= 2:
        y = input("Enter ID to continue edition or Enter to exit: ")

        with open('Notes.csv', 'r') as inp, open('Notes1.csv', 'w') as out:
            writer = csv.writer(out)
            count1 = 1
            for row in csv.reader(inp):
                count1 += 1
                if count1 % 2 == 0:
                    if row[0] != y:
                        writer.writerow(row)
                    else:
                        Theme = input("Theme: ")
                        Note = input("Note: ")
                        Date = str(datetime.datetime.now())+" (changed)"
                        new_value = [y, Theme, Note, Date]
                        writer.writerow(new_value)
            print("Record has updated.")

        os.remove('Notes.csv')
        os.rename('Notes1.csv', 'Notes.csv')
        logger.logging.info("Records update")
    else:
        return
