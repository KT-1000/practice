import unittest


def get_max_profit(stock_prices):
    """Calculates the best profit that could have made from 1 purchase and 1 sale of 1 stock, with no shorting allowed

    Args:
        stock_prices: list of stock prices in chronological order such that stock_prices[minutes_past_open] = price
            ex. if the stock cost $500 at 10:30am (60 minutes past opening), stock_prices_yesterday[60] = 500

    Returns:
        max_profit: int describing the best possible profit, provided purchase came before sale

    Raises:
        ValueError if there are fewer than two prices in the stock_prices list

    Complexity: O(n) time and O(1) space
    """
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_time in xrange(1, len(stock_prices)):
        current_price = stock_prices[current_time]
        potential_profit = current_price - min_price
        max_profit = max(potential_profit, max_profit)
        min_price = min(min_price, current_price)

    return max_profit


class Test(unittest.TestCase):
    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([])


unittest.main(verbosity=2)
