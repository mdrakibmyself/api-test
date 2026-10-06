import requests
import json
import pdb 
url = "https://jsonplaceholder.typicode.com/posts"

try:
    #fetch the data
    response = requests.get(url)
    response.raise_for_status() #Check for errors
    
    #3. parse the data
    posts = response.json()
    print(f"Successfully fetched {len(posts)} posts.\n")
    
    for post in posts[:2]:
        print(f"ID {post['id']}: {post['title']}")
        
        
except Exception as e:
    print(f"Failec to fetch posts: {e}")