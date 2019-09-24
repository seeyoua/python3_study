import json
import asyncio
import aiohttp
import os
import requests
import aiofiles

PROKJECT_PATH = os.path.join(os.path.dirname(__file__), 'video')

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q = 0.9',
    'Origin': 'https://www.bilibili.com',
    'Referer': 'https://www.bilibili.com/video/av28871471',
}

down_load_headers = {
    'Origin': 'https://www.bilibili.com',
    'Referer': 'https://www.bilibili.com/video/av28871471',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


url_failed_list = []
url_success_list = []


async def get_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=5, headers=headers) as resp:
            if resp.status != 200:
                url_failed_list.append(url)
            else:
                url_success_list.append(url)
            r = await resp.text()
            return r


def extract_url(resp):
    video_detial = json.loads(resp)
    video_urls = video_detial.get('data')['durl']
    url = video_urls[0]['url']
    return url


async def down_load_video(video_url, title):
    async with aiohttp.ClientSession() as session:
        async with session.get(video_url, headers=headers) as resp:
            if not os.path.exists(PROKJECT_PATH):
                os.mkdir(PROKJECT_PATH)
            file_name = title + '.flv'
            async with aiofiles.open(os.path.join(PROKJECT_PATH, file_name), 'wb') as fd:
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break
                    await fd.write(chunk)


async def get_video_url(url, title):
    resp = await get_response(url)
    video_url = extract_url(resp)
    await down_load_video(video_url, title)


def main():
    loop = asyncio.get_event_loop()
    resp = requests.get(
        "https://api.bilibili.com/x/player/pagelist?aid=28871471&jsonp=jsonp",
        headers=headers)
    tasks = []
    if resp.status_code == 200:
        results = json.loads(resp.text)
        for result in results['data']:
            cid = result.get('cid')
            title = result.get('part')
            detail_url = "https://api.bilibili.com/x/player/playurl?avid=28871471&cid={}".format(
                cid)
            tasks.append(asyncio.ensure_future(get_video_url(detail_url, title)))
        loop.run_until_complete(asyncio.gather(*tasks))


main()
