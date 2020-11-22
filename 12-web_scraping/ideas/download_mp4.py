#! python3
# download_mp4.py - Download mp4 videos from website.

import requests
import bs4
from pathlib import Path
import sys
import os

url = sys.argv[1]
url = url if url.startswith('https://') else 'https://' + url

folder_name = Path(Path(url).name)
os.makedirs(folder_name, exist_ok=True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

video_links = [link.get('src') for link in soup.select(
    'video source') if link.get('src').endswith('.mp4')]

for i, video_link in enumerate(video_links):
    res = requests.get(video_link)

    print(f'Downloading {video_link}...')
    with open(folder_name / (str(i) + '.mp4'), 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
    #     for chunk in res.iter_content(100000):
    #         f.write(chunk)
