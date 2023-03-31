import requests
import re
import pyperclip

"""IP:PORT regex pattern"""
pattern=r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"

req=requests.get("https://proxy-daily.com")
text=str(req.content)
http_dirty=str(text.split("Free Http/Https Proxy List:")[1].split("Free Socks4 Proxy List:")[0])
socks4_dirty=str(text.split("Free Socks4 Proxy List:")[1].split("Free Socks5 Proxy List:")[0])
socks5_dirty=str(text.split("Free Socks5 Proxy List:")[1].split("Premium Proxy Service")[0])
match_http = re.findall(pattern=pattern,string=http_dirty)
match_socks4 = re.findall(pattern=pattern,string=socks4_dirty)
match_socks5 = re.findall(pattern=pattern,string=socks5_dirty)
req2=requests.get("https://free-proxy-list.net")
text2=str(req2.content)
http_dirty2=text2.split("Updated at")
match_http2=re.findall(pattern,http_dirty2[1])
total_http=match_http + match_http2
import pyperclip
sonuc=""
for i in total_http:
    sonuc += i + "\n"

if not pyperclip.copy(sonuc):
    print("Done!")
else:
    print("Problem")
