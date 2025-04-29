import pytest
from token_service.services.auth_service import AuthService
from token_service.schemas.models import Credentials


@pytest.mark.asyncio
async def test_authenticate_success():
    credentials = Credentials(username="testuser", password="TESTUSER")
    auth_service = AuthService()
    user = await auth_service.login(user=credentials.username, credentials=credentials)
    assert user.user_id == "testuser"  # <-- fix: user_id not userId


@pytest.mark.asyncio
async def test_authenticate_failure():
    credentials = Credentials(username="testuser", password="wrongpass")
    auth_service = AuthService()
    with pytest.raises(ValueError, match="Invalid credentials"):
        await auth_service.login(user=credentials.username, credentials=credentials)
