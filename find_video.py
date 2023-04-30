import requests
import re

def find_video(channel):
  url=[]
  list1=[]
  test=[]
  #channel = "https://www.youtube.com/channel/UC14zSCww91iy_JMaM8aXImQ"
  #print("test")
  html = requests.get(channel + "/recent", cookies={'CONSENT': 'YES+42'}).text
  
  #info = re.search('(?<={"label":").*?(?="})', html).group()
  info = html.split('"}}},"publishedTimeText":{"simpleText":"')#skip the first part of the page
  for i in range(len(info)-1):
    test=re.search('.*?(?= geleden"})', info[i+1]).group()#find upload date (relative to current time) #ago becomes geleden
    if '":"0:' in info[i+1]:#find videos with length < 1 minute
      print("this is a short: ", i+1 )
      continue
    print (test)
    url.append(re.search('(?<=url":").*?(?=","webPageType":"W)', info[i+1]).group())#find video URL
    #the following was used when I wanted different responses depending on when something was uploaded. But didn't end up using it.
    #if "dag" in test or "dagen" in test:
    #  test = [int(s) for s in test.split() if s.isdigit()]
    #  test[0]=test[0]*24*3600
    #  print(test[0])
    #  url.append(re.search('(?<=url":").*?(?=","webPageType":"W)', info[i+1]).group())
    #  print(url)
    #
    #
    #  
    #if "uur" in test:
    #  test = [int(s) for s in test.split() if s.isdigit()]
    #  #print(test[0])
    #  test[0] *=3600
    #  print(test[0])
    #  url.append(re.search('(?<=url":").*?(?=","webPageType":"W)', info[i+1]).group())
    #  print(url)
    #if "minuten" in test:
    #  test = [int(s) for s in test.split() if s.isdigit()]
    #  test[0]*=60
    #  print(test[0])
    # # url = re.search('(?<=url":").*?(?=","webPageType":"W)', info[i+1]).group()
    #  url.append(re.search('(?<=url":").*?(?=","webPageType":"W)', info[i+1]).group())
    #  print(url)
   
    list1.append(test[0])#left in because of old design, used in for loop below but is useless data
  print(list1)
  urlindex=0
  
  for i in range(len(list1)):#not at all necessary any more
   # print(type(list[i]))
    print("new video uploaded")
    print("watch it here: https://www.youtube.com" + url[urlindex])
    urlindex+=1
    #if list1[i] <=518400:
    #  print("new video uploaded")
    #  print("watch it here: https://www.youtube.com" + url[urlindex])
    #  urlindex+=1
  return url
channel = "https://www.youtube.com/channel/UC14zSCww91iy_JMaM8aXImQ"
hello= find_video(channel)
