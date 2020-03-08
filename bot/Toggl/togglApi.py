from toggl.TogglPy import Toggl
from dataclasses import dataclass
from typing import List
from Utils.timeUtils import millisToText


def getTogglReport(token: str, workSpace: int, since: str, until: str) -> str:
    """
    Fetches data from Toggl and creates printable report.
    :param token: token for Toggl
    :param workSpace: id of workspace from which should be data fetched
    :param since:"2020-03-01"
    :param until:"2020-03-01"
    :return: printable report for given dates
    """
    # create toggl instance and get report
    toggl = getTogglClient(token)
    report = obtainTogglReport(toggl, workSpace, since, until)

    # convert received data
    totalWorkedInMillis = report['total_grand']
    projects = [getDataForProject(x) for x in report['data']]

    # format data to printable string
    projectsStringReport = "\n".join([x.toString() for x in projects])
    finalReport = f"Total time worked since {since} until {until}: {millisToText(totalWorkedInMillis)}\nProjects " \
                  f"report:\n{projectsStringReport} "
    return finalReport


def getTogglClient(token: str) -> Toggl:
    toggl = Toggl()
    toggl.setAPIKey(token)
    return toggl


def obtainTogglReport(toggl: Toggl, workspace: int, since: str, until: str) -> dict:
    dataFilter = {
        "workspace_id": workspace,
        "since": since,
        "until": until
    }
    report = toggl.getSummaryReport(dataFilter)
    return report


@dataclass
class Topic:
    name: str
    time: int

    def toString(self) -> str:
        return f"{self.name} - {millisToText(self.time)}"


@dataclass
class Project:
    name: str
    time: int
    topics: List[Topic]

    def toString(self) -> str:
        topics = "\n".join([f"|____ {x.toString()}\n" for x in self.topics])
        return f"{self.name} - total time - {millisToText(self.time)}\n{topics}"


def getDataForTopic(topic) -> Topic:
    name = topic['title']['time_entry']
    time = topic['time']
    return Topic(name, time)


def getDataForProject(project) -> Project:
    name = project['title']['project']
    time = project['time']
    topics = [getDataForTopic(x) for x in project['items']]
    return Project(name, time, topics)
