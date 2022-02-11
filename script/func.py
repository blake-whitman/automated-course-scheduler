# Dependencies
import config
import requests
from bs4 import BeautifulSoup as bs

# Session Setup
s = requests.Session()

# Login to account
# Returns void
def login(username, password):
  payload = {
    'pass': password,
    'submit': '',
    'uname': username
  }
  
  s.get(config.URL)
  s.post(config.URL, data=payload)
  return

# Verify successful registration
# Returns bool ifSuccessful
def isRegistered():
  sourceTMP = s.get('%smodules/group/?course=%s' %(config.URL, config.COURSE))
  soupTMP = bs(sourceTMP.content, 'lxml')
  for group in soupTMP.find_all('td'):
    if (config.DATE['day'] in group.text and config.DATE['time']+'-' in group.text and 'my group' in group.text):
      return True
  return False

# Register for a lab/lecture
# Returns void
def register(day, time):
  # Labs Page Source Code
  groupsHTML = s.get('%smodules/group/?course=%s' %(config.URL, config.COURSE))
  # Beautiful Soup Setup
  soup = bs(groupsHTML.content, 'lxml')
  # Labs' Info Scraping
  a = ''
  for group in soup.find_all('td'):
    if (day in group.text and time+'-' in group.text and not 'my group' in group.text):
      reg_ele = group.find_next_siblings('td')[3]
      a = reg_ele.find('a')['href']
  # Registration
  if (a): s.get('%smodules/group/%s' %(config.URL, a))
  return
