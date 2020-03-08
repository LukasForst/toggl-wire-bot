from Toggl.togglApi import getTogglReport
from Utils.systemUtils import getWorkspaceId, getTogglToken
from Wire.proxy import sendMessage


def processMessage(message):
    if message["type"] == "conversation.new_text":
        processTextMessage(message)


def sendReport(token, since, until):
    workspace = getWorkspaceId()
    report = getTogglReport(getTogglToken(), workspace, since, until)
    print(report)
    msg = {"type": "text", "text": report}
    sendMessage(token, msg)


def processTextMessage(message):
    text = message["text"]
    if text.startswith("/report"):
        sendReport(message["token"], "2020-03-01", "2020-03-30")
