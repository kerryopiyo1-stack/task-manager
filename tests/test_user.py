from models.user import User

def test_user_creation():
    user = User("1", "Kerry")

    assert user.user_id == "1"
    assert user.name == "Kerry"
    assert user.projects == []