import json

from flask import jsonify, request
from flask.blueprints import Blueprint
from flask_cors import cross_origin

from .constants import (
    listings_args_list, 
    contacts_args_list, 
    listings_endpoint, 
    contacts_endpoint, 
    transactions_args_list, 
    transactions_endpoint,
    bar_graph_endpoint,
    bar_graph_args_list,
    team_endpoint,
    team_args_list,
    geography_endpoint,
    geography_args_list
)
from .data import get_data

healthcheck = Blueprint('healthcheck', __name__)

listings = Blueprint('listings', __name__)
contacts = Blueprint('contacts', __name__)
transactions = Blueprint('transactions', __name__)
bar_graph = Blueprint('bar_graph', __name__)
team = Blueprint('team', __name__)
geography = Blueprint('geography', __name__)

@contacts.route(contacts_endpoint, methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_contacts():
    args = {}
    try:
        for key in contacts_args_list:
            args[key] = request.args.get(key)

        contacts = get_data("api/mockdata/contacts.json")
        results = json_response(args, contacts_endpoint, contacts)
        resp = api_response(results, contacts_endpoint, args["start"], args["limit"])
    except Exception as e:
        results = {
            "error": str(e)
        }
        resp = api_response(results, contacts_endpoint, None, None, 400)
    return resp

@transactions.route(transactions_endpoint, methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_transactions():
    args = {}
    try:
        for key in transactions_args_list:
            args[key] = request.args.get(key)

        transactions = get_data("api/mockdata/transactions.json")
        results = json_response(args, transactions_endpoint, transactions)
        resp = api_response(results, transactions_endpoint, args["start"], args["limit"])
    except Exception as e:
        results = {
            "error": str(e)
        }
        resp = api_response(results, transactions_endpoint, None, None, 400)
    return resp

@listings.route(listings_endpoint, methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_listings():
    args = {}
    try:
        for key in listings_args_list:
            args[key] = request.args.get(key)


        results = json_response(args, listings_endpoint, [
            {
                "city": "Austin",
                "state": "TX",
                "bedrooms": 3,
                "bathrooms": 2,
                "square_feet": 2000
            }
        ])
        resp = api_response(results, listings_endpoint, args["start"], args["limit"])
    except Exception as e:
        results = {
            "error": str(e)
        }
        resp = api_response(results, listings_endpoint, None, None, 400)
    return resp

@bar_graph.route(bar_graph_endpoint, methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_bar_graph():
    args = {}
    try:
        for key in bar_graph_args_list:
            args[key] = request.args.get(key)

        bar_graph = get_data("api/mockdata/bar_graph.json")
        results = json_response(args, bar_graph_endpoint, bar_graph)
        resp = api_response(results, bar_graph_endpoint, args["start"], args["limit"])
    except Exception as e:
        results = {
            "error": str(e)
        }
        resp = api_response(results, bar_graph_endpoint, None, None, 400)
    return resp

@geography.route(geography_endpoint, methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_geography():
    args = {}
    try:
        for key in geography_args_list:
            args[key] = request.args.get(key)

        geography = get_data("api/mockdata/geography.json")
        results = json_response(args, geography_endpoint, geography)
        resp = api_response(results, geography_endpoint, args["start"], args["limit"])
    except Exception as e:
        results = {
            "error": str(e)
        }
        resp = api_response(results, geography_endpoint, None, None, 400)
    return resp

@team.route(team_endpoint, methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_team():
    args = {}
    try:
        for key in team_args_list:
            args[key] = request.args.get(key)

        team = get_data("api/mockdata/team.json")
        results = json_response(args, team_endpoint, team)
        resp = api_response(results, team_endpoint, args["start"], args["limit"])
    except Exception as e:
        print(e)
        results = {
            "error": "invalid arguments entered"
        }
        resp = api_response(results, team_endpoint, None, None, 400)
    return resp


@healthcheck.route('/', methods=["GET"])
def get():
    return jsonify(
        {
            "status": "UP"
        }
    )

def api_response(payload, endpoint, start=None, limit=None, status=200):
    if start and limit:
        payload = get_paginated_list(payload, endpoint, start, limit)
    return (payload, status, {'content-type': 'application/json'})

def json_response(args: str, path: str, data: list):
    payload =  {
        "metadata": {
            "path": path,
            "query": args
        },
        "num_results": len(data),
        "results": data
    }
    return jsonify(payload)


# adapted slightly from Stack Overflow
def get_paginated_list(results, url, start, limit):
    count = len(results["results"])
    if count < start or limit < 0:
        return results
    
    paginated_response = {}
    paginated_response['start'] = start
    paginated_response['limit'] = limit
    paginated_response['num_results'] = count
    paginated_response["metadata"] = results["metadata"]
    
    # starting from 1 for results insteaf of 0 for programming
    if start == 1:
        paginated_response['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        paginated_response['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    
    if start + limit > count:
        paginated_response['next'] = ''
    else:
        start_copy = start + limit
        paginated_response['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    
    paginated_response['results'] = results["results"][(start - 1):(start - 1 + limit)]
    return paginated_response
