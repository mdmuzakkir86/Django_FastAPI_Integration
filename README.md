# TaskManager: Simple Django and FastAPI Integration Task Management Project

- In this project, There is main.py file in root directory, which has a FastAPI app and main.py file has a configurations which integrate FastAPI with Django ORM.

# Impornant Note: 
- I won't be able to implement html files with FastAPI routers due to lack of time. You can test FastAPI CURD operations from http://127.0.0.1:8000/docs.
- While testing FastAPI, when you create new task, task id will be starts from 9 because 1-8 are already used and some of them are deleted.
- So for tesing use ids from 9, to update and delete.

**Follow steps properly else you may get below System realted errors**
  - TypeError: 'NoneType' object is not subscriptable 
  - TypeError: argument of type 'WindowsPath' is not iterable
  **No worries Even though errors occur, it won't effects the project, you can use application in browser as usual**

## Setting Up the Development Environment

1. **Clone the Project and Navigate to the Project Directory**:
   - *cd TaskManager*
   

2. **Create a Virtual Environment**:
   - *python -m venv venv*
   

3. **Activate the Virtual Environment**:
   -  **Windows**:
      - Navigate to *cd venv\Scripts*
      - then run command: *activate*
      
5. **Navigate back to the Project Directory**:
    - Run command two times to navigate back to TaskManager folder: *cd ..*
     
6. **Install Dependencies**:
    - *pip install -r requirements.txt* -  make sure your in TaskManager
    
7. **To Start the Django Development Server**:
    - *python manage.py runserver*  -  make sure your in TaskManager
    - **Once the django development server is running, access the application in your browser at http://127.0.0.1:8000/.**
   
9. **To Start the FastAPI Development Server**:
    - *uvicorn main:app --reload*  - make sure your in TaskManager
   - **Once the FastAPI development server is running, access the application in your browser at http://127.0.0.1:8000/docs.**
   - While testing FastAPI, when you create new task, task id will be starts from 9 because 1-8 are already used and some of them are deleted.
   - So for tesing use ids from 9, to update and delete.
