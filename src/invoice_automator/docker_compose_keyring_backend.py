import os
import keyring
from keyring._compat import properties


class DockerComposeKeyringBackend(keyring.backend.KeyringBackend):
    def __init__(self, path_to_secrets: str = "/run/secrets/"):
        self.path_to_secrets = path_to_secrets

    @properties.classproperty
    def priority(cls):
        # on mac, the mac os keychain backend has priority 5,
        # so I choose a lower value because by default i want to use the mac os keychain
        return 2

    def get_password(self, service: str, username: str) -> str | None:
        secret_name = (service + "_" + username).replace(" ", "_")

        with open(os.path.join(self.path_to_secrets, secret_name), "r") as f:
            return f.read()

    def set_password(self, service: str, username: str, password: str) -> None:
        raise keyring.errors.PasswordSetError(
            "Configure secrets in your docker compose file."
        )
