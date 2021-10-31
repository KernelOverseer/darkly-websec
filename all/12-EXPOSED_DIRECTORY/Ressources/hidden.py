import requests
import re

link_regex = re.compile(r"^<a href=\"(.*)\">", re.MULTILINE)
links = ""
results = []
def browse_page(url):
    page = requests.get(url).text
    dirs = link_regex.findall(page)
    for dr in dirs:
        if '/' in dr and dr != '../':
            new_url = url + dr
            browse_page(new_url)
        else:
            file_url = url + dr
            result = requests.get(file_url).text
            if result not in results:
                results.append(result)
                print(result)
browse_page('http://10.11.100.138/.hidden/')
