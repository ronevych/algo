import unittest
import os

class TestFindRootVertex(unittest.TestCase):

    def setUp(self):
        self.input_file = 'test_input.txt'
        with open(self.input_file, 'w') as file:
            file.write("1 2\n")
            file.write("2 3\n")
            file.write("3 4\n")
            file.write("4 1\n")

    def tearDown(self):
        os.remove(self.input_file)

    def test_find_root_vertex(self):
        from solution import find_root_vertex

        with open(self.input_file, 'r') as file:
            lines = file.readlines()
            max_vertex = max(max(map(int, line.strip().split()[:2])) for line in lines)
            graph = [[] for _ in range(max_vertex + 1)]

            for line in lines:
                values = list(map(int, line.strip().split()))
                if len(values) < 2:
                    continue
                u, v = values[:2]
                graph[u].append(v)

        root_vertex = find_root_vertex(graph)

        self.assertEqual(root_vertex, -1)

if __name__ == '__main__':
    unittest.main()
