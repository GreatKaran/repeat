from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon import functions, types
api_ids = [11462244] #add more when need u gey
api_hashs = ['cc99e2d4b6d2e803500bee18a416ab21']
string_session = ['1AZWarzMBu4SKr0K_MKw7Zz1tAVya1O7alrt7dpvmyVMjjUavvJR1MmOLp2EIPYppKYYzT3P4-g5kHMh8cwTj6HzqaSAubqHS4jZyeCMSZ9V9qS-vhmz4ol-5Z4wc2c0Ok5mUovh3b_9HwHv-CokIDWLaBT66pzWlidw54OXJ0NbqRvJhhEYS5ACssMbUQGc6-D5_6SafbjWuO64zkosBsNVpdqz5SsdNFOk11O0xpaBaf2Wv4t8Tub9W4o2FiuKsbnKLnIxok3032IlLSvKOuLGTs98h3mYND-VAtjQOJugLg39UHFwrRH2AYA68uvVKaNeox7C0uzwgHA1to57PKkhZzyng-Bg=']
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
