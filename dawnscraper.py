from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os


from utils import ImgUtils,TextUtils


load_dotenv()
link = os.getenv("LINK")
folder = os.getenv("FOLDER")
htmlpath = os.getenv("HTMLPATH")
resultpath = os.getenv("RESULTPATH")


html_doc = requests.get(link).text

soup = BeautifulSoup(html_doc, 'html.parser')
newslines = soup.select('h2 a.story__link')
fullnews = ""

for news in newslines:
    fullnews+=news.get_text().replace("\n","")
    fullnews+="\n"

TextUtils.textSave(text=html_doc,destination=htmlpath)
TextUtils.textSave(text=fullnews,destination=resultpath)


images = soup.select("img.lazyload")
print(type(images))
imglist=ImgUtils.imgList(images)



# ImgUtils.imgDownloader(imglist,folder_path=folder)
