from dataclasses import dataclass


# Define a User dataclass
@dataclass
class User:
    id: int
    name: str
    email: str
    is_valid_email: bool = False
    profile_pic_url: str = None
    last_active_days: int = None
