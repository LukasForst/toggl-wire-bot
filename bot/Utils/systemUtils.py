import os


def getTogglToken() -> str:
    return os.getenv("TOGGL_TOKEN")


def getWorkspaceId() -> int:
    # TODO fetch from env
    return 4039412
