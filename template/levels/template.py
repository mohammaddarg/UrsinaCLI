from ursina import *

class template(Entity):
    def __init__(self, content:list):
        super().__init__()
        self.content = content
        self.unload()

    def unload(self):
        for i in self.content:
            i.enabled  = False
    

    def load(self):
        for i in self.content:
            i.enabled  = True