import requests
api='a58181b16636418e84eff9567c96e1ca'
query=input("what type of news are you intersted today:")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-28&sortBy=publishedAt&apiKey={api}"

print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]
for index, article in enumerate(articles):
     print(index+1,article["title"],article["url"])
     print("\n*************************************\n")