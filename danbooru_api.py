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

# Number of Pics to Grab from danbooru
limit_count = "1"

url = (f'{base_url}api_key={api_key}&login={login}&limit={limit_count}')

def danbooru_pic():

    '''
    This function pulls a picture from danbooru. The payload options can be manipulated to search and pull various posts from the site.
    Be aware that with free tier you will only be able to use 2 criteria to search with. # Payload is in a 'criteria'='vlaue' pair 
    see https://testbooru.donmai.us/wiki_pages/help%3Acheatsheet for more information
    '''
    payload='random=True&tags=order%3Aranking'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("GET", url, headers=headers, data=payload)
    
    # save json output from request as pic_grab
    pic_grab = response.json()
    
    # pic_grab is a list - slice at [0] and then at ['file_url'] for picture URL, if it does not exist send 'preview_file_url'
    try:
        pic = pic_grab[0]['file_url']
        source = pic_grab[0]['source']
        message = (f'You can find this pic at this url: {source} \n')
    except:
        pic = 'Sorry Senpai, there was an issue with the request. 悪い、先輩。残念リクエストが失敗しました'
        message = None 
    return (message, pic)

if __name__ == "__main__":
    print(danbooru_pic())
