from DeckOfCardsAPITesting.Infra.api_wrapper import APIWrapper
from DeckOfCardsAPITesting.Infra.Utils import Utils

class DeckOfCards:

    PATH = "https://deckofcardsapi.com/api/deck/"
    DECK_ID = "2697xce8viqq"
    picked_cards = []

    def __init__(self,api_object):
        self.api = api_object
        self.utils = Utils()


    def get_new_deck(self,deck_count = 1):
        my_api = APIWrapper()
        deck_count_req_var = "?deck_count="+str(deck_count)
        result = my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/new/shuffle/'+deck_count_req_var)
        ret_json = result.json()
        deck_id = ret_json["deck_id"]
        DeckOfCards.DECK_ID = deck_id
        return result


    def draw_a_card(self, deck_id, count = 1):
        my_api = APIWrapper()
        count_req_var = str(count)
        path = self.PATH + deck_id + "/draw/?count=" + count_req_var
        result = my_api.api_get_request(path)
        ret_json = result.json()
        card = ret_json["cards"]
        card_code = card[0]["code"]
        print("Card Drawn is: " + card_code)
        DeckOfCards.picked_cards.append(card_code)
        return result


    def add_to_piles(self, deck_id ,name):
        my_api = APIWrapper()
        draw_card_result = self.draw_a_card(deck_id)
        draw_card_result_json = draw_card_result.json()
        cards = draw_card_result_json["cards"]
        card = cards[0]
        card = card["code"]

        path = self.PATH + deck_id + "/pile/" + name + "/add/?cards=" + card
        result = my_api.api_get_request(path)
        ret_json = result.json()
        return result


    def list_cards_in_pile(self, deck_id ,pile_name):
        my_api = APIWrapper()
        path = self.PATH + deck_id + "/pile/" + pile_name + "/list/"
        result = my_api.api_get_request(path)
        ret_json = result.json()
        return result


    def shuffle_pile(self,deck_id ,pile_name):
        my_api = APIWrapper()
        path = self.PATH + deck_id + "/pile/" + pile_name + "/shuffle/"
        result = my_api.api_get_request(path)
        ret_json = result.json()
        print(ret_json)
        return result

    def black_jack(self,deck_id):
        # first Card
        print("Player 1 Draws Card")
        self.player_one = self.add_to_piles(deck_id, "Player1")
        print("Dealer Draws Card")
        self.dealer = self.add_to_piles(deck_id, "Dealer")
        self.player_one_list = self.list_cards_in_pile(deck_id, "Player1")
        self.dealer_list =self.list_cards_in_pile(deck_id, "Dealer")

        # second Card
        print("Player 1 Draws Card")
        self.player_one = self.add_to_piles(deck_id, "Player1")
        self.player_one_list = self.list_cards_in_pile(deck_id, "Player1")

        self.player_hand = self.utils.calc_player_hand(self.player_one_list, "Player1")
        print(self.player_hand)

        # player decision
        self.player_decision = self.utils.player_decision(self.player_hand, self, deck_id, "Player1")
        print("Player Decision: " + str(self.player_decision))

        self.player_hand = self.utils.calc_player_hand(self.player_one_list, "Player1")
        print("Player Hand: " + str(self.player_hand))

        # check game
        print("Dealer Draws Card")
        self.dealer = self.add_to_piles(deck_id, "Dealer")
        self.dealer_list = self.list_cards_in_pile(deck_id, "Dealer")

        self.dealer_hand = self.utils.calc_player_hand(self.dealer_list, "Dealer")
        print("Dealer Hand: " + str(self.dealer_hand))

        # player decision
        self.dealer_decision = self.utils.player_decision(self.dealer_hand, self, deck_id, "Dealer")
        print("Dealer Decision: " + str(self.dealer_decision))

        # check for Winner
        winner = self.utils.check_winner(self.player_decision, self.dealer_decision)
        return winner





