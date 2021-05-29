# danbooru_api.py
from dotenv import load_dotenv
import requests
import os 


# Inialize envirnomentals
load_dotenv()

# Base URL to search for posts in json format on danbooru.donmai.us
base_url = "https://safebooru.donmai.us/posts.json?"

# API Key generated
api_key = os.getenv('API_KEY')

# login account
login = os.getenv('USERNAME')

def danbooru_pic(limit_count):

    '''
    This function pulls a picture from danbooru. The payload options can be manipulated to search and pull various posts from the site.
    Be aware that with free tier you will only be able to use 2 criteria to search with. # Payload is in a 'criteria'='vlaue' pair 
    see https://testbooru.donmai.us/wiki_pages/help%3Acheatsheet for more information
    '''
    # This conditional is to stop a request of over 10 pics

    url = (f'{base_url}api_key={api_key}&login={login}&limit={limit_count}')
    
    payload='tags=order%3Arandom+score%3A>75'
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    # save json output from request as pic_grab
    pic_grab = response.json()
    return (pic_grab)

if __name__ == "__main__":
    print(type(danbooru_pic()))