import requests

api_key = 'e70af12a746d4e02b06d85b58ea79de5'

# url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-02-28&sortBy=publishedAt&apiKey=e70af12a746d4e02b06d85b58ea79de5'

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

content = response.json()

print(content)

# for article in content['articles']:
#     print(article['title'])
#     print(article['description'])
# with open('content.txt','w') as file:
#     file.write(content)

