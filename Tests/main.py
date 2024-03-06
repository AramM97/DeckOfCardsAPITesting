import unittest

from DeckOfCardsAPITesting.Infra.api_wrapper import APIWrapper
from DeckOfCardsAPITesting.Infra.Utils import Utils
from DeckOfCardsAPITesting.Logic.shuffle_endpoints import DeckOfCards


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.utils = Utils()

    def deck_init(self, api_logic):
        result = api_logic.get_new_deck()
        ret = result.json()
        deck_id = ret["deck_id"]
        return deck_id

    def test_check_status_code_shuffle(self):
        api_logic = DeckOfCards(self.my_api)
        result = api_logic.get_new_deck()
        ret = result.json()
        self.assertTrue(ret["shuffled"])

    def test_check_draw_card(self, amount=2):
        api_logic = DeckOfCards(self.my_api)
        deck_id = self.deck_init(api_logic)
        result = api_logic.draw_a_card(deck_id, amount)
        ret = result.json()
        drawn_cards_num = len(ret["cards"])
        self.assertEqual(drawn_cards_num, amount, "Drawn Wrong Amount")

    def test_add_to_piles(self):
        api_logic = DeckOfCards(self.my_api)
        deck_id = self.deck_init(api_logic)
        result = api_logic.add_to_piles(deck_id, "Player1")
        self.assertTrue(result.ok)

    def test_list_pile_cards(self):
        api_logic = DeckOfCards(self.my_api)
        deck_id = self.deck_init(api_logic)
        api_logic.add_to_piles(deck_id, "Player1")
        result = api_logic.list_cards_in_pile(deck_id, "Player1")
        res_json = result.json()
        self.assertLess(res_json["remaining"], 52 ,"No Cards Added to Pile")

    def test_shuffle_pile_cards(self):
        api_logic = DeckOfCards(self.my_api)
        deck_id = self.deck_init(api_logic)
        api_logic.add_to_piles(deck_id, "Player1")
        result = api_logic.shuffle_pile(deck_id, "Player1")
        self.assertTrue(result.ok)

    def test_play_blackjack(self):
        api_logic = DeckOfCards(self.my_api)
        deck_id = self.deck_init(api_logic)
        winner = api_logic.black_jack(deck_id)
        self.assertTrue(winner)

