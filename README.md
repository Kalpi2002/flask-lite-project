# flask-lite-project
## 📌 Project Summary

This is a beginner-friendly group project to implement a Lite CRUD system using Flask, SQLAlchemy, and SQLite.
The project includes a single core entity with full CRUD functionality, simple validation, and a basic search/filter option.
## 👥 Team Members

- K.E.Kumarasinghe (Team Lead) - ASP/2022/149
- R.M.C.N. Abeyvickrama - ASP/2022/152
- Monali Dissanayake - ASB/2022/169
- P.N. Wickramarathna - ASP/2022/137
- W.D.N.O.Wanniarachchi - ASP/2022/142

  Instructor GitHub: akalanka-h
## ⚙️ Tech Stack
- Python 3.x
- Flask
- SQLAlchemy (SQLite)
- Jinja2 Templates
- Bootstrap (via CDN)
  
## 🚀 Setup & Run

1.  **Clone the repository**
    ```bash
    git clone https://github.com/KushanLakshitha/Flask-Lite-Group-Project
    cd Flask-Lite-Group-Project
    ```

2.  **Create and activate a virtual environment**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    # python -m venv venv
    # .\venv\Scripts\activate
    ```

3.  **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize and seed the database**
    Run the seed script to create the `tasks.db` file and populate it with sample data.
    ```bash
    python seed.py
    ```

5.  **Run the application**
    This will start the Flask development server.
    ```bash
    python app.py
    ```
    The application will be running at `http://127.0.0.1:5000`.

## 📈 Progress Log

**Sep 2**
-   Repo created
-   Members added
-   Base Flask app runs
-   Defined the database schema with a `Task` model (`models.py`).
-   Configured the Flask app to connect to a SQLite database (`app.py`).
-   Created a seed script to populate the database with sample data (`seed.py`).
-   Implemented a basic route (`/tasks`) to fetch and display all tasks from the database.
