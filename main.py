import os
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

cl = Client()
cl.login(username=USERNAME, password=PASSWORD, verification_code='939538')

following = cl.user_following(amount=50)
print(following)
