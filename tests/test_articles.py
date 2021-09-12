import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    """
    Test class to test the behavior of the News class.
    """
    def setUp(self):
        """
        set up method that will run before every Test.
        """
        self.current_news = News('A thrilling news api from python','')
    def test_instance(self):
        self.assertTrue(isinstance(self.current_news, News))
        
if __name__ == '__main__':
    unittest.main()