

class TestFactory(object):

    def __init__(self, suite, **kwargs):

        self.suite = suite
        self.params = kwargs

    def __call__(self):

        return self.suite

    def add_tests(self, test_class):
        for name in test_class.my_tests():
            self.suite.addTest(
                test_class(
                    name,
                    self.params["browser"],
                    self.params["base_url"],
                    self.params["extra_args"],
                    )
                )

class ElementFinder(object):

    browser = None

    @classmethod
    def set_browser(cls, browser):
        cls.browser = browser

    def css(self, selector, many=False):
        func = (
            self.browser.find_elements_by_css_selector if many
            else self.browser.find_element_by_css_selector
        )
        return func(selector)

    def name(self, name):
        return self.browser.find_element_by_name(name)

    def link(self, text):
        return self.browser.find_element_by_link_text(text)

    def xpath(self, selector):
        return self.browser.find_element_by_xpath(selector)
