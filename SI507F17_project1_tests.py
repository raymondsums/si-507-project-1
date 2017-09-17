## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

class Function_Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_constructor_1(self):
        self.assertEqual(Card().suit_names,['Diamonds','Clubs','Hearts','Spades'],'testing that suit_names contains a list of strings that represent suits')
        #no one should ever put in a number that is an invalid suit (less than zero or greater than 3)

    def test_constructor_2(self):
        list = []
        for i in range(1,14):
            list.append(i)
        self.assertEqual((Card().rank_levels),list,'testing that rank_levels contain a list of integer from 1 to 13')
        #no one should put an invalid rank (less than zero or greater than 13)

    def test_constructor_3(self):
        dict={1:'Ace',11:'Jack',12:'Queen',13:'King'}
        self.assertEqual((Card().faces),dict,'testing that the values in the card matches the dictionary keys assigned')

    def test_constructor_4(self):
        run1 = Card(suit,rank)
        self.assertEqual(type(suit),int,'testing that the values for the input suits are integers')
        self.assertEqual(type(rank),int,'testing that the values for the input ranks are integers')

    def test_pop_card(self):
    	self.assertEqual((Deck().pop_card,Deck(3,13),'testing the last card in the deck is 13 of Spades')

unittest.main(verbosity=2)

#
#    def test_constructor_4(self):
#        self.assertEqual(Card())
#
#    def test_constructor_1(self):
#        for i in range(0,3):
#            self.assertRaises(Card(i,rank))
#        self.assertEqual(Card(suit,rank),4,"testing that the constructor accepts only two numbers")

#    def test_constructor_4(self):
        #testing that the input is int and not a string or a float

#    def test_deck(self):
#        self.assertEqual(list(Deck(),52,'testing that there are 52 multi-lines printed for Deck'))

#    def test_show_song(self):
#        self.assertEqual(show_song(),'')
        #testing that the show_song takes a string as an input

#    def test_show_song_2(self):
        #testing that the show_song function returns the type list

#    def test_play_war_game(self):
#        test_result = play_war_game(True)
#        print test_result
        #change default value to testing=TRUE to test this