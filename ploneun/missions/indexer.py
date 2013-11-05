from plone.indexer import indexer
from five import grok
from ploneun.missions.content.mission import IMission
from ploneun.missions.content.missionreport import IMissionReport
from DateTime import DateTime
from Acquisition import aq_chain

def get_mission(obj):
    for i in aq_chain(obj):
        if IMission.providedBy(i):
            return i
    return None

@indexer(IMission)
def mission_start(obj):
    if obj.startDate:
        return DateTime(obj.startDate)

@indexer(IMission)
def mission_end(obj):
    if obj.endDate:
        return DateTime(obj.endDate)

@indexer(IMission)
def mission_country(obj):
    return obj.country

@indexer(IMissionReport)
def missionreport_country(obj):
    mission = get_mission(obj)
    return mission.country

@indexer(IMissionReport)
def missionreport_ilo_themes(obj):
    mission = get_mission(obj)
    return mission.ilo_themes
