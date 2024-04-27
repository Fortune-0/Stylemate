#!/usr/bin/python3
#Test the Database class
from models.bottom import Bottom
from models.top import Top
from models.user import User
from sqlalchemy import create_engine, insert, update
from sqlalchemy.orm import sessionmaker
import unittest
from utils.database import Database

class TestDatabaseClass(unittest.TestCase):
    """Test the Database Class and its methods"""

    def setUp(self):
        """Create an instance of Database"""
        self.database = Database('anomalie', 'Ola')
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
        self.assertListEqual(return_result, [input_dict['name'], input_dict['number']])
    def test_get_all_cty(self):
        """Test get_all_cty Database instance method"""
        tests_result = self.__session__.query(Top).all()
        tests_result_list = []
        for item in tests_result:
            tests_result_list.append(item.name)
        result = self.database.get_all_cty("tops")
        self.assertListEqual(result, tests_result_list)
    def test_get_cty_numbers(self):
        """Test get_cty_numbers Database instance method"""
        tests_result = self.__session__.query(Top).all()
        tests_result_dict = {}
        for item in tests_result:
            tests_result_dict.update({item.name: item.number})
        results = self.database.get_cty_numbers("tops")
        self.assertDictEqual(results, tests_result_dict)
    def test_get_user_sex(self):
        self.__session__.execute(
            update(User),
            [{'name': 'Uvere Amarachi', 'age': 20, 'sex': 'Female'}]
        )
        self.__session__.commit()
        test_result = self.__session__.query(User).first().sex
        result = self.database.get_user_sex()
        self.assertEqual(test_result, result)
    def test_get_user_name(self):
        """Test get_user_name Database instance method"""
        test_result = self.__session__.query(User).first().name
        result = self.database.get_user_name()
        self.assertEqual(test_result, result)
    def test_get_cty(self):
        """Test get_cty Database instance method"""
        test_result = self.__session__.query(Bottom)\
                      .filter_by(name = "jean trousers").first()
        if test_result is None:
            test_result_dict = {}
        else:
            test_result_dict = {test_result.name: test_result.number}
        result = self.database.get_cty("jean trousers")
        self.assertDictEqual(result, test_result_dict)




if __name__ == '__main__':
    unittest.main()



