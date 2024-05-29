import unittest
from collisions import count_collisions

class TestCountCollisions(unittest.TestCase):
    
    def test_cases(self):
        self.assertEqual(count_collisions('LR'), '0 0')
        self.assertEqual(count_collisions('RL'), '1 1')
        self.assertEqual(count_collisions('RRR'), '0 0 0')
        self.assertEqual(count_collisions('RRL'), '1 2 1')
if __name__ == '__main__':
    unittest.main()
