import urllib

str = 'http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian1761.html'
str = urllib.unquote(str)
print str