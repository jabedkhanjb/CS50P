import re
url = input("URL: ").strip()

if matches := re.search(r"https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):

    print(f"Username: ", matches.group(1))
else:
    print("Username: Invalid URL")

# inside a parenthesis ?: means not to capture those parenthesis