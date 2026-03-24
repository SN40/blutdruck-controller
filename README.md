# 🩸 Blutdruck-Controller

Eine Flask-Anwendung zum Sammeln und Verwalten von Blutdruckwerten mit SQLAlchemy.

## Features

- ✅ Blutdruckwerte erfassen (Systolisch, Diastolisch, Puls)
- ✅ Notizen hinzufügen
- ✅ Alle Werte anzeigen
- ✅ Werte löschen
- ✅ REST API für externe Integrations
- ✅ SQLite Datenbank

## Installation

```bash
# Repository klonen
git clone https://github.com/SN40/blutdruck-controller
cd blutdruck-controller

# Virtuelle Umgebung erstellen
python -m venv venv

# Virtuelle Umgebung aktivieren
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Dependencies installieren
pip install -r requirements.txt
```

## Verwendung

```bash
# Flask App starten
python app.py
```

Die App läuft dann auf **http://localhost:5000**

## API Endpoints

### GET /api/werte
Alle Blutdruckwerte abrufen

### POST /api/wert
Neuen Blutdruckwert hinzufügen

**Request Body:**
```json
{
  "systolisch": 120,
  "diastolisch": 80,
  "puls": 72,
  "notizen": "Nach dem Sport"
}
```

### DELETE /api/wert/<id>
Wert mit ID löschen

## Projektstruktur

```
blutdruck-controller/
├── app.py              # Hauptanwendung
├── requirements.txt    # Python Dependencies
├── .gitignore         # Git ignore Datei
├── README.md          # Diese Datei
├── templates/         # HTML Templates
│   └── index.html     # Startseite
└── blutdruck.db       # SQLite Datenbank (wird auto-erstellt)
```

## Technologien

- **Flask** - Web Framework
- **SQLAlchemy** - ORM
- **SQLite** - Datenbank

## Lizenz

MIT
