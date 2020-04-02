#encoding=utf-8
import unittest
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(1,1)
        
    def test2(self):
        self.assertTrue(2==3)
       
    def test3(self):  #当我们要断言会出现某个异常时，可以用with self.assertRaises(异常类型)  来实现
        print('----演示:断言一定会出现异常---')
        with self.assertRaises(Exception):
            self.chufa()
    def chufa(self):
        return 1/0

if __name__=='__main__':
    unittest.main()
