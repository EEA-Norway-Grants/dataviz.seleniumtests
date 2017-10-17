import unittest
from functools import partial

from selenium.webdriver.support.ui import WebDriverWait

from edw.seleniumtesting.common import BrowserTestCase

import dataviz.seleniumtests.util as util


FINDER = util.ElementFinder()


def suite(browser, base_url, extra_args):
    """ Call on homepage: `seleniumtesting http://localhost/`
    """
    FINDER.set_browser(browser)

    test_suite = util.TestFactory(
        unittest.TestSuite(),
        browser=browser, base_url=base_url, extra_args=extra_args
    )

    test_suite.add_tests(Homepage)

    return test_suite()


def _to_int(val):
    return int(val.translate(str.maketrans('', '', '€')).replace(' ', ''))


def _get_amounts():
    return [elm.text.strip() for elm in FINDER.css('.info .amount', many=True)]


def _wait_for_amounts(browser):
    """ Returns the amounts if their length is 3.
        During animation there are more than 3 elements.
    """
    def _checker(arg):
        elems = _get_amounts()
        return elems if len(elems) == 3 else False

    return WebDriverWait(browser, 5).until(_checker)


def _amounts(browser):
    return sum(map(_to_int, _wait_for_amounts(browser)))


class Homepage(BrowserTestCase):

    def setUp(self):
        self.browser.get(self.url)

    def test_chart(self):
        """ Test main homepage chart
        """
        amounts = partial(_amounts, self.browser)

        initial = amounts()

        FINDER.css('svg g.item.eea-grants').click()

        self.assertTrue(amounts() < initial)

        FINDER.css('#reset-filters').click()

        self.assertTrue(amounts() == initial)
