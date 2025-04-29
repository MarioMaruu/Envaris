from flask import Flask, jsonify

app = Flask(__name__)

# Kategorien und Fragen vordefinieren
categories = [
    {
        "id": 1,
        "name": "Kognitive Strukturen",
        "questions": [
            "Wie würdest du deine typische Denkweise beschreiben?",
            "Worauf liegt meistens dein Fokus beim Denken oder Handeln?",
            "Wie gehst du mit eigenen Fehlern um?"
        ]
    },
    {
        "id": 2,
        "name": "Emotionale Dynamik",
        "questions": [
            "Wie gut kannst du deine Emotionen steuern?",
            "Wie stabil empfindest du deine Gefühle über Zeit hinweg?",
            "Wie stark ist deine Fähigkeit, dich in andere einzufühlen?"
        ]
    }
    # ➔ Hier kannst du später noch die anderen 30 Kategorien hinzufügen
]

# API-Route: Hole nächste Kategorie
@app.route('/next_category/<int:category_id>', methods=['GET'])
def next_category(category_id):
    if 1 <= category_id <= len(categories):
        return jsonify(categories[category_id - 1])
    else:
        return jsonify({"error": "Kategorie nicht gefunden"}), 404

# Starte die App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
