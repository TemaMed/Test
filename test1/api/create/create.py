from api.models import User


def create_user(username, password):
    user = User(user_name=username,
                password=password)
    user.save()
