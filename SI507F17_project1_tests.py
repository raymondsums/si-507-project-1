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
        Card1 = Card(-1)
        self.assertNotIsInstance(Card1.suit, str, 'testing that if a suit value input outside of the range 0-3 returns a string value')

    def test_constructor_2(self):
        Card2 = Card(0,15)
        self.assertNotIsInstance(Card2.rank,int,'testing that if a rank value outside of the range 1-13 and if it returns an int value')

    def test_constructor_3(self):
        dict={1:'Ace',11:'Jack',12:'Queen',13:'King'}
        self.assertEqual((Card().faces),dict,'testing that the values in the card matches the dictionary keys assigned')

    def test_constructor_4(self):
        alist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.assertEqual((Card().rank_levels),alist,'testing that the rank levels are similar to what is described in the code description')

    def test_play_war_game(self):
        self.assertEqual(type(play_war_game('TRUE')),type(('String',1,3)),'testing that the output of play_war_game returns a tuple')
        
    def test_play_war_game_2(self):
        new_list = []
        for i in play_war_game('TRUE'):
            new_list.append(i)
        test_list = ['String',1,3]
        for i in range(len(new_list)):
            self.assertEqual(type(new_list[i]),type(test_list[i]),'testing that every element in the output of play_war_game matches the expected type')

    def test_deck(self):
        self.assertEqual((len(str(Deck()).split('\n'))),52,'testing that the deck has generated 52 cards in total')

    def test_pop_card(self):
        self.assertEqual(str(Deck().pop_card()),str(Card(3,13)),'testing that the popped card is the last card(card with highest value as assigned by the suit and rank) in an unshuffled deck')

    def test_deal_hand(self):
        self.assertEqual(str((Deck().deal_hand(1))[0]),str(Card(0,1)),'testing that deal_hand pops the first card in a unshuffled deck')

    def test_show_song(self):
        self.assertRaises(TypeError,show_song(0),'testing that the input for show_song can only be a string')
    
    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main(verbosity=2)