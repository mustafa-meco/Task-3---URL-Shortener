import tkinter as tk
import pyshorteners
import pyperclip
import validators
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog
from cachetools import Cache, LRUCache

# Create an in-memory cache with a maximum size
url_cache = LRUCache(maxsize=1000)

def unpack_widgets():
    result_label.pack_forget()
    result_entry.pack_forget()
    copy_button.pack_forget()
    generate_qr_button.pack_forget()
    qr_code_label.pack_forget()
    save_qr_button.pack_forget()

def generate_qr_code_image(url):
    global img
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return ImageTk.PhotoImage(img)

def update_qr_code():
    url = result_entry.get()
    if validators.url(url):
        qr_code_image = generate_qr_code_image(url)
        qr_code_label.config(image=qr_code_image)
        qr_code_label.photo = qr_code_image
        qr_code_label.pack(pady=10)
        save_qr_button.pack(pady=10)
    else:
        qr_code_label.config(image=None)

def save_qr_code():
    global img
    url = url_entry.get()
    if validators.url(url):
        qr_code_image = generate_qr_code_image(url)
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            img.save(file_path)

def shorten_url_cache(long_url):
    # Check if the shortened URL is in the cache
    if long_url in url_cache:
        return url_cache[long_url]

    # If not in the cache, generate the shortened URL
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)

    # Store the shortened URL in the cache
    url_cache[long_url] = short_url
    return short_url


def shorten_url(event=None):
    unpack_widgets()
    long_url = url_entry.get()
    result_label.pack()
    result_entry.pack()
    
    if validators.url(long_url):
        short_url = shorten_url_cache(long_url)
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, short_url)
        result_entry.config(state="readonly")
        
        copy_button.pack(pady=10)
        generate_qr_button.pack(pady=10)
    else:
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid URL")
        result_entry.config(state="readonly")

    

def copy_to_clipboard():
    short_url = result_entry.get()
    pyperclip.copy(short_url)

# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Create and place widgets
url_label = tk.Label(window, text="Enter the URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(window, width=40)
url_entry.pack()

shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

result_label = tk.Label(window, text="Shortened URL:")


result_entry = tk.Entry(window, width=40)


copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)


qr_code_label = tk.Label(window)


generate_qr_button = tk.Button(window, text="Generate QR Code", command=update_qr_code)


save_qr_button = tk.Button(window, text="Save QR Code", command=save_qr_code)


# Bind the Enter key to trigger the "Shorten URL" button
url_entry.bind("<Return>", shorten_url)

# Start the main loop
window.mainloop()
