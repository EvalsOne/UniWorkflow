class OAuthHandler:
    def __init__(self):
        self.tokens = {}

    def add_token(self, provider, token):
        self.tokens[provider] = token

    def get_token(self, provider):
        return self.tokens.get(provider)
