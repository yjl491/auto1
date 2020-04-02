#encoding=utf8
import unittest
class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('测试类前执行')
    @classmethod
    def tearDownClass(cls):
        print('测试类后执行')
    
    def setUp(self):
        print('我要先登录')
    def tearDown(self):
        print('我要最后退出')
    
    def testAdd(self):
        self.assertEqual((1+2),3,'报错1')
        self.assertEqual((1+100),101,'报错2')
        
   
    def testChengFa(self):
        self.assertEqual((0*12),0,'报错3')
        self.assertEqual((4*12),48,'报错4')

if __name__=='__main__':
    unittest.main()