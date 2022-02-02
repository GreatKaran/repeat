from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon import functions, types
api_ids = [10811615] #add more when need u gey
api_hashs = ['7708fab7ae0a3e77d142bad2960da72d']
string_session = ['1AZWarzwBu2zIkae1R3x7nuWgrRVCD64CHkX0VOua3uLchewuXFi9gL3-KKdcGwLwntljMpnS-1EOTXrRhj36V_z2w_fmSGS7LHLxEuFuRKslaAcBI9lEvHJhxXReR1qQvZE50FEF4glNqSRfH8dHb1HyQuP1Oj6hN_ZL9BGFBRKdeRxCa5D2-hnnFsuQ7EbpmVoTLFEcj9-wCR8np1WQVtxkCeAIlWzR8UU6qvlNX3pBbZcGEMNihZcAQnnAzwHrFWgoE8EsyZJe1EHhQ4r0OGMDgK8cpvqh9dK85ptE3BqDnKMt2XjMzn8HN75Tg0haS5rAqBkGlnjx8LzqX1vE2nKb1TQcTp4=']
for i in range(0,len(api_ids)):
    api_id = api_ids[i]
    api_hash = api_hashs[i]
    string = string_session[i]
    with TelegramClient(StringSession(string),api_id,api_hash) as client:
        result = client(functions.messages.ReportRequest(
        peer='username',
        id=[42],
        reason=types.InputReportReasonSpam(),
        message='mass forwarding child porn and scamming people we request telegram to ban this channel '
    ))
        print(result)
