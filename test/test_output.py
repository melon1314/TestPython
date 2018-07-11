
import unittest
from data.InputData import input_data
from intersection.output import process_number


class OutPutTest(unittest.TestCase):  # 继承unittest.TestCase

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('testcase end')
        input_data.clear_model_list()

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('testcase start')
        # 初始化全局变量
        input_data.init_input_model_list()

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('test class end')
    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('test class start')

    def test_update_model_by_input_list(self):
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        model_list = input_data.get_model_list()
        self.assertEqual(len(input_list), len(model_list))
        self.assertEqual(3, model_list[0].raw_int)
        self.assertEqual(5, model_list[1].raw_int)
        self.assertEqual(7, model_list[2].raw_int)

    def test_process_number_01(self):
        number = 3
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('Fizz', result)

    def test_process_number_02(self):
        number = 10
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('Buzz', result)

    def test_process_number_03(self):
        number = 14
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('Whizz', result)

    def test_process_number_04(self):
        number = 15
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('FizzBuzz', result)

    def test_process_number_05(self):
        number = 30
        input_list = [2, 3, 5]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('FizzBuzzWhizz', result)

    def test_process_number_06(self):
        number = 30
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('Fizz', result)

    def test_process_number_07(self):
        number = 13
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('Fizz', result)

    def test_process_number_08(self):
        number = 17
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('17', result)

    def test_process_number_09(self):
        number = 11
        input_list = [3, 5, 7]
        input_data.update_model_by_input_list(input_list)
        result = process_number(number, input_data.model_list)
        self.assertTrue('11', result)


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
