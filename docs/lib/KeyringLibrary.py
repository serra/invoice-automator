import keyring


class KeyringLibrary:
    def __init__(self):
        pass

    def can_access_credential(self, system, key):
        return keyring.get_password(system, key)
