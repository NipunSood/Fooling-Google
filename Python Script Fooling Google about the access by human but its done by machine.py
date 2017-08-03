import urllib.request
import urllib.parse

value={'q':'Python Progamming Language'}
data=urllib.parse.urlencode(value)
url="https://www.google.co.in/search?"+data
header={}
"""Below line fools the Google that the content is access by Human
Not by machine"""
header['User-Agent']="Mozilla/6.0 (x11; Linux i686)"
req=urllib.request.Request(url,headers=header)
resp=urllib.request.urlopen(req)
resp_data=resp.read()
print(resp_data)