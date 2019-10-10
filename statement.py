class Statement(object):
    # A statement object contains a string for the sentence
    # and a list of words that fit the "context"
    # (What words were used in previous message for this statement)
    sentence = ""
    context = []
    def __init__(self, s, c = None):
        self.sentence = s
        if c:
            self.generate_context(c)
            
    def generate_context(self, c):
        self.context = c.split()
