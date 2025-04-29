import asyncio
import random
from token_service.schemas.models import Credentials, User

class AuthService:
    @staticmethod
    async def login(user: User, credentials: Credentials):
        # Simulate a delay
        delay = random.randint(0, 5)
        await asyncio.sleep(delay)
        # Check credentials
        if credentials.password != credentials.username.upper():
            raise Exception("Invalid credentials")
        # Return user
        return User(user_id=credentials.username)
