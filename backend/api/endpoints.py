import json

from flask import jsonify, request
from flask.blueprints import Blueprint
from flask_cors import cross_origin

from constants import args_dict

listings = Blueprint('listings', __name__)

@listings.route('/listings', methods=["GET"])
@cross_origin(headers=['Content-Type'])
def get_listings():
    args = {}
    for key in args_dict:
        args[key] = request.args.get(key)

    results = json_response(args, "/listings", [
        {
            "city": "Austin",
            "state": "TX",
            "bedrooms": 3,
            "bathrooms": 2,
            "square_feet": 2000
        }
    ])
    resp = api_response(results, args["start"], args["limit"])
    # except Exception as e:
    #     print(e)
    #     results = {
    #         "error": "invalid arguments entered"
    #     }
    #     resp = api_response(results, None, None, 400)
    print(results)
    return resp

@listings.route('/', methods=["GET"])
def get():
    print("healthcheck")
    return jsonify(
        {
            "status": "UP"
        }
    )

def api_response(payload, start=None, limit=None, status=200):
    print("in api_response")
    if start and limit:
        payload = get_paginated_list(payload, '/listings', start, limit)
    return (payload, status, {'content-type': 'application/json'})

def json_response(args: str, path: str, data: list):
    print("in json_response")
    payload =  {
        "metadata": {
            "path": path,
            "query": args
        },
        "num_results": len(data),
        "results": data
    }
    print(json.dumps(payload))
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