import requests

url='https://vip.weibo.com/personal?showall=all'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'cookie':'SINAGLOBAL=5263992966328.351.1510218306316; SCF=ArnIAJbNd5P2LFQuDTEphJ6ki81IRHQ-nrkTLpF6bmkcO8ah5aNs3vB_S8LnU9gKcVI90Za8rsTxwTkOPRZQISM.; login_sid_t=b1bcb4d5beb1082b6809ba8ff270014a; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=2175518268392.1182.1603453901524; ULV=1603453901528:1:1:1:2175518268392.1182.1603453901524:; webim_unReadCount=%7B%22time%22%3A1603454619129%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; VIP-G0=c82a2c3fe29499531400f46f7a79a2a9; WBStorage=8daec78e6a891122|undefined; UOR=,,login.sina.com.cn; SUB=_2A25ylraZDeRhGeNG7FcY9irJwzSIHXVR5a9RrDV8PUNbmtAKLUynkW9NSzbxKIl6KWOt8azvkfzl09nlUZay13VP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFTrjZxlXTKv.aiHpAguWEz5JpX5KzhUgL.Fo-RS0-4SoBf1hn2dJLoI0YLxK.L1-BL1KzLxKqLBKBL1KzLxKqL12zL12eLxK.LBK-LB-BLxK.LBK-LB-BLxK.LBK-LB-BLxK.LBK-LB-Bt; SUHB=0V5lAlcp7KAmQu; ALF=1634990665; SSOLoginState=1603454665; wvr=6'

}

res=requests.get (url,headers=headers);

code=res.status_code;
print(code)

if code==200:
    with open('./test.html','w') as fp:
        fp.write(res.content.decode('utf-8'))