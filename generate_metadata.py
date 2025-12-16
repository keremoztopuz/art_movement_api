import os
import json

DATA_DIR = "/Users/keremoztopuz/Desktop/art_movement_deep_learning_project/Images/resized_wikiart"

artworks = []

for movement in os.listdir(DATA_DIR):
    movement_path = os.path.join(DATA_DIR, movement)
    if os.path.isdir(movement_path):
        for filename in os.listdir(movement_path):
            if filename.endswith(".jpg"):
                parts = filename.replace(".jpg", "").split("_")
                artist = parts[0].replace("-", " ")
                title = parts[1].replace("-", " ").title() if len(parts) > 1 else "Unknown"
    
                artworks.append({
                    "id": len(artworks) + 1,
                    "filename": filename,
                    "artist": artist,
                    "title": title,
                    "movement": movement,
                })

with open("artworks.json", "w") as f:
    json.dump(artworks, f, indent=2, ensure_ascii=False)

print(f"Total artworks: {len(artworks)}")