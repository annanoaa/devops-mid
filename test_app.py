import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_submit_route(self):
        test_data = {
            'name': 'Test User',
            'message': 'This is a test message'
        }
        response = self.client.post('/submit', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test User', response.data)
        self.assertIn(b'This is a test message', response.data)

if __name__ == '__main__':
    unittest.main() 