### README

Using unit tests to test the card sorting and war game program.
I wrote ten tests in total including some stress case tests.

The first four tests are constructor tests, that tests that the suit value is within the range of 0-3 and that it returns a string value, the second test is to test the rank value to be within the range 1-13 and if it returns an int value, testing that the values in the card matches the dictionary keys assigned and testing that the rank levels are similar to what is described in the code description.

The following two tests are to test play_war_game, to test the outputs that it is both a tuple and contain a string and two integers.

Next, there is a test to test the deck method if it contains 52 cards in total. The test_deal_hand test will determine if the deck will pop the first card in an unshuffled deck.

Lastly, the test_show_song will test that the input for show_song can only be a string. And if an error is raised, there will be an exception for the error within the test case.
