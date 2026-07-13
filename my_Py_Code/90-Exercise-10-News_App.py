#News App  
#Use the newsapi and requests module to fetch the daily news related to different topics.
#Go to: https://newsapi.org/
#and explore variation options to built you application

import requests

API_KEY = "049dfd5f2e854bf2b8d03d48df97e10e"

print("Choose a News Category:")
print("1. Business")
print("2. Entertainment")
print("3. General")
print("4. Health")
print("5. Science")
print("6. Sports")
print("7. Technology")

choice = input("Enter your choice (1-7): ")

categories = {
    "1": "business",
    "2": "entertainment",
    "3": "general",
    "4": "health",
    "5": "science",
    "6": "sports",
    "7": "technology"
}

category = categories.get(choice)

if category:
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "category": category,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        news = response.json()

        print(f"\nTop {category.capitalize()} News:\n")

        for i, article in enumerate(news["articles"], start=1):
            print(f"{i}. {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"URL: {article['url']}")
            print("-" * 60)
    else:
        print("Error:", response.status_code)
else:
    print("Invalid Choice!")