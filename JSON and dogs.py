from tkinter import *
import requests
from tkinter import messagebox as mb
from PIL import Image, ImageTk
from io import BytesIO

from bottle import response
from pygame.examples.cursors import image

def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream = True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300))
            label.config(image = img)
            label.image = img
        except Exception as e:
            mb.showerror('Ошибка!', f'Возникла ошибка: {e}')

window = Tk()
window.title('Картинки с "собатшками"')
window.geometry('360x420')

label = Label()
label.pack(pady = 10)

button = Button(text = 'Загрузить изображение', command = show_image)
button.pack(pady = 10)

window.mainloop()
