class Config:
    def __init__(self):
        self.settings = {"debug": True}


c1 = Config()
c2 = Config()

print(c1 is c2)