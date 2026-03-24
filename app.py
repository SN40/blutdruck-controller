from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# SQLAlchemy Konfiguration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blutdruck.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Datenbankmodell für Blutdruck-Werte
class BlutdruckWert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    systolisch = db.Column(db.Integer, nullable=False)
    diastolisch = db.Column(db.Integer, nullable=False)
    puls = db.Column(db.Integer)
    notizen = db.Column(db.String(255))
    erstellt_am = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'systolisch': self.systolisch,
            'diastolisch': self.diastolisch,
            'puls': self.puls,
            'notizen': self.notizen,
            'erstellt_am': self.erstellt_am.strftime('%Y-%m-%d %H:%M:%S')
        }

# Startseite
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'status': 'Blutdruck-Controller läuft',
        'version': '1.0',
        'endpoints': {
            'GET /': 'Startseite',
            'POST /api/blutdruck': 'Neuen Blutdruck-Wert speichern',
            'GET /api/blutdruck': 'Alle Blutdruck-Werte abrufen',
            'GET /api/blutdruck/<id>': 'Einzelnen Wert abrufen',
            'DELETE /api/blutdruck/<id>': 'Wert löschen'
        }
    })

# Neuen Blutdruck-Wert speichern
@app.route('/api/blutdruck', methods=['POST'])
def add_blutdruck():
    data = request.get_json()
    
    if not data or 'systolisch' not in data or 'diastolisch' not in data:
        return jsonify({'fehler': 'systolisch und diastolisch sind erforderlich'}), 400
    
    try:
        wert = BlutdruckWert(
            systolisch=data['systolisch'],
            diastolisch=data['diastolisch'],
            puls=data.get('puls'),
            notizen=data.get('notizen')
        )
        db.session.add(wert)
        db.session.commit()
        return jsonify(wert.to_dict()), 201
    except Exception as e:
        return jsonify({'fehler': str(e)}), 500

# Alle Blutdruck-Werte abrufen
@app.route('/api/blutdruck', methods=['GET'])
def get_blutdruck():
    werte = BlutdruckWert.query.all()
    return jsonify([wert.to_dict() for wert in werte]), 200

# Einzelnen Wert abrufen
@app.route('/api/blutdruck/<int:id>', methods=['GET'])
def get_blutdruck_by_id(id):
    wert = BlutdruckWert.query.get(id)
    if not wert:
        return jsonify({'fehler': 'Wert nicht gefunden'}), 404
    return jsonify(wert.to_dict()), 200

# Wert löschen
@app.route('/api/blutdruck/<int:id>', methods=['DELETE'])
def delete_blutdruck(id):
    wert = BlutdruckWert.query.get(id)
    if not wert:
        return jsonify({'fehler': 'Wert nicht gefunden'}), 404
    
    db.session.delete(wert)
    db.session.commit()
    return jsonify({'nachricht': 'Wert gelöscht'}), 200

# Datenbankinitialisierung
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)