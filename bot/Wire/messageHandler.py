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
        sendResponse(message['token'], text.split("/report", 1)[1].strip())


def sendResponse(token, text):
    split = text.split(" ")
    since = split[0]
    until = split[1]
    sendReport(token, since, until)
