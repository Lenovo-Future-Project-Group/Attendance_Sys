import requests
import json, re
from multiprocessing.dummy import Pool as ThreadPool


class Ts():
    def __init__(self, site, token, path):
        self.site = site
        self.token = token
        self.path = path

    def api(self, url):
        print(f">>> 正在向百度推送链接-- {url} ..")
        post_url = f"http://data.zz.baidu.com/urls?site={self.site}&token={self.token}"
        headers = {
            'User-Agent': 'curl/7.12.1',
            'Host': 'data.zz.baidu.com',
            'Content-Type': 'text/plain',
            'Content-Length': '83',
        }
        response = requests.post(post_url, headers=headers, data=url)
        req = response.text
        if "success" in req:
            print(f"恭喜，{url} -- 百度推送成功！")
            req_json = json.loads(req)
            print(f'当天剩余的可推送url条数: {req_json["remain"]}')

        else:
            print(f"{url} -- 百度推送失败！")

        return None

    def get_url(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            xml_data = f.read()

        print(">>> 读取网站地图文件成功！")

        urls = re.findall(r'<loc>(.+?)</loc>', xml_data, re.S)
        print(urls)
        print(f">>> 共有网页链接数 ：{len(urls)} 条!")

        return urls

    def main(self):
        urls = self.get_url()
        try:
            # 开4个 worker，没有参数时默认是 cpu 的核心数
            pool = ThreadPool()
            results = pool.map(self.api, urls)
            pool.close()
            pool.join()
            print(">> 采集所有链接百度推送完成！")

        except Exception as e:
            print(f'错误代码：{e}')
            print("Error: unable to start thread")


if __name__ == '__main__':
    site = "https://www.fymjcl.top"
    token = "OxFlzat9l5ew68BM"
    path = r"C:\Users\Administrator\PycharmProjects\pythonProject\交付版本v3-添加模版\sitemap.xml"
    spider = Ts(site, token, path)
    spider.main()

