import re
url = input("URL: ").strip()
 
if match := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url):
    print(f"Username: ", match.group(1))
else:
    print("Invalid URL")