from flask import Flask, jsonify, send_from_directory

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
    # ➔ Hier kannst du später weitere Kategorien ergänzen
]

# API-Route: Hole nächste Kategorie
@app.route('/next_category/<int:category_id>', methods=['GET'])
def next_category(category_id):
    if 1 <= category_id <= len(categories):
        return jsonify(categories[category_id - 1])
    else:
        return jsonify({"error": "Kategorie nicht gefunden"}), 404

# NEU: Route für ai-plugin.json
@app.route('/.well-known/ai-plugin.json')
def serve_manifest():
    return send_from_directory('.', 'ai-plugin.json', mimetype='application/json')

# NEU: Route für openapi.yaml
@app.route('/openapi.yaml')
def serve_openapi():
    return send_from_directory('.', 'openapi.yaml', mimetype='application/yaml')

# Start der App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
