from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw, ImageFont
import threading
import time
import requests
import json
from PIL import ImageFont
url = "http://starts.sytes.net:7890/get_temp_now"

def get_temp():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if response.status_code == 200:
                data = json.loads(response.text)
                temperatura = float(data["temp"])
                return temperatura
        return 0
    except requests.RequestException as e:
        return 0

def make_number_icon(number):
    img = Image.new('RGBA', (64,64), color=(0,0,0,0))
    fnt = ImageFont.truetype("arial.ttf", 55)  
    d = ImageDraw.Draw(img)
    d.text((0,0), f"{number:00}", font=fnt, fill='white')
    return img

def update_icon(icon, _=None):
    count = get_temp()
    icon.icon = make_number_icon(count)

icon = icon("Pystray test",
            icon=make_number_icon(0),
            menu=menu(item("Atualizar ", update_icon),
                      item("Sair", icon.stop)))

def update_periodically_forever():
    global icon
    while True:
        update_icon(icon)
        time.sleep(60) 

update_thread = threading.Thread(target=update_periodically_forever, daemon=True)
update_thread.start()

icon.run()