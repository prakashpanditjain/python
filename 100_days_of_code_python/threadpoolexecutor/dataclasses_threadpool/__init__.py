import random
import time
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import as_completed

from fontTools.misc.cython import returns
from sqlalchemy.testing import future

from datalake.user import User


# Function to validate email
def validate_email(user: User) -> User:
    time.sleep(random.uniform(0.1, 0.5))  # Simulate network delay
    # Simulate email validation logic
    user.is_valid_email = '@' in user.email and '.' in user.email.split('@')[-1]
    return user


def fetch_profile_picture(user: User):
    time.sleep(random.uniform(0.1, 0.5))
    user.profile_pic_url = f"https://picsum.photos/seed/{user.id}/200"
    return user


def get_activity(user: User):
    time.sleep(random.uniform(0.1, 0.5))
    user.last_active_days = random.randint(0, 30)
    return user


def enrich_user(user: User):
    # ThreadPoolExuecutor cross check all the parameter of user

    with ThreadPoolExecutor(max_workers=3) as executor:
        print(f"{time.time():.2f} - Enriching user {user.id}")
        futures = [
            executor.submit(validate_email, user),
            executor.submit(fetch_profile_picture, user),
            executor.submit(get_activity, user)
        ]

        for f in as_completed(futures):
            result = f.result()
    return result


if __name__ == '__main__':
    users = [
        User(1, "Alice", "alice@example.com"),
        User(2, "Bob", "bob[at]example.com"),
        User(3, "Charlie", "charlie@example.com"),
    ]

    start = time.time()
    # Enrich all users concurrently
    with ThreadPoolExecutor(max_workers=3) as  executor:
        enrich_users = list(executor.map(enrich_user, users))

    for usr in enrich_users:
        print(usr.email, usr.is_valid_email, usr.profile_pic_url, usr.last_active_days)

    print(f"TIme taken to enrich user  = {time.time() - start:.2f} seconds")