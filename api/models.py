#database stuff
from django.db import models
import string
import random

def generate_unique_code():
    length = 6
    while True: #generates codes until it finds an unique one
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        #check if any room on db has a code equal to that
        if Room.objects.filter(code = code).count() == 0:
            break

    return code

# Create your models here.
#rooms created by the host
class Room(models.Model): #fields of information in each room
    code = models.CharField(max_length = 8, default = "", unique = True) #stores characters for the room's code
    host = models.CharField(max_length = 50, unique = True) #one host cant have multiple rooms
    guest_can_pause = models.BooleanField(null = False, default = False)
    votes_to_skip = models.IntegerField(null = False, default = 1)
    created_at = models.DateTimeField(auto_now_add = True) #automatically stores the date and time the room was created

    