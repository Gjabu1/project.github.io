import pyshorteners

url = input()
short = pyshorteners.Shortener()
result = short.clckru.short(url)

print(result)
