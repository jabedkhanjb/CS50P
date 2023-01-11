import re
url = input("URL: ").strip()
 
if match := re.search(r"^(?:https?://)?(?:www\.)?(?:twitter|hackerrank|linkedin|instagram|snapchat|soundcloud|youtube)\.(?:com|org|net)/(?:in/)?([a-z0-9_]+)", url):
    print(f"Username: ", match.group(1))
else:
    print("Invalid URL")