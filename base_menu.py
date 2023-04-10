import logging

import records_work
import data_input
import search

def main_menu():
    while True:
        mode = input("Enter\n"
                     "1 - add new record\n"
                     "2 - delete record\n"
                     "3 - edit record\n"
                     "4 - find\n"
                     "5 - show all\n"
                     "6 = exit\n")
        match mode:
            case "1":
                records_work.record_to_add(data_input.data_receive())
            case "2":
                records_work.delete_record()
            case "3":
                records_work.edit_record()
            case "4":
                search.find_record()
            case "5":
                search.show_all()
            case "6":
                break
            case _:
                logging.warning("Wrong item selected")
                print("Error")

