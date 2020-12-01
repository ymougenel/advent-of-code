import unittest
import day11
from Direction import Direction
from Robot import Robot


class TestDay11(unittest.TestCase):

    # Test Painting
    def test_robots_paint(self):
        # Single digit instruction
        panel = day11.init_matrix(5, 5)
        robot = Robot(0, 0, Direction.LEFT)
        robot.paint(panel, 1)
        self.assertEqual(panel[0][0], 1)

    # Test Movement
    def test_robots_move(self):
        # Trigonometric rotation
        robot = Robot(1, 1, Direction.UP)
        robot.move(0)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 1)

        robot.move(0)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)

        robot.move(0)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 0)

        robot.move(0)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)

        # Clockwise rotation
        robot = Robot(1, 1, Direction.RIGHT)
        robot.move(1)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 0)

        robot.move(1)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)

        robot.move(1)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 1)

        robot.move(1)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)

if __name__ == '__main__':
    unittest.main()
