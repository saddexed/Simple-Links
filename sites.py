import re
def twitter(link):
    #Twitter Status
    if f"/status/" in link:
        m = (re.search(r"twitter.com\/[\w\-.]{3,}\/status\/[\d]{3,}", link)).group(0)
        stat = (re.search(r"[\d]{3,}", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.twitter.android;scheme=https;end")
        print(f"iOS : twitter://status?id={stat}")
        print(f"Web : {m}")
    #Twitter Users
    else:
        m = (re.search(r"twitter.com\/[\w-.]{3,}", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.twitter.android;scheme=https;end")
        print(f"iOS : twitter://user?screen_name={m[12:]}")
        print(f"Web : {m}")
def instagram(link): 
    #Instagram Posts
    if f"/p/" in link:
        m = (re.search(r"instagram.com\/p\/[\w\-\.]{3,}", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.instagram.android;scheme=https;end")
        print(f"iOS : instagram://media?id={m[16:]}")
        print(f"Web : {m}")
    #Instagram Users
    else :
        m = (re.search(r"instagram.com\/[\w\-\.]{3,}", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.instagram.android;scheme=https;end")
        print(f"iOS : instagram://user?username={m[14:]}")
        print(f"Web : {m}")
def youtube(link):
    m = (re.search(r"youtube.com\/watch\?v\=[\w-]{3,}", link)).group(0)
    print(f"Android : intent://{m}#Intent;package=com.google.android.youtube;scheme=https;end")
    print(f"iOS : vnd.youtube://{m[20:]}")
    print(f"Web : {m}")