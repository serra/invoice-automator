from importlib.metadata import PackageNotFoundError, version

APP_NAME = "Serra ICT Invoice Automator"

try:
    __version__ = version("invoice_automator")
except PackageNotFoundError:  # running from a source tree that is not installed
    __version__ = "unknown"
