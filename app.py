from flask import Flask, jsonify, send_from_directory, Response

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

# Route für ai-plugin.json
@app.route('/.well-known/ai-plugin.json')
def serve_manifest():
    return send_from_directory('.', 'ai-plugin.json', mimetype='application/json')

# Route für openapi.yaml
@app.route('/openapi.yaml')
def serve_openapi():
    return send_from_directory('.', 'openapi.yaml', mimetype='application/yaml')

# ➡️ NEUE Routen für Privacy, Legal, Terms

@app.route('/privacy')
def privacy_policy():
    text = """
    Datenschutzerklärung:

    Dieses Plugin erhebt keine personenbezogenen Daten. Es verarbeitet lediglich Antworten auf gestellte Fragen lokal innerhalb der ChatGPT Umgebung. Keine Daten werden gespeichert oder an Dritte weitergegeben.

    Verantwortlicher: Envaris Plugin Entwickler
    Kontakt: deine-email@example.com
    """
    return Response(text, mimetype='text/plain')

@app.route('/legal')
def legal_info():
    text = """
    Impressum:

    Verantwortlich für den Inhalt:
    Envaris Plugin Entwickler
    Kontakt: deine-email@example.com
    Hinweis: Dieses Plugin ist ein persönliches Projekt und dient ausschließlich Test- und Demonstrationszwecken.
    """
    return Response(text, mimetype='text/plain')

@app.route('/terms')
def terms_of_service():
    text = """
    Nutzungsbedingungen:

    Durch die Nutzung dieses Plugins stimmen Sie zu, dass alle Eingaben freiwillig erfolgen. Der Entwickler übernimmt keine Haftung für Ergebnisse, Entscheidungen oder Interpretationen, die auf Basis der Plugin-Antworten getroffen werden.
    """
    return Response(text, mimetype='text/plain')

# Start der App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

