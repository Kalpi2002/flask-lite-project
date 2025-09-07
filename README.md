# flask-lite-project

## 📌 Project Summary
This is a **Flask Lite CRUD application** for managing tasks.  
It allows users to **Create, Read, Update, Delete**, and **search/filter** tasks.  
The project is built using **Flask, SQLAlchemy, SQLite, Jinja2, and Bootstrap 5**.

## 👥 Team Members

- K.E.Kumarasinghe (Team Lead) - ASP/2022/149
- R.M.C.N. Abeyvickrama - ASP/2022/152
- G.A.M.A. Dissanayake - ASB/2022/169
- P.N. Wickramarathna - ASP/2022/137
- W.D.N.O.Wanniarachchi - ASP/2022/142

  Instructor GitHub: akalanka-h
  
## ⚙️ Tech Stack
- Python 3.x
- Flask
- SQLAlchemy (SQLite)
- Jinja2 Templates
- Bootstrap (via CDN)
  
## Features
- List all tasks in a responsive card layout  
- Search/filter tasks by title or description  
- Add new tasks with server-side validation  
- Edit existing tasks  
- Delete tasks with a confirmation page  
- Flash messages for success/error notifications  
- Database seeding with sample tasks  

## Project Structure
~~~
project_root/
├─ app.py # Flask app with routes
├─ models.py # SQLAlchemy Task model
├─ seed.py # Seed script to populate DB
├─ requirements.txt # Project dependencies
├─ README.md # This file
├─ .gitignore
├─ templates/
│ ├─ base.html
│ ├─ list.html
│ ├─ form.html
│ └─ delete_confirm.html
└─ static/ # Optional for CSS/JS
~~~
## 📸 Screenshots

### 🏠 Task List Page
![Task List](screenshots/task-list.png)

### ➕ Add Task Form
![Add Task](screenshots/add-task.png)

### 📝 Edit Task Form
![Edit Task](screenshots/edit-task.png)

### ❌ Delete Confirmation
![Delete Task](screenshots/delete-task.png)

## 🚀 Setup & Run

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Kalpi2002/flask-lite-project
    cd flask-lite-project
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
   
    
## 🚀 Contribution Table

- Member	                  -Contribution
- K.E. Kumarasinghe (Lead)	-Repo setup, DB config, seed script, README, Create form
- R.M.C.N. Abeyvickrama	    -Edit form, Templates & CSS
- G.A.M.A. Dissanayake     -Search/filter functionality
- P.N. Wickramarathna	      -List page layout & functionality
- W.D.N.O. Wanniarachchi	  -Delete feature with confirmation

## 📈 Progress Log

**Sep 2**
- Repo created
- Members added
- Base Flask app runs
- Defined the database schema with a `Task` model (`models.py`)
- Configured the Flask app to connect to a SQLite database (`app.py`)
- Created a seed script to populate the database with sample data (`seed.py`)
- Implemented a basic route (`/tasks`) to fetch and display all tasks from the database

**Sep 3**
- Added Create Task functionality with validation and flash messages
- Added Edit Task functionality with prefilled form
- Updated templates with Bootstrap styling

**Sep 4**
- Added Delete Task with confirmation page
- Implemented Search/Filter on list page
- Refined template styling for cards, forms, and buttons

**Sep 5–6**
- Polished UI: spacing, responsive design, flash messages
- Tested all CRUD flows and search functionality
- Updated README with screenshots and contribution table

**Sep 7**
- Final testing of all CRUD + search flows
- Verified flash messages and responsive layout
- Committed and pushed final code to main
- Confirmed instructor access to private repository

