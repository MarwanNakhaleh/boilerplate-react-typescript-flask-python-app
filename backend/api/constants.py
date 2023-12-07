import os
import sys
sys.path.insert(0, os.getcwd())

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

listings_endpoint = "/listings"
contacts_endpoint = "/contacts"
transactions_endpoint = "/transactions"