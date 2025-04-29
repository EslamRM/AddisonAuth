import pytest
from token_service.services.orchestrator_service import OrchestratorService
from token_service.schemas.models import Credentials


@pytest.mark.asyncio
async def test_request_token_success():
    credentials = Credentials(username="user123", password="USER123")
    token = await OrchestratorService().request_token(credentials)
    assert token.token.startswith("user123_")


@pytest.mark.asyncio
async def test_request_token_failure_invalid_credentials():
    credentials = Credentials(username="user123", password="wrongpass")
    with pytest.raises(ValueError, match="Invalid credentials"):
        await OrchestratorService().request_token(credentials)
