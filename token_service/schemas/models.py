from dataclasses import dataclass

@dataclass
class Credentials:
    username: str
    password: str

@dataclass
class User:
    user_id: str


@dataclass
class UserToken:
    token: str