#!/usr/bin/python3
"""Console for stylemate"""

import cmd
from models.base import BaseItem
from models.bottom import Bottom
from models.top import Top
from models.user import User
from utils.database import Database
import json
import json_files
import mysql.connector
import sys
import os

class StyleMate (cmd.Cmd):
    """The StyleMate command line interface."""
    prompt  = '(StyleMate)'
    intro   = "Welcome to the StyleMate Command Line Interface! \n\n Type help or ? to list all avaliable commands.\n" \
            "To exit type exit exit .\n\n"

    classes = {"base": BaseItem, 'top': Top, 'bottoms': Bottom, 'database': Database}

    def do_exit(self, *args):
        """Exit the program and return to shell"""
        return True
    def emptyline(self):
        """ overides the empty line method """
        pass
    def do_list(self, *args):
        """Show list of avaliable commands"""
        print("all avaliable commands")
        pass

    # Retrives all the items from json_file (tops & bottom.json)
    def do_show(self, *args):
        """show waldrope"""
        with open('json_files/tops.json', 'r') as f:
            data_tops = json.load(f)

        with open('json_files/bottoms.json', 'r') as f:
            data_bottom = json.load(f)
        # print (data_tops, data_bottom)

        # convert tops to a table
        output_tops = []
        for key, value in data_tops.items():
            output_tops.append(f"{key}: {value}")

        output_bottoms = []
        for key, value in data_bottom.items():
            output_bottoms.append(f"{key}: {value}")

        print("\nTOPS\n")
        for i, item in enumerate(output_tops, start=1):
             print(f"{i}. {item}")

        print("\nBOTTOMS\n")
        for i, item in enumerate(output_bottoms, start=1):
             print(f"{i}. {item}")

        pass

    def do_delete(self, item_id):
        """ Delete item with the item_id from database"""
        try:
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                Database = "StyleMate_db",
                password = "password"
            )
            cursor = conn.cursor()

            cursor.execute(f"Delete selected item with the {item_id} from the database")

            conn.commit()

            print(f"Item with {item_id} has been deleted.")
        except Exception as e:
            print(f"Error deleting item: {str(e)}")
        finally:
            conn.close()

    def do_total(self, count_id):
        """Prints the total number of outfits avaliable"""
        try:
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                Database = "StyleMate_db",
                password = "password"
            )
            cursor = conn.cursor()

            cursor.execute(f"SELECT COUNT(*) ")
            # count all the otfits
            total_count = cursor.fetchone()[0]

            conn.commit()

            print(f"Total outfits avaliable {total_count}.")
        except Exception as e:
            print(f"Error retriving total number of outfits : {str(e)}")

        finally:
            conn.close()


    def lastcmd(self):
        """Last non empty command prefix seen"""
        pass

    def do_restart(self, *args):
        """Restart the CLI"""
        print('Restarting...')
        os.system('python console.py')
        # os._exit(1)
        # sys.restart


    # def do_create_user(username, password):
    #     """ Create a new User"""
    #     try:
    #         conn = mysql.connector.connect(
    #             host = "localhost"
    #             user = "root"
    #             pass
    #         )



if __name__ == "__main__":
    StyleMate().cmdloop()

