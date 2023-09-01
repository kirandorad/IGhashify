import requests

def generate_hashtags(keyword, num_hashtags=10):
    # Instagram API endpoint for hashtag search
    endpoint = 'https://www.instagram.com/web/search/topsearch/'

    # Create headers with user-agent to mimic a web browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Prepare the query parameters
    params = {
        'context': 'blended',
        'query': keyword
    }

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()

        # Extract hashtags from the API response
        hashtags = []
        for tag in data['hashtags'][:num_hashtags]:
            hashtags.append('#' + tag['hashtag']['name'])

        return hashtags

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        return []

if __name__ == "__main__":
    keyword = input("Enter a keyword: ")
    num_hashtags = int(input("Enter the number of hashtags to generate: "))

    hashtags = generate_hashtags(keyword, num_hashtags)

    if hashtags:
        print("Generated Hashtags:")
        for i, hashtag in enumerate(hashtags, start=1):
            print(f"{i}. {hashtag}")
    else:
        print("No hashtags found.")
