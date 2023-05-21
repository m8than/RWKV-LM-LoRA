class Registry:
    def __init__(self):
        print("Registry init")
        pass
    def setup(self):
        print("Registry setup")
        self.last_token_lengths = []
        self.last_ctx_length = 0
        self.total_documents = 0