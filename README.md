# Deck of Cards API Testing

This repository contains a set of Python tests for the [Deck of Cards API](https://deckofcardsapi.com/). The tests are implemented using the `unittest` framework and include API calls to verify various functionalities provided by the Deck of Cards API.

## Getting Started

Before running the tests, make sure you have the required dependencies installed. You can install them using the following command:

```bash
pip install requests
```

## Tests Overview

### `MainTest` Class

#### `setUp` Method
This method initializes the API wrapper and utility functions before each test case.

#### `deck_init` Method
This method initializes a new deck and returns the deck ID.

#### `test_check_status_code_shuffle` Method
Verifies that a new deck is shuffled successfully.

#### `test_check_draw_card` Method
Verifies the functionality of drawing a specified number of cards from a deck.

#### `test_add_to_piles` Method
Verifies the addition of cards to a pile.

#### `test_list_pile_cards` Method
Verifies listing cards in a specified pile.

#### `test_shuffle_pile_cards` Method
Verifies shuffling cards in a specified pile.

#### `test_play_blackjack` Method
Verifies the blackjack game functionality.

## Additional Notes

- The tests utilize the `APIWrapper` and `Utils` classes to interact with the Deck of Cards API and perform utility functions.
- Ensure that the Deck of Cards API is accessible and responsive before running the tests.
- Update the API base URL in the code if there are any changes to the API endpoint.

Feel free to explore and modify the test cases based on your requirements. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

Happy testing!
