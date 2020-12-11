import unittest

# 实现加法的方法
def add(x,y):
    return x + y

class TestAdd(unittest.TestCase):


    # def test_add_01(self):
    #     res1 = add(1,1)
    #     self.assertEqual(2,res1)
    #
    #
    # def test_add_02(self):
    #     res2 = add(1,0)
    #     self.assertEqual(1,res2)
    #
    # def test_add_03(self):
    #     res3 = add(-1,2)
    #     self.assertEqual(1,res3)


    def test_add(self):
        test_data = [(1,1,2),(1,0,1),(-1,2,1),(0,0,0)]
        for x,y,expect_value in test_data:
            res = add(x,y)
            self.assertEqual(res,expect_value)


if __name__ == '__main__':
    unittest.main()