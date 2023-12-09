import os
import sys
sys.path.insert(0, os.getcwd())

api_prefix = '/api/v1'

origins = [
    "localhost", 
    "http://localhost:3000",
    "http://localhost:9002",
]

listings_args_list = [
    "min_bedrooms",
    "max_bedrooms",
    "min_bathrooms",
    "max_bathrooms",
    "min_price",
    "max_price",
    "start",
    "limit",
    "city",
    "state",
    "is_test"
]

contacts_args_list = [
    "start",
    "limit",
]

transactions_args_list = [
    "start",
    "limit",
]

bar_graph_args_list = [
    "start",
    "limit",
]

team_args_list = [
    "start",
    "limit",
]

geography_args_list = [
    "start",
    "limit",
]

listings_endpoint = "/listings"
contacts_endpoint = "/contacts"
transactions_endpoint = "/transactions"
bar_graph_endpoint = "/bar_graph"
team_endpoint = "/team"
geography_endpoint = "/geography"