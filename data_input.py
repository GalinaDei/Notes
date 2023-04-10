import datetime

def data_receive():
    print("New record")
    with open('ID.txt', 'r+') as f:
        id0 = f.readline()
    if id0 == "":
        id = 1
    else:
        id = int(id0) + 1
    with open('ID.txt', 'w') as f:
        f.write(str(id))
    Theme = input("Theme: ")
    Note = input("Note: ")
    Date = str(datetime.datetime.now())+" (created)"
    notes_table = {'ID': id, 'Theme': Theme, 'Note': Note, 'Date': Date}

    return notes_table
