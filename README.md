<<<<<<< HEAD
Career Guidance Platform - Prototype

Prerequisites
- Python 3.11+

Setup (Windows PowerShell)
```
python -m venv .venv
./.venv/Scripts/Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000/docs for API docs.

Frontend (static)
- Open `web/index.html` in a browser (or serve with `python -m http.server 8080` and visit http://localhost:8080).

Notes
- SQLite database file is `app/data.db`. To reset, delete it and restart.

=======
# SIH-Hackathon
>>>>>>> 97495ad5193d67fdc3d35ed41b6ca3dbdef0de5a
