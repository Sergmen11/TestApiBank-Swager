from src.main.api.models.login_user_request import LoginUserRequest
import requests
from http import HTTPStatus
from src.main.api.models.login_user_response import LoginUserResponse


class RequestSpecs:
    @staticmethod
    def base_headers():
        return {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

    @staticmethod
    def auth_headers(username: str, password: str):
        request = LoginUserRequest(username=username, password=password)
        response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json=request.model_dump(),
            headers=RequestSpecs.base_headers()
        )
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            response_data = LoginUserResponse(**response.json())
            token = response_data.token
            headers = RequestSpecs.base_headers()
            headers['Authorization'] = f'Bearer {token}'
            return headers
        raise Exception(f"Failed to login")