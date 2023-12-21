import os
from django.apps import apps
from django.conf import settings
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TaskManager.settings")

django.setup()  # Alternatively, use this if you prefer

apps.populate(settings.INSTALLED_APPS)


from fastapi import FastAPI
from django.conf import settings
from django.apps import apps
from Tasks.models import Task
from starlette.middleware.base import BaseHTTPMiddleware
from django.db import close_old_connections
from django.shortcuts import get_object_or_404
from pydantic import BaseModel


class DBConnectionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        close_old_connections()
        response = await call_next(request)
        close_old_connections()
        return response

app = FastAPI()
app.add_middleware(DBConnectionMiddleware)


class TaskCreateUpdateBase(BaseModel):
    title: str
    description: str
    due_date: str
    status: str

class TaskCreateUpdate(TaskCreateUpdateBase):
    pass


@app.get("/api/tasks/", response_model=list[TaskCreateUpdateBase])
def read_tasks():
    tasks = Task.objects.all()
    tasks_data = [{"title": task.title, "description": task.description, "due_date": str(task.due_date), "status": task.status} for task in tasks]
    return tasks_data


'''
    While creating tasks input from API formate should be same as below
    {
    "title": "Python code",
    "description": "Develop Python code for complex password generator.",
    "due_date": "2023-12-20",
    "status": "TODO"
    }
'''

@app.post("/api/tasks/", response_model=TaskCreateUpdateBase)
def create_task(task: TaskCreateUpdate):
    new_task = Task.objects.create(**task.dict())
    return new_task


'''
    to update the task input task_id should be like indexing 0,1, 2, ..
    Note id is unieque if 1 id realted data deleted, you can't access any other data using delete id
    Every pack of data it's own unique id
'''
@app.put("/api/tasks/{task_id}", response_model=TaskCreateUpdateBase)
def update_task(task_id: int, updated_task: TaskCreateUpdate):
    task = get_object_or_404(Task, pk=task_id)
    for field, value in updated_task.dict().items():
        setattr(task, field, value)
    task.save()
    return task


'''
    to delete the task input task_id should be like indexing 0,1, 2, ..
'''
@app.delete("/api/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return {"message": "Task deleted successfully"}

