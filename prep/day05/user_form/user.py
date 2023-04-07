class User:
    
    user_count = 0
    all_users = []
    def __init__(self, data) -> None:
        User.user_count += 1
        self.id = User.user_count
        self.user_name = data['user_name']
        self.password = data['password']
        User.all_users.append(self)