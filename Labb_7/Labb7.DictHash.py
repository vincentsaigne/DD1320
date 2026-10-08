class DictHash:
    def __init__(self):
        self.dict = {}

    def store(self, nyckel, data):
        self.dict[nyckel] = data

    def search(self, nyckel):
        try:
            return self.dict[nyckel]
        except KeyError:
            return "Datan finns inte"

    def __getitem__(self, nyckel):
        return self.search(nyckel)

    def __contains__(self, nyckel):
        return nyckel in self.dict

