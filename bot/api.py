#!/usr/bin/python3.6
''' This is a future implementation '''

''' Using pubgs open API to create another layer of detail on the announced kill, game placement, damage dealt, etc. '''
import json, requests, traceback
from abc import ABC, abstractmethod

class Api(ABC):
    ''' Trying to learn abc..'''
    def __init__(self):
        self.url = 'https://api.pubg.com/shards/steam'

class GetData(Api):
    def MatchInfo(self, matchid=None):
        ''' Returns data and statistics for this match '''
        if matchid is None:
            return None
        headers = {'Accept': 'application/vnd.api+json'}
        self.append = '/matches/{}'.format(matchid)
        get = requests.get(self.url + self.append, headers=headers)
        data = json.loads(get.text)
        return data

def compute(victim=None, matchid=None):
    ''' Chaos incarnate'''
    from bot.pubg import Api as dApi
    x = GetData() # Init pubg api
    y = dApi()    # Init report api
    victimid = y.getId(victim)
    proc = x.MatchInfo(matchid=matchid)
    if victimid == None:
        return False
    for i in proc['included']:
        try:
            if i['attributes']['stats']['playerId'] == victimid: # AccountID
                diter = i['attributes']['stats']
                place = diter['winPlace']
                kills = diter['kills']
                time = diter['timeSurvived'] / 60
                knocked = diter['DBNOs']
                return('{} had {} kills, {} knock(s), was alive for {} minutes and was ranked {}/100 in this match.'.format(victim, kills, knocked, round(time,1), place))
        except:
            pass
    return False

#print(compute('Elite2802', 'acaaaa94-b8b7-4f2f-b037-40241afc42e3'))
