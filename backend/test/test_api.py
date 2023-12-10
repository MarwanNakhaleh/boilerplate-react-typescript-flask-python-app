import json
import os, sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import make_response

from app import create_app
from api.constants import listings_args_list

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app.app_context().push()
       
    # this doesn't work on Windows     
    def tearDown(self):
        self.app = None
    
    def test_correct_results_from_base_endpoint(self):
        response = make_response(self.app.test_client().get('/api/v1/listings')).data
        json_response = json.loads(response)
        
        num_results = json_response["num_results"]
        self.assertEqual(1, num_results)
        
        query = json_response["metadata"]["query"]
        for arg in listings_args_list:
            self.assertEqual(None, query[arg])
            
        data = json_response["results"][0]
        self.assertEqual(2, data["bathrooms"])
        self.assertEqual(3, data["bedrooms"])
        self.assertEqual(2000, data["square_feet"])
        self.assertEqual("Austin", data["city"])
        self.assertEqual("TX", data["state"])

if __name__ == '__main__':
    unittest.main()
    