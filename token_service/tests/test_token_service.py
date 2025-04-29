import pytest
from token_service.services.tokenService import TokenService
from token_service.schemas.models import User


@pytest.mark.asyncio
async def test_generate_token_success():
    user = User(user_id="testuser")  # <-- fix: user_id not userId
    token = await TokenService().generate_token(user)
    assert token.token.startswith("testuser_")


@pytest.mark.asyncio
async def test_generate_token_failure():
    user = User(user_id="AppleUser")  # <-- fix: user_id not userId
    with pytest.raises(
        ValueError, match="Users starting with 'A' cannot be issued tokens"
    ):
        await TokenService().generate_token(user)
