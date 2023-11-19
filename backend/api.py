from flask import Flask, request, jsonify
import requests
import uuid

app = Flask(__name__)
MLS_API_URL = "https://mockmlsapi.com/houses"  # this is a placeholder URL
MLS_API_KEY = "MY_MLS_API_KEY"

@app.route('/get_houses', methods=['GET'])
def get_houses():
    print("request")
    is_test = request.args.get('is_test')
    city = request.args.get('city')
    state = request.args.get('state')
    bedrooms = request.args.get('bedrooms')
    bathrooms = request.args.get('bathrooms')
    square_feet = request.args.get('square_feet')

    if not is_test:
        # Mocking the call to the MLS API
        response = requests.get(
            MLS_API_URL,
            headers={"Authorization": f"Bearer {MLS_API_KEY}"},
            params={
                "city": city,
                "state": state,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "square_feet": square_feet
            }
        )
        
        houses = response.json()

        # Add a custom UUID4 to each house object
        for house in houses:
            house["uuid"] = str(uuid.uuid4())

        return jsonify(houses)
    return jsonify([
        {
            "city": "Austin",
            "state": "TX",
            "bedrooms": 3,
            "bathrooms": 2,
            "square_feet": 2000
        }
    ])

if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0", debug=True)
