from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.repay_credit_request import RepayCreditRequest
from src.main.api.models.request_credit_request import RequestCreditRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest


"""класс для получения и погашения кредита"""
class SecretUserSteps(BaseSteps):
    def create_account_secret(self, create_secret_user_request: CreateSecretUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_secret_user_request.username, password=create_secret_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def request_credit(self, create_secret_user_request: CreateSecretUserRequest, request_credit_request: RequestCreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_secret_user_request.username, password=create_secret_user_request.password),
            Endpoint.REQUEST_CREDIT,
            ResponseSpecs.request_created()
        ).post(request_credit_request)
        return response

    def repay_credit(self, create_secret_user_request: CreateSecretUserRequest, repay_credit_request: RepayCreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(create_secret_user_request.username, password=create_secret_user_request.password),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_ok()
        ).post(repay_credit_request)
        return response

    def request_credit_invalid(self, create_secret_user_request: CreateSecretUserRequest, request_credit_invalid_request: RequestCreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_secret_user_request.username, password=create_secret_user_request.password),
            Endpoint.REQUEST_CREDIT,
            ResponseSpecs.request_not_found()
        ).post(request_credit_invalid_request)

    def repay_credit_invalid(self, create_secret_user_request: CreateSecretUserRequest, repay_credit_invalid_request: RepayCreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_secret_user_request.username, password=create_secret_user_request.password),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.unprocessable_entity()
        ).post(repay_credit_invalid_request)