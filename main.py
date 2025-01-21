from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
cl = Client()
cl.login(user, password)

followers = cl.user_followers(cl.user_id)
following = cl.user_following(cl.user_id)

not_following = []
for user in following.keys():
    if user not in followers:
        not_following.append(user)

for user in not_following:
    print(user)