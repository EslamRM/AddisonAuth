import asyncio
import random
from datetime import datetime, timezone

from token_service.schemas.models import User, UserToken


class TokenService:
    @staticmethod
    async def generate_token(user: User) -> UserToken:
        # simulate random delay (0-5 seconds)
        delay = random.uniform(0, 5)
        await asyncio.sleep(delay)

        # Fail if user_id starts with "A" or "a"
        if user.user_id.lower().startswith("a"):
            raise ValueError("Token generation failed: user_id starts with 'A'")

        # generate timestamp in UTC
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        # Create the token
        token = f"{user.user_id}_{timestamp}"

        return UserToken(token=token)