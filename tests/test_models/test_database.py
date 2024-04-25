#!/usr/bin/python3
#Test the Database class
from models.top import top
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest
from utils.database import Database

class TestDatabaseClass(unittest.TestCase):
    """Test the Database Class and its methods"""

    def setUp(self):
        """Create an instance of Database"""
        self.database = Database('anomalie', 'Olaniyielect23%')
        engine = create_engine("mysql://{}:{}@{}/stylemate_db".format("anomalie",
                               "Olaniyielect23%", "localhost"))
        Session = sessionmaker(bind=engine)
        self.__session__ = Session()
    def test_add_cty(self):
        """Test the method add_cty"""
        input_dict = {
            'name': 'jacket',
            'number': 2
        }
        return_result = self.database.add_cty(input_dict, "tops")
        self.assertListEqual(return_result, [input_dict[name], input_dict['number']])
    def test_get_all_cty(self):
        """Test get_all_cty Database instance method"""
        tests_result = self.__session__.query(Top).all()
        tests_result_list = []
        for item in tests_result:
            tests_result_list.append(item.name)
        result = Database.get_all_cty("top")
        self.assertListEqual(result, tests_result_list)
    def test_get_cty_numbers(self):
        tests_result = self.__session__.query(Top).all()
        tests_result_dict = {}
        for item in tests_result:
            tests_result_dict.update({item.name: item.number})
        results = Database.get_all_cty("top")
        self.assertListEqual(results, tests_result_list)

if __name__ == '__main__':
    unittest.main()



