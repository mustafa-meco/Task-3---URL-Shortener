import tkinter as tk
import pyshorteners
import pyperclip
import validators

# Dictionary to store custom short URLs
custom_urls = {}

def shorten_url(event=None):
    long_url = url_entry.get()
    custom_url = custom_entry.get()
    
    if custom_url:
        if custom_url in custom_urls:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Custom URL already in use")
        elif validators.url(long_url):
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(long_url)
            result_entry.delete(0, tk.END)
            result_entry.insert(0, short_url)
            custom_urls[custom_url] = short_url
        else:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Invalid URL")
    else:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Custom URL is required")

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

custom_label = tk.Label(window, text="Custom Short URL (Optional):")
custom_label.pack(pady=10)

custom_entry = tk.Entry(window, width=20)
custom_entry.pack()

shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

result_label = tk.Label(window, text="Shortened URL:")
result_label.pack()

result_entry = tk.Entry(window, width=40)
result_entry.pack()

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Bind the Enter key to trigger the "Shorten URL" button
url_entry.bind("<Return>", shorten_url)

# Start the main loop
window.mainloop()
