import random

class Utils:


    def get_random_card(self):
        val = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 0, "J", "Q", "K"]
        suit = ["S","D","C","H"]

        card_val = random.choice(val)
        card_suit = random.choice(suit)
        card = str(card_suit)+str(card_val)
        print(card)
        return card

    def get_random_cards(self,amount = 1):
        cards = []
        while len(cards) < amount:
            picked = self.get_random_card()
            if picked not in cards:
                cards.append(picked)

        return self.get_cards_names_as_list(cards)

    def get_cards_names_as_list(self, cards):
        cards_str = ""
        for card in cards:
            cards_str = cards_str + card +","
        return cards_str

    def calc_player_hand(self,response,name):
        sum = 0
        special_cards = ["ACE","JACK","QUEEN","KING","0"]

        respone_json = response.json()
        player_cards = respone_json["piles"]
        player_cards = player_cards[name]
        player_cards = player_cards["cards"]

        for card in player_cards:
            val = card["value"]
            if val in special_cards:
                sum += 10
            else:
                sum += int(val)

        return sum

    def player_decision(self, hand, api_object, deck_id, pile_name):
        cont = True

        while cont:
            if hand < 16:
                # Draw Card
                print(pile_name+" Draws Card")
                api_object.add_to_piles(deck_id , pile_name)
                pile_list = api_object.list_cards_in_pile(deck_id, pile_name)

                hand = self.calc_player_hand(pile_list, pile_name)
                if hand > 21:
                    cont = False

            else:
                #Hold
                print(pile_name+" Holds")
                cont = False
        return hand


    def check_winner(self,player_hand,dealer_hand):
        print("Player Hand: " + str(player_hand))
        print("Dealer Hand: " + str(dealer_hand))
        if player_hand > 21:
            print("Player Lost, House Wins")
        elif dealer_hand > 21:
            print("Player Wins")
        elif dealer_hand == player_hand:
            print("Draw")
        elif player_hand > dealer_hand:
            print("Player Wins")
        else:
            print("Player Lost, House Wins")
        return True





if __name__ == "__main__":
    utils = Utils()
    cards = utils.get_random_cards(5)
    print(cards)
    print(utils.get_cards_names_as_list(cards))

