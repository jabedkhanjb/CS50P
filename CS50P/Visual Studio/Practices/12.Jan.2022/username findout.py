import re

url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?(?:twitter|email|instagram|facebook)\.(?:com|org|net|edu|bd)/(?:in/)?([a-z0-9_.]+)", url, re.IGNORECASE):
    print("Username: ", matches.group(1))
else:
    print("Invalid URL")