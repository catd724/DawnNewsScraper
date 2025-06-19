from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


from utils import ImgUtils,TextUtils,ProxyUtils


ProxyUtils.findProxies(refreshFile=False)
proxylist = ProxyUtils.getProxies()


load_dotenv()
link = os.getenv("LINK")
folder = os.getenv("FOLDER")
htmlpath = os.getenv("HTMLPATH")
resultpath = os.getenv("RESULTPATH")



html_doc = ProxyUtils.request_with_proxies(url=link,proxy_list=proxylist).text
# print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')
newslines = soup.select('h2 a.story__link')
images = soup.select("img.lazyload")


fullnews = ""
for news in newslines:
    fullnews+=news.get_text().replace("\n","")
    fullnews+="\n"

TextUtils.textSave(text=html_doc,destination=htmlpath)
TextUtils.textSave(text=fullnews,destination=resultpath)

imglist=ImgUtils.imgList(images)



ImgUtils.imgDownloader(imglist,folder_path=folder,proxylist=proxylist)
