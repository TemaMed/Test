from api.models import User


def get_pvd(username):
    return User.objects.get(user_name=username).password
