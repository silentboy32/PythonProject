import requests 
from tqdm import tqdm


#url = "https://www.kali.org/get-kali/#kali-installer-images"
#url2 = "https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux "
url3 = "https://download-cdn.jetbrains.com/python/pycharm-professional-2024.1.1.tar.gz"
url4 = input(" Enter the url")

response = requests.get(url4, stream=True)

total_size = int(response.headers.get("content-length",0))
block_size = 128

with tqdm(desc="Downloading" ,total=total_size ,unit="iB" , unit_scale=True) as progress_bar:
    with open("tom_and_jary.mkv", "wb") as f:
        for data in response.iter_content(block_size):

            progress_bar.update(len(data))
            f.write(data)


