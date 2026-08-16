from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
import pytest
from src.main.api.db.crud.user_crud import UserCrudDb as User


@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)],
    )
    def test_create_user_valid(self, api_manager, create_user_request: CreateUserRequest, db_session: Session):

        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.role == response.role, "Созданный пользователь не имеет роли ROLE_USER, ошибка"
        assert create_user_request.username == response.username, "Пользователь не создался, ошибка"

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, "Созданного пользователя нет в БД"

    @pytest.mark.parametrize(
        "username, password",
        [
            ("ааывф", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("asdsfffsdfghjklmn", "Pas!sw0rd"),
            ("asds!", "Pas!sw0rd"),
            ("Max20", "Pas!sw0rп"),
            ("Max21", "Pas!sw"),
            ("Max22", "as!sw0rd"),
            ("Max23", "PAS!SW0R"),
            ("Max24", "Passw0rd"),
            ("Max25", "Pas!swrd"),
        ]
    )
    def test_create_user_invalid(self, db_session: Session, api_manager: ApiManager, username: str, password: str):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")

        api_manager.admin_steps.create_user_invalid(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert user_from_db is None, 'Пользователь создан, ошибка'