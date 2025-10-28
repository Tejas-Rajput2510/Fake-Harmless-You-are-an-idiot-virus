import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import pygame
import random

# 🔊 Play looping audio
def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("idiot.mp3")
    pygame.mixer.music.play(-1)

# ⚡ Flash image using after()
def flash(label, img1, img2, state=[True]):
    label.config(image=img1 if state[0] else img2)
    label.image = img1 if state[0] else img2
    state[0] = not state[0]
    label.after(500, flash, label, img1, img2, state)

# 🪟 Create popup window with smooth movement
def create_popup(master):
    popup = tk.Toplevel(master)
    popup.title("You Are An Idiot")
    popup.resizable(False, False)
    popup.geometry("400x300")

    img = Image.open("idiot.png").resize((300, 200))
    inverted = ImageOps.invert(img.convert("RGB"))

    tk_img = ImageTk.PhotoImage(img, master=popup)
    tk_inverted = ImageTk.PhotoImage(inverted, master=popup)

    label = tk.Label(popup, image=tk_img)
    label.image = tk_img
    label.pack(pady=10)

    text = tk.Label(popup, text="You are an idiot", font=("Helvetica", 16, "bold"))
    text.pack()

    flash(label, tk_img, tk_inverted)

    # 🕺 Smooth movement variables
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = random.randint(0, screen_width - 400)
    y = random.randint(0, screen_height - 300)
    dx = random.choice([-3, 3])
    dy = random.choice([-3, 3])

    def move():
        nonlocal x, y, dx, dy
        x += dx
        y += dy

        # Bounce off edges
        if x <= 0 or x >= screen_width - 400:
            dx = -dx
        if y <= 0 or y >= screen_height - 300:
            dy = -dy

        popup.geometry(f"400x300+{x}+{y}")
        popup.after(30, move)

    move()

# 🔁 Launch popups endlessly
def launch_endless_popups(master, delay=1000):
    def summon():
        create_popup(master)
        master.after(delay, summon)
    summon()

# 🔥 Start everything
pygame.init()
root = tk.Tk()
root.withdraw()
play_audio()
launch_endless_popups(root, delay=1000)  # One new dancing window every second
root.mainloop()
