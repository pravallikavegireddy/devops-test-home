import unittest

import webapp


class WebappTestCase(unittest.TestCase):

    def setUp(self):
        self.app = webapp.app.test_client()


if __name__ == '__main__':
    unittest.main()
