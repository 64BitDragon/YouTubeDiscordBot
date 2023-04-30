import requests
import re

def find_video(channel):
  url=[]
  #channel = "https://www.youtube.com/channel/UC14zSCww91iy_JMaM8aXImQ"
  #print("test")
  html = requests.get(channel + "/recent", cookies={'CONSENT': 'YES+42'}).text
  
  #info = re.search('(?<={"label":").*?(?="})', html).group()
  info = html.split('"}}},"publishedTimeText":{"simpleText":"')#skip the first part of the page
  for i in range(len(info)-1):
    if '":"0:' in info[i+1]:#find videos with length < 1 minute
      print("this is a short: ", i+1 )
      continue
    #print (test)
    url.append(re.search('(?<=url":").*?(?=","webPageType":"W)', info[i+1]).group())#find video URL
    #print("new video uploaded")
    #print("watch it here: https://www.youtube.com" + url[-1])
  return url

channel = "https://www.youtube.com/channel/UC14zSCww91iy_JMaM8aXImQ"
hello= find_video(channel)
print(hello)
