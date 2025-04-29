from token_service.schemas.models import Credentials, UserToken
from token_service.services.auth_service import AuthService
from token_service.services.tokenService import TokenService


class OrchestratorService:
    def __init__(self):
        self.auth_service = AuthService()
        self.token_service = TokenService()

    async def request_token(self, credentials: Credentials) -> UserToken:
        # Step 1: Authenticate user
        user = await self.auth_service.login(user=credentials.username, credentials=credentials)

        # Step 2: Issue token
        token = await self.token_service.generate_token(user)

        return token
