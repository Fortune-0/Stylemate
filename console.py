import cmd
from models.base import BaseItem
from models.bottom import Bottom
from models.top import Top
from models.user import User
from utils.database import Database
import json
import json_files
# import mysql.connector
import sys
import os
# from utils.database import Session

class StyleMate(cmd.Cmd):
    """The StyleMate command line interface."""
    prompt = '(StyleMate) ## '
    intro = "Welcome to the StyleMate Command Line Interface!\n\nType help or ? to list all available commands.\n"\
            "To exit type exit or press Ctrl+D.\n\n"
    classes = {"base": BaseItem, 'top': Top, 'bottoms': Bottom, 'database': Database}

    # def __init__(self):
    #     super().__init__()
    #     username = "",
    #     password = ""
    #     self.database = Database(username, password)


    def do_category(self, database):
        """get category"""
        try:
            categories = database.get_cty()
            if categories:
                print("Available categories:")
            for category in categories:
                print(f"- {category}")

            else:
                print(" NO CATEGORIES FOUND IN DATABASE")

        except Exception as e:
            print(f"Error retriving database {str(e)}")

    def do_add():
        """Adds a category"""
        pass

    def do_exit(self, arg):
        """Exit the program and return to shell"""
        return True

    def emptyline(self):
        """ overides the empty line method """
        pass
    # def do_list(self, arg):
    #     """Show list of avaliable commands"""
    #     print("all avaliable commands")
    #     pass

    # Retrives all the items from json_file (tops & bottom.json)
    def do_show(self, *args):
        """show wardrobe"""
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

    def do_delete(self, Database, table_name, item_id):
        """ Delete item with the item_id from database"""
        try:
            item = Database.get_item_by_id(table_name, item_id)
            if item:
                Database.delete_item(table_name, item_id)
                print(f"{item_id} deleted from {table_name}")

            else:
                print(f" No item with ID {item_id} in table {table_name}")

        except Exception as e:
            print(f"Unexpected error: {e}")
    
    #     try:
    #         conn = mysql.connector.connect(
    #             host = "localhost",
    #             user = "root",
    #             database = "StyleMate_db",
    #             password = "password"
    #         )
    #         cursor = conn.cursor()

    #         cursor.execute(f"Delete selected item with the {item_id} from the database")

    #         conn.commit()

    #         print(f"Item with {item_id} has been deleted.")
    #     except Exception as e:
    #         print(f"Error deleting item: {str(e)}")
    #     finally:
    #         conn.close()

    def do_total(self, database, table_name, count_id):
        """Prints the total number of outfits avaliable"""
        try:
            total = database.get_total(table_name, count_id)
            print("You have {count_id} Outfits Avaliable in {table_name}: ", {total})
        except IndexError:
            print('Please enter a valid category')
        except  Exception as e:
            print(f"An error occured: {str(e)}")

    def do_gender(self, user_id):
        """ Gets the gender of the User """
        try:

            gender = self.database.get_gender(user_id)
            if gender:
                print(f"User {user_id} is a: {gender}")
            else:
                print(f"Gender infomation for {user_id} not found in the database.")
        except Exception as e:
            print(f" An error Occured {str(e)} .")

        # try:
        #     user_sex = self.__Session__.query(Database.table_classes.get("User")).first()
        #     if user_sex:
        #         print(f"Gender: {user_sex}")
        #     else:
        #         print("Current User not found in Database, please sign-up")
        # except Exception as e:
        #         print(f"Error retriving User's gender: {str(e)} ")

    # def  do_user_name(self, *args):
    #     """ Gets the user name of the current User """
    #     try:
    #        user = Database.get_user_name():
    #         if user:
    #             print(f" Hey: {user} :")
    #         else:
    #             print("User not found!!!!")
    #     except Exception as e:
    #         print("An error occured : ", str(e))

    def lastcmd(self):
        """Last non empty command prefix seen"""
        pass

    def do_restart(self, *args):
        """Restart the CLI"""
        print('Restarting...')
        os.system('python console.py')
        # os._exit(1)

if __name__ == "__main__":
    StyleMate().cmdloop()
