import pytest
from accounts.models import CustomUser


@pytest.mark.django_db
def test_should_create_user(user_details):
    user = CustomUser.objects.create_user(
        email=user_details["email"], name=user_details["name"]
    )
    assert user.email == "test@gmail.com"
    assert user.name == "test user"


@pytest.mark.django_db
def test_should_fail_to_create_user_with_email(user_details):
    try:
        CustomUser.objects.create_user(email="", name=user_details["name"])
    except ValueError as ve:
        assert str(ve) == "User must have an email address"
        assert type(ve) == ValueError


@pytest.mark.django_db
def test_should_fail_to_create_user_with_name(user_details):
    try:
        CustomUser.objects.create_user(email=user_details["email"], name="")
    except ValueError as ve:
        assert str(ve) == "User must have a full name"
        assert type(ve) == ValueError


@pytest.mark.django_db
def test_should_create_super_user(user_details):
    user = CustomUser.objects.create_superuser(
        email=user_details["email"], name=user_details["name"]
    )
    assert user.email == "test@gmail.com"
    assert user.name == "test user"

@pytest.mark.django_db
def test_should_fail_to_create_super_user_with_email(user_details):
    try:
        CustomUser.objects.create_user(email="", name=user_details["name"])
    except ValueError as ve:
        assert str(ve) == "User must have an email address"
        assert type(ve) == ValueError

@pytest.mark.django_db
def test_should_fail_to_create_super_user_with_name(user_details):
    try:
        CustomUser.objects.create_user(email=user_details["email"],name="")
    except ValueError as ve:
        assert str(ve) == "User must have a full name"
        assert type(ve) == ValueError
#
@pytest.mark.django_db
def test_should_fail_to_create_super_user_with_false_is_staff_value(user_details):
    try:
        CustomUser.objects.create_superuser(
            email=user_details["email"], name=user_details["name"], is_staff=False
        )
    except ValueError as ve:
        assert str(ve) == "Superuser must have is_staff=True."
        assert type(ve) == ValueError

@pytest.mark.django_db
def test_should_fail_to_create_super_user_with_false_is_superuser_value(user_details):
    try:
        CustomUser.objects.create_superuser(
            email=user_details["email"], name=user_details["name"], is_superuser=False
        )
    except ValueError as ve:
        assert str(ve) == "Superuser must have is_superuser=True."
        assert type(ve) == ValueError
