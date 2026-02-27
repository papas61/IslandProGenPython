from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import os
import base64
import openai

image_paths = []
cIndex = 0

OUTPUT_DIR = "outputs"

client = openai.OpenAI(api_key = 'sk-proj-')

def generate_ideas(user_text, n):
    prompt = f"Give me {n} creative ideas for islands about: {user_text}\n" \
             f"Return ONLY {n} lines. NO numbering, NO bullets, NO emojis!!"

    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    ideas = []

    for line in resp.choices[0].message.content.splitlines():
        print(line)

        if line != "":
            ideas.append(line)
    return ideas[:n]

def generate_images_from_ideas(ideas):
    paths = []

    for i in range(len(ideas)):
        idea = ideas[i]
        print(idea)
        img = client.images.generate(
            model="dall-e-3",
            prompt=idea,
            size="1024x1024",
            n=1
        )

        url = img.data[0].url
        print(url)

def generate_images_from_ideas2(ideas):
    paths = []
    for i in range(len(ideas)):
        idea = ideas[i]

        img = client.images.generate(
            model="gpt-image-1.5",
            prompt=ideas[i],
            size="1024x1024",
            n=1,
            output_format="jpeg"
        )

        filepath = os.path.join(OUTPUT_DIR, f"request_{i+1}.jpg")

        b64 = img.data[0].b64_json
        print(b64)

        with open(filepath, "wb") as f:
            f.write(base64.b64decode(b64))

        paths.append(filepath)

    return paths

def showImage(ind):
    global imagePreview

    img = Image.open(image_paths[ind])
    img = img.resize((400, 400), Image.Resampling.LANCZOS)
    imagePreview = ImageTk.PhotoImage(img)
    image_label.configure(image=imagePreview)

def nextImg(event=None):
    global cIndex

    cIndex = (cIndex + 1) % len(image_paths)
    showImage(cIndex)

def prevImg(event=None):
    global cIndex

    if not image_paths:
        return

    cIndex = (cIndex - 1) % len(image_paths)
    showImage(cIndex)

def preview_first():
    if image_paths == True:
        os.startfile(image_paths[0])

def process(event=None):
    global image_paths

    user = text_widget.get()
    if rb.get() == "Choice15":
        n = 3
    else:
        n = 2

    ideas = generate_ideas(user, n)
    image_paths = generate_images_from_ideas2(ideas)

    cIndex = 0
    showImage(0)

window = ThemedTk(theme="equilux")
window.configure(themebg="equilux")
window.geometry("500x800")
window.title("IslandProGen")
window.resizable(False, False)

title = ttk.Label(window, text="IslandProGen", font=("Monocraft", 20))
title.pack(anchor="center")

rb = StringVar(value="Choice5")

rad1 = ttk.Radiobutton(window, text="Short [2 Variants]", value="Choice5", variable=rb)
rad1.place(x=110, y=100)

rad2 = ttk.Radiobutton(window, text="Extended [3 Variants]", value="Choice15", variable=rb)
rad2.place(x=260, y=100)

text_widget = ttk.Entry(window, width=35, font=("Segoe UI", 15))
text_widget.place(x=50, y=150)

enter_button = ttk.Button(window, text="Enter", command=process)
enter_button.place(x=310, y=290, height=40, width=140)

preview_button = ttk.Button(window, text="Preview", command=preview_first)
preview_button.place(x=50, y=290, height=40, width=140)

image_label = ttk.Label(window)
image_label.place(x=50, y=330, width=400, height=400)

window.bind("<Left>", prevImg)
window.bind("<Right>", nextImg)

window.mainloop()
