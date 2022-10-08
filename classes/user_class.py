class User:
    def __init__(self, user_name, password, is_student, needs_sponsorship, email, desired_industry):
        self.user_name = user_name
        self.password = password
        self.is_student = is_student
        self.needs_sponsorship = needs_sponsorship
        self.email = email
        self.desired_industry = desired_industry

    def create_user(self):
        unique_id = "".join([str(ord(string)) for string in (f"{self.user_name}{self.password}")])
        user_info = {
            "user_name": self.user_name, 
            "password": self.password, 
            "user_id": unique_id, 
            "is_student": self.is_student,
            "needs_sponsorship": self.needs_sponsorship,
            "email": self.email,
            "desired_industry": self.desired_industry
            }
        return user_info