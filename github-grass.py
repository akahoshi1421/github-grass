import re
import requests
from bs4 import BeautifulSoup as bs4
from tkinter import messagebox

res = requests.get("https://github.com/akahoshi1421")
soup = bs4(res.content, "html.parser")
rect = soup.select(".js-calendar-graph-svg rect")
commit = rect[len(rect) - 1].get("data-count")

if commit == "0":
    messagebox.showinfo("GitHub草警察", "まだ今日の分のcommitが完了していません")
