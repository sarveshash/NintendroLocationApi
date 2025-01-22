from flask import Flask, jsonify, request

app = Flask(__name__)

locations = {
  "locations": {
    "kanto": {
      "pallet_town": {},
      "route_1": {
        "rattata": {
          "level": "3-4",
          "spawn_rate": 30
        },
        "oddish": {
          "level": "3-4",
          "spawn_rate": 30
        },
        "pidgey": {
          "level": "3-4",
          "spawn_rate": 40
        },
        "bellsprout": {
          "level": "3-4",
          "spawn_rate": 30
        },
        "dragonite": {
          "level": "3-56",
          "spawn_rate": 5
        },
        "charizard": {
          "level": "3-56",
          "spawn_rate": 5
        },
        "moltres": {
          "level": "3-56",
          "spawn_rate": 1
        },
        "articuno": {
          "level": "3-56",
          "spawn_rate": 1
        },
        "zapdos": {
          "level": "3-56",
          "spawn_rate": 1
        },
      }
    }
  }
}

# Define a route to return the full data
@app.route('/locations', methods=['GET'])
def get_all_locations():
    return jsonify(locations)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
