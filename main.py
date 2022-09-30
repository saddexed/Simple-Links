import re

link = input()
check = 0

if f"twitter.com/" in link:
    print("Twitter Valid")
    check = 1
    m = (re.search(r"twitter.com\/[\w-.]{3,}", link)).group(0)
    print(f"Android : intent://{m}#Intent;package=com.twitter.android;scheme=https;end")
    print(f"iOS : twitter://user?screen_name={m[12:]}")
    print(f"Web : {m}")
    
if f"instagram.com/" in link:
    print("Instagram Valid")
    check = 2
    if f"/p/" in link:
        m = (re.search(r"instagram.com\/p\/[\w\-\.]{3,}", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.instagram.android;scheme=https;end")
        print(f"iOS : instagram://media?id={m[16:]}")
        print(f"Web : {m}")
    else :
        m = (re.search(r"instagram.com\/[\w\-\.]{3,}", link)).group(0)
        print(f"Android : intent://{m}#Intent;package=com.instagram.android;scheme=https;end")
        print(f"iOS : instagram://user?username={m[14:]}")
        print(f"Web : {m}")

if f"youtube.com/" in link:
    print("Youtube Valid")
    check = 3
    m = (re.search(r"youtube.com\/watch\?v\=[\w-]{3,}", link)).group(0)
    print(f"Android : intent://{m}#Intent;package=com.google.android.youtube;scheme=https;end")
    print(f"iOS : vnd.youtube://{m[20:]}")
    print(f"Web : {m}")
