class KeyProvider:
    def __init__(self, keys_path):
        self.keys = {}
        with open(keys_path) as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                self.keys[name.strip()] = var

    def get_value(self, key):
        return self.keys[key]
