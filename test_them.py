#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_review = Review()
my_review.text = "very good project"
my_review.user_id = "captain marvel"
my_review.place_id = 'MCU'

my_review.save()
print(my_review)

