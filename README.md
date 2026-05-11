# Microscope Specimen Size Calculator

This project implements the five-phase assignment:

- Core CLI calculator (Python)
- SQLite database integration
- Python GUI (tkinter) saved in `gui_py/` (kept for marking)
- Web GUI (Flask) in `web_app/`
- Deployment notes for free hosting

Files created:

- `src/cli.py` — command-line program
- `src/db.py` — shared SQLite helper used by CLI and GUI
- `gui_py/app_gui.py` — Python (tkinter) GUI (kept for marking)
- `web_app/app.py` — Flask web application
- `web_app/templates/` — templates for the web app
- `requirements.txt` — Python deps

Quick run (create a virtualenv first):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run CLI:

```bash
python -m src.cli
```

Run Python GUI (kept in project folder for marking):

```bash
python gui_py/app_gui.py
```

Run Web App:

```bash
python web_app/app.py
```

Deployment notes:

- The app is a plain Flask app and can be deployed to free platforms like Render, Railway, or Fly. Ensure the `uploads/` folder (in `web_app/`) is writable and that the SQLite DB is persisted.
# CSC442-II
