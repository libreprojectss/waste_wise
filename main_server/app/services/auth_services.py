from app.services.user_services import AccountServices

class AuthServices:
    def __init__(self):
        self.userServices = AccountServices()

    def login(self, email, password):
        user = self.userServices.get_user_by_email(email)
        if user:
            if user.check_password(password):
                return user
        return None