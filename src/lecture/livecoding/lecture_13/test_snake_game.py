from unittest import TestCase

from lecture.livecoding.lecture_13.snake import SnakeGameBoard, Direction


class SnakeTest(TestCase):
    def test_game_init(self):
        b = SnakeGameBoard(5, 5, 3)
        # Test the initial location of the snake
        self.assertEqual(b.snake(), [(2, 2), (3, 2)])
        # We don't know where the apples are but there must be 3
        # TODO Check for valid apple positions (inside the board, don's overlap the snake, don't
        #  overlap each other)
        self.assertEqual(len(b.apples()), 3)
        self.assertEqual(b.direction, Direction.UP)

    def test_move_snake(self):
        b = SnakeGameBoard(5, 5, 3)
        # can't reverse the snake
        self.assertRaises(ValueError, b.move, Direction.DOWN, 1)

        for i in range(2):
            # TODO Check if there are any apples in the snake's path and if there are,
            # check that its length increased correctly
            # take the snake for a spin around the board
            b.move(Direction.RIGHT, 1)
            # check updated snake head
            self.assertEqual(b.snake()[0], (2, 3))
            b.move(Direction.DOWN, 1)
            self.assertEqual(b.snake()[0], (3, 3))
            b.move(Direction.LEFT, 1)
            self.assertEqual(b.snake()[0], (3, 2))
            b.move(Direction.UP, 1)
            self.assertEqual(b.snake()[0], (2, 2))
