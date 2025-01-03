from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_student(db: Session):

    student_all = db.query(models.Student).all()
    res = {
        'student_all': student_all,
    }
    return res

async def get_student_user_id(db: Session, user_id: int):

    student_one = db.query(models.Student).filter(models.Student.user_id == user_id).first()


    user_name: str = student_one.name

    res = {
        'student_one': student_one,
    }
    return res

async def post_student(db: Session, user_id: int, name: str, email: str, password: str, role: str):

    record_to_be_added = {'user_id': user_id, 'name': name, 'email': email, 'password': password, 'role': role}
    new_student = models.Student(**record_to_be_added)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    student_inserted_record = new_student


    user_name = []  # Creating new list

    res = {
        'student_inserted_record': student_inserted_record,
        'user': name,
    }
    return res

async def put_student_user_id(db: Session, user_id: str, name: str, email: str, password: str, role: str):

    student_edited_record = db.query(models.Student).filter(models.Student.user_id == user_id).first()
    for key, value in {'user_id': user_id, 'name': name, 'email': email, 'password': password, 'role': role}.items():
          setattr(student_edited_record, key, value)
    db.commit()
    db.refresh(student_edited_record)
    student_edited_record = student_edited_record

    res = {
        'student_edited_record': student_edited_record,
    }
    return res

async def delete_student_user_id(db: Session, user_id: int):

    student_deleted = None
    record_to_delete = db.query(models.Student).filter(models.Student.user_id == user_id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          student_deleted = record_to_delete
    res = {
        'student_deleted': student_deleted,
    }
    return res

async def get_user(db: Session):

    user_all = db.query(models.User).all()
    res = {
        'user_all': user_all,
    }
    return res

async def get_user_id(db: Session, id: int):

    user_one = db.query(models.User).filter(models.User.id == id).first()
    res = {
        'user_one': user_one,
    }
    return res

async def post_user(db: Session, id: str, address: str, fullname: str, age: str, email: str):

    record_to_be_added = {'id': id, 'address': address, 'fullname': fullname, 'age': age, 'email': email}
    new_user = models.User(**record_to_be_added)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user_inserted_record = new_user
    res = {
        'user_inserted_record': user_inserted_record,
    }
    return res

async def put_user_id(db: Session, id: str, address: str, fullname: str, age: str, email: str):

    user_edited_record = db.query(models.User).filter(models.User.id == id).first()
    for key, value in {'id': id, 'address': address, 'fullname': fullname, 'age': age, 'email': email}.items():
          setattr(user_edited_record, key, value)
    db.commit()
    db.refresh(user_edited_record)
    user_edited_record = user_edited_record

    res = {
        'user_edited_record': user_edited_record,
    }
    return res

async def delete_user_id(db: Session, id: int):

    user_deleted = None
    record_to_delete = db.query(models.User).filter(models.User.id == id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          user_deleted = record_to_delete
    res = {
        'user_deleted': user_deleted,
    }
    return res

async def get_tasks(db: Session):

    tasks_all = db.query(models.Tasks).all()
    res = {
        'tasks_all': tasks_all,
    }
    return res

async def get_tasks_id(db: Session, id: int):

    tasks_one = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    res = {
        'tasks_one': tasks_one,
    }
    return res

async def post_tasks(db: Session, id: str, title: str, description: str, status: str, priority: str):

    record_to_be_added = {'id': id, 'title': title, 'description': description, 'status': status, 'priority': priority}
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    tasks_inserted_record = new_tasks
    res = {
        'tasks_inserted_record': tasks_inserted_record,
    }
    return res

async def put_tasks_id(db: Session, id: str, title: str, description: str, status: str, priority: str):

    tasks_edited_record = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    for key, value in {'id': id, 'title': title, 'description': description, 'status': status, 'priority': priority}.items():
          setattr(tasks_edited_record, key, value)
    db.commit()
    db.refresh(tasks_edited_record)
    tasks_edited_record = tasks_edited_record

    res = {
        'tasks_edited_record': tasks_edited_record,
    }
    return res

async def delete_tasks_id(db: Session, id: int):

    tasks_deleted = None
    record_to_delete = db.query(models.Tasks).filter(models.Tasks.id == id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          tasks_deleted = record_to_delete
    res = {
        'tasks_deleted': tasks_deleted,
    }
    return res

async def post_studentsdetails(db: Session, id: int):    res = {
    }
    return res

