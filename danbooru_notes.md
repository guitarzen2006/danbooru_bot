# NOTES FROM THIS PROJECT

Download 'python-dotenv' from pypi. Use this to get environmental variables.

## DANBOORU API

<code>https://danbooru.donmai.us/profile.json?api_key=your_api_key_goes_here&login=[your user name]</code>

## TESTING SERVER

(https://testbooru.donmai.us/) - all desting needs to be done here.


## Base code of the get request for the danbooru api pic grab

```
# danbooru_api.py
from dotenv import load_dotenv
import requests
import os 

# Inialize envirnomentals
load_dotenv()

# Base URL to search for posts in json format on danbooru.donmai.us
base_url = "https://testbooru.donmai.us/posts.json?"

# API Key generated
api_key = os.getenv('TEST_API_KEY')

# login account
login = os.getenv('TEST_USERNAME')

# Number of Pics to Grab from danbooru
limit_count = "1"

url = (f'{base_url}api_key={api_key}&login={login}&limit={limit_count}')

def danbooru_pic():

    '''
    This function pulls a picture from danbooru. The payload options can be manipulated to search and pull various posts from the site.
    Be aware that with free tier you will only be able to use 2 criteria to search with. # Payload is in a 'criteria'='vlaue' pair 
    see https://testbooru.donmai.us/wiki_pages/help%3Acheatsheet for more information
    '''
    payload='random=True&tags=rating%3Asafe'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("GET", url, headers=headers, data=payload)
    
    # save json output from request as pic_grab
    pic_grab = response.json()
    
    # pic_grab is a list - slice at [0] and then at ['file_url'] for picture URL
    pic = pic_grab[0]['file_url']
    return (pic)
```