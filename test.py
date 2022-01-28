import unittest

from Tensor import getTensor

class TestTensor(unittest.TestCase):
    def test_trimming_data(self):
        """
        Test to check if the additional data is removed
        """
        arr = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1] 
        shape = [5, 2]
        intendedResult = [[0, 1], [2, 3], [4, 5], [0.1, 0.2], [-3, -2]]
        print("\nGiven data: ")
        print("list of data: ", arr)
        print("list of shape: ", shape)
        print("test result: ", intendedResult)
        res = getTensor(arr,shape)
        self.assertEqual(res, intendedResult)

    def test_padding_data(self):
        """
        Test to check if padding is applied to the data
        """
        arr = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
        shape = [2, 3, 2]
        intendedResult = [[[0, 1], [2, 3], [4, 5]], [[0.1, 0.2], [-3, 0], [0, 0]]]
        print("\nGiven data: ")
        print("list of data: ", arr)
        print("list of shape: ", shape)
        print("test result: ", intendedResult)
        res = getTensor(arr,shape)
        self.assertEqual(res, intendedResult)

    def test_empty_shape(self):
        """
        Test to check for empty shape array
        """
        arr = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1] 
        shape = []
        intendedResult = []
        print("\nGiven data: ")
        print("list of data: ", arr)
        print("list of shape: ", shape)
        print("test result: ", intendedResult)
        res = getTensor(arr,shape)
        self.assertEqual(res, intendedResult)

    def test_nonint_shape(self):
        """
        Test to check for the case where the shape array is not an integer
        """
        arr = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1] 
        shape = ["",5, 2]
        intendedResult = "Erroneous shape array!"
        print("\nGiven data: ")
        print("list of data: ", arr)
        print("list of shape: ", shape)
        print("test result: ", intendedResult)
        res = getTensor(arr,shape)
        self.assertEqual(res, intendedResult)


if __name__ == '__main__':
    unittest.main()
