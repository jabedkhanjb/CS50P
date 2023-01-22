import re

url = input("URL: ").strip()
if match:= re.search(r"^(?:https?://)?(?:www\.)?(?:[a-z0-9]+)\.(?:com|org|net|edu|bd|it|to)/(?:@)?([a-z0-9._]+)", url, re.IGNORECASE):
    print(f"Username: {match.group(1)}")
else:
    print("Invalid URL")
    
    