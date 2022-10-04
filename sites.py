import re
def twitter(link):
    #Twitter Status
    if f"/status/" in link:
        m = (re.search(r"twitter.com\/[\w\-.]+\/status\/[\d]+", link)).group(0)
        stat = (re.search(r"[\d]+", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.twitter.android;scheme=https;end")
        print(f"iOS : twitter://status?id={stat}")
        print(f"Web : {m}")
    #Twitter Users
    else:
        m = (re.search(r"twitter.com\/[\w-.]+", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.twitter.android;scheme=https;end")
        print(f"iOS : twitter://user?screen_name={m[12:]}")
        print(f"Web : {m}")
def instagram(link): 
    #Instagram Posts
    if f"/p/" in link:
        m = (re.search(r"instagram.com\/p\/[\w\-\.]+", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.instagram.android;scheme=https;end")
        print(f"iOS : instagram://media?id={m[16:]}")
        print(f"Web : {m}")
    #Instagram Users
    else :
        m = (re.search(r"instagram.com\/[\w\-\.]+", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.instagram.android;scheme=https;end")
        print(f"iOS : instagram://user?username={m[14:]}")
        print(f"Web : {m}")
def youtube(link):
    #Youtube Videos
    m = (re.search(r"youtube.com\/watch\?v\=[\w-]+", link)).group(0)
    print(f"Android : intent://{m}#Intent;package=com.google.android.youtube;scheme=https;end")
    print(f"iOS : vnd.youtube://{m[20:]}")
    print(f"Web : {m}")
def tiktok(link):
    #Tiktok Videos
    m = (re.search(r"tiktok.com/[\w\-\/]+", link)).group(0)
    print(f"Android : snssdk1233://webview?url={m}")
    print(f"iOS : snssdk1233://webview?url={m}")
    print(f"Web : {m}")
def snapchat(link):
    #Snapchat Users
    if f"/add/" in link:
        m = (re.search(r"snapchat.com\/add\/[\w\.]+", link)).group(0)
        print(f"Android : intent://add/{m[17:]}#Intent;package=com.snapchat.android;scheme=snapchat;end;")
        print(f"iOS : snapchat://add/{m[17:]}")
        print(f"Web : {m}")
    #Snapchat Video?
    else:
        m = (re.search(r"snapchat.com\/discover\/[\w\.]+", link)).group(0)
        print(f"Android : intent://discover/{m[22:]}#Intent;package=com.snapchat.android;scheme=snapchat;end;")
        print(f"iOS : snapchat://discover/{m[22:]}")
        print(f"Web : {m}")
def messenger(link):
    #Messenger Thread
    m = (re.search(r"messenger.com\/t\/[\d\.]+", link)).group(0)
    print(f"Android : intent://user/{m[16:]}/#Intent;package=com.facebook.orca;scheme=fb-messenger;end")
    print(f"iOS : fb-messenger-public://user-thread/{m[16:]}")
    print(f"Web : {m}")


