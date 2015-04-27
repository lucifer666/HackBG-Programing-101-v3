from matrix_bombing import matrix_bombing_plan
import unittest

class TestMatrix(unittest.TestCase):

    def test_matrix_bombing_plan(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        result = matrix_bombing_plan(matrix)
        self.assertEqual(matrix_bombing_plan(matrix),result)

        matrix2 = [[1,2,3,4],[4,5,6,7],[7,8,9,10],[11,12,13,14]]
        result2 = matrix_bombing_plan(matrix2)
        self.assertEqual(matrix_bombing_plan(matrix2),result2)


if __name__ == "__main__":
    unittest.main()
