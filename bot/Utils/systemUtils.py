import os


def getTogglToken() -> str:
    return os.getenv("TOGGL_TOKEN")


def getRomanToken() -> str:
    return os.getenv("ROMAN_TOKEN")


def getRomanURL() -> str:
    # TODO
    return "http://proxy.services.zinfra.io"


def getWorkspaceId() -> int:
    # TODO fetch from env
    return 4039412
