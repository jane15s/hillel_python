class TooManyStudents(Exception):
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name

    def __str__(self):
        return f"{self.error_message} (Group: {self.group_name})"