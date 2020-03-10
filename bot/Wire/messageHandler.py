from typing import Tuple

from Toggl.togglApi import getTogglReport, obtainBase64Pdf
from Utils.systemUtils import getWorkspaceId, getTogglToken
from Wire.proxy import sendMessage


def processMessage(message):
    if message["type"] == "conversation.new_text":
        processTextMessage(message)


def processTextMessage(message):
    text = message["text"]
    if text.startswith("/report"):
        sendResponse(message['token'], text.split("/report", 1)[1].strip(), False)
    elif text.startswith("/pdf"):
        sendResponse(message['token'], text.split("/pdf", 1)[1].strip(), True)


def parse(text: str) -> Tuple[str, str]:
    split = text.split(" ")
    since = split[0]
    until = split[1]
    return since, until


def sendResponse(token: str, text: str, pdf: bool):
    since, until = parse(text)
    if pdf:
        sendPdf(token, since, until)
    else:
        sendReport(token, since, until)


def sendReport(token, since, until):
    workspace = getWorkspaceId()
    report = getTogglReport(getTogglToken(), workspace, since, until)
    print(report)
    msg = {"type": "text", "text": report}
    sendMessage(token, msg)


def sendPdf(token, since, until):
    workspace = getWorkspaceId()
    report = obtainBase64Pdf(getTogglToken(), workspace, since, until)
    print(report)
    msg = {"type": "attachment", "attachment": report}
    sendMessage(token, msg)
