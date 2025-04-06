# Client and Project Management API

This is a Django REST Framework project to manage clients and their assigned projects. Users can create clients, assign projects to them, and link registered users to those projects.

 Features

- Create and view clients
- Assign projects to clients
- Add existing users to projects
- View projects assigned to logged-in users

 How to Run

1. Clone the repo:
   git clone https://github.com/Swapnilawalekar/Nimap-Project.git

2. Navigate to the folder:
   cd Nimap-Project

3. Create virtual environment and install dependencies:
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   pip install -r requirements.txt
  

4. Run migrations and start the server:
   python manage.py migrate
   python manage.py runserver

API Endpoints

- `GET /clients/` – List all clients  
- `POST /clients/` – Create a new client  
- `POST /clients/<id>/projects/` – Create a project for a client  
- `GET /projects/` – View projects assigned to logged-in user  

Author

Swapnil Anil Awalekar
