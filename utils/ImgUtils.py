import os
import bs4
import requests


def imgDownloader(imglist,folder_path):
    # Create a folder for images
    os.makedirs(folder_path, exist_ok=True)

    # Download each image
    for i, url in enumerate(imglist, 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise error for bad status codes

            # Extract filename from URL
            filename = url.split("/")[-1].split("?")[0]
            filepath = os.path.join(folder_path, filename)

            # Write image to file
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"[{i}] Downloaded: {filename}")
        except Exception as e:
            print(f"[{i}] Failed to download: {url} ({e})")



def imgList(images):
    imglist=[]
    for img in images:
        link = (img.get("data-src") or img.get("src"))
        if link is not None:
            imglist.append(link)
    imglist = set(imglist)
    print("length of the image list is", len(imglist))
    return list(imglist)