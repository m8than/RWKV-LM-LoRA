class Registry:
    def __init__(self):
        self.last_token_lengths = []
        self.last_ctx_length = 0
        self.total_documents = 0