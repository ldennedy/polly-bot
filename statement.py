class Statement(object):
    sentence = ""
    context = []
    def __init__(self, s, c = None):
        self.sentence = s
        if c:
            self.generate_context(c)

    def generate_context(self, c):
        self.context = c.split()
