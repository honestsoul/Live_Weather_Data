import sys
sys.path.append("live_weather")
from live_weather  import app
import unittest 

class FlaskLiveWeatherTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the response data
        self.assertTrue(result.data)

if __name__ == '__main__':
  unittest.main()