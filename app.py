from flask import Flask, jsonify, request 
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("artworks.json", "r", encoding="utf-8") as f:
    artworks = json.load(f)

with open("movements.json", "r", encoding="utf-8") as f:
    movements = json.load(f)

@app.route("/", methods = ["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Art Movement API!",
        "endpoints": [
            "/movement/<name>",
            "/movements",
            "/artworks",
            "/artworks/<movement>",
            "/artwork/<int:id>"
        ]
    })

@app.route("/movement/<name>", methods = ["GET"])
def get_movement_info(name):
    if name in movements:
        return jsonify(movements[name])
    else:
        return jsonify({"message": "Movement not found"}), 404

@app.route("/movements", methods = ["GET"])
def get_all_movements():
    return jsonify(movements)

@app.route("/artworks", methods = ["GET"])
def get_artworks():
    return jsonify(artworks)

@app.route("/artworks/<movement>", methods = ["GET"])
def get_by_movement(movement):
    filtered = [artwork for artwork in artworks if artwork["movement"] == movement]
    return jsonify(filtered)

@app.route("/artwork/<int:id>", methods = ["GET"])
def get_artwork(id):
    artwork = next((artwork for artwork in artworks if artwork["id"] == id), None)
    if artwork:
        return jsonify(artwork)
    else:
        return jsonify({"message": "Artwork not found"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)