import random as random

class SessionError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Session():
    def __init__(self, bound=100000):
        self._sess = {}
        self.bound = bound

    def setbound(self, bound):
        self.bound = bound

    def initrand(self):
        self.bound += random.randint(0, 5000)

    def checkitem(self, item):
        if item not in self._sess:
            return False
        return True

    def __getitem__(self, item):
        if item not in self._sess:
            raise SessionError("Session set doesn't contain this session!")
        else:
            return self._sess[item]

    def gen_sess(self, randlen = 50000):
        while True:
            sess_num = self.bound + random.randint(0, randlen)
            if sess_num not in self._sess:
                return sess_num

    def insertuid(self, uid, group):
        new_sess = self.gen_sess()
        self._sess[new_sess] = (uid, group)
        return new_sess

#sess = Session()

