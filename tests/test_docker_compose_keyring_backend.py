import keyring
from invoice_automator import moneybird

from invoice_automator.docker_compose_keyring_backend import DockerComposeKeyringBackend

SECRET_PATH = "./tests/run/secrets/"


def test_can_print_available_backends():
    print(keyring.backend.get_all_keyring())


def test_can_create_custom_backend():
    kbe = DockerComposeKeyringBackend()


def test_dckb_path_default_to_compose_default_backend():
    dckb = DockerComposeKeyringBackend()
    assert dckb.path_to_secrets == "/run/secrets/"


def test_dckb_path_can_be_set():
    dckb = DockerComposeKeyringBackend(SECRET_PATH)
    assert dckb.path_to_secrets == SECRET_PATH


def test_can_set_own_custom_backend():
    kbe = DockerComposeKeyringBackend(SECRET_PATH)
    keyring.set_keyring(kbe)


def test_when_set_password_then_raise_error():
    kbe = DockerComposeKeyringBackend(SECRET_PATH)
    keyring.set_keyring(kbe)
    try:
        keyring.set_password("service_x", "user_y", "password")
        assert False, "Should have raised an error"
    except Exception as e:
        assert type(e) == keyring.errors.PasswordSetError
        assert str(e) == "Configure secrets in your docker compose file."


def test_can_get_password():
    kbe = DockerComposeKeyringBackend(SECRET_PATH)
    keyring.set_keyring(kbe)
    with open(SECRET_PATH + "service_x_user_y", "r") as f:
        password_from_file = f.read()
    assert password_from_file == "password"
    password = keyring.get_password("service_x", "user_y")
    assert password == "password"


def test_can_get_moneybird_password_although_the_system_name_has_spaces():
    kbe = DockerComposeKeyringBackend(SECRET_PATH)
    keyring.set_keyring(kbe)
    password = keyring.get_password(
        moneybird.SYSTEM_NAME, moneybird.INVOICE_AUTOMATOR_MONEY_BIRD_TOKEN_KEY
    )
    assert password == "this is the moneybird secret"
