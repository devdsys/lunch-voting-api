import pytest
from app.auth.services import login
from app.auth.schemas import LoginRequest
from app.models.employee import Employee
from sqlalchemy.orm import Session
from pytest_mock import MockerFixture
from fastapi import HTTPException

@pytest.fixture
def mock_db_session(mocker: MockerFixture):
    mock_session = mocker.MagicMock(spec=Session)
    mock_query = mocker.MagicMock()
    
    # Create a mock employee
    mock_employee = Employee(
        email="test@i.ua",
        name="TestName",
        surname='TestSurname'
    )
    mock_employee.set_password("Test1111!")
    
    # Mock the query method
    mock_query.filter.return_value.first.return_value = mock_employee
    mock_session.query.return_value = mock_query
    
    return mock_session

@pytest.fixture
def login_request():
    return LoginRequest(
        email="test@i.ua",
        password="Test1111!",
        role="employee"
    )

def test_login_successful(mock_db_session, login_request):
    result = login(login_request, mock_db_session)
    assert result is not None
    assert "access_token" in result
    assert "refresh_token" in result


def test_login_fails_with_wrong_password(mock_db_session, login_request):
    wrong_login_request = login_request.copy(update={"password": "Test2222!"})

    with pytest.raises(HTTPException) as exc_info:
        login(wrong_login_request, mock_db_session)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Incorrect email or password"
