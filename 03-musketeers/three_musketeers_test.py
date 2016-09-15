import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual((0, 4), string_to_location("A5"))

    def test_string_to_location_2(self):
        self.assertEqual((0, 4), string_to_location_2("A5"))
        self.assertEqual((1, 4), string_to_location_2("B5"))
        self.assertEqual((2, 4), string_to_location_2("C5"))
        self.assertEqual((3, 4), string_to_location_2("D5"))
        self.assertEqual((4, 4), string_to_location_2("E5"))
        self.assertEqual((0, 0), string_to_location_2("A1"))
        self.assertEqual((1, 1), string_to_location_2("B2"))
        self.assertEqual((2, 2), string_to_location_2("C3"))
        self.assertEqual((3, 3), string_to_location_2("D4"))
        self.assertEqual((4, 4), string_to_location_2("E5"))
        # don't let this one scare you.
        # it checks to make sure there is an error where we expect it to be. 
        # because of the complexity of this type of test, we have to call the 
        # assert in a different way
        #
        # assert "Raises" stands for "raises an exception" whihc in plain language
        # just means causes a critical error that would normally stop the program
        # (but since you called the function in this funny way, the computer was 
        # able to keep going ... if only all programs were this smart)
        self.assertRaises(AssertionError, string_to_location_2, "A0") 
        self.assertRaises(AssertionError, string_to_location_2, "F6")
        


    def test_location_to_string(self):
        self.assertEqual("A5", location_to_string((0, 4)))
        self.assertEqual("B5", location_to_string((1, 4)))
        self.assertEqual("C5", location_to_string((2, 4)))
        self.assertEqual("D5", location_to_string((3, 4)))
        self.assertEqual("E5", location_to_string((4, 4)))
        self.assertEqual("A1", location_to_string((0, 0)))
        self.assertEqual("B2", location_to_string((1, 1)))
        self.assertEqual("C3", location_to_string((2, 2)))
        self.assertEqual("D4", location_to_string((3, 3)))
        self.assertEqual("E5", location_to_string((4, 4)))

    """
    def test_at(self):
        self.fail() # Replace with tests

    def test_all_locations(self):
        self.fail() # Replace with tests

    def test_adjacent_location(self):
        self.fail() # Replace with tests
        
    def test_is_legal_move_by_musketeer(self):
        self.fail() # Replace with tests
        
    def test_is_legal_move_by_enemy(self):
        self.fail() # Replace with tests

    def test_is_legal_move(self):
        self.fail() # Replace with tests

    def test_can_move_piece_at(self):
        self.fail() # Replace with tests
        
    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        self.fail() # Put additional tests here

    def test_possible_moves_from(self):
        self.fail() # Replace with tests

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.fail() # Replace with tests

    def test_is_legal_location(self):
        self.fail() # Replace with tests

    def test_is_within_board(self):
        self.fail() # Replace with tests

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.fail() # Replace with tests
        
    def test_make_move(self):
        self.fail() # Replace with tests
        
    def test_choose_computer_move(self):
        self.fail() # Replace with tests; should work for both 'M' and 'R'

    def test_is_enemy_win(self):
        self.fail() # Replace with tests



    """

unittest.main()