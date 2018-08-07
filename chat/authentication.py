from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def authenticate(self, username, password):
        pass


class Memory(Authentication):
    def __init__(self, users):
        self._users = users

    def authenticate(self, username, password):
        # This is a poor implementation of authentication, without using
        # any sort of mechanism to protect against timing attacks, password leaks,
        # or .. well.. a variety of problems.

        if not username in self._users:
            return False

        return self._users[username] == str(password)
