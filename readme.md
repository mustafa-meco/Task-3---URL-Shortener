# URL Shortener Project

The URL Shortener project is a simple Python application that allows you to shorten long URLs, making them more manageable and shareable. It includes features such as URL validation, URL shortening using an external service, generating QR codes for the shortened URLs, and the ability to copy the shortened URL to the clipboard.

## Features

1. **URL Shortening**: Enter a long URL, click the "Shorten URL" button, and get a shortened URL in seconds.

2. **URL Validation**: The application validates URLs to ensure that they are well-formed before shortening.

3. **QR Code Generation**: Create QR codes for the shortened URLs to make sharing easy.

4. **Clipboard Copy**: One-click copying of shortened URLs to your clipboard for quick sharing.

5. **Cache**: The project utilizes an in-memory cache to store previously shortened URLs for faster retrieval.

6. **User-Friendly Interface**: The graphical user interface is developed using Tkinter, ensuring a simple and intuitive user experience.

## Prerequisites

Before using the project, make sure you have the following prerequisites:

- Python (3.x recommended)
- Required Python libraries: `tkinter`, `pyshorteners`, `pyperclip`, `validators`, `qrcode`, `Pillow` (PIL), and `cachetools`.

## Getting Started

1. **Shorten a URL**: Enter the long URL that you want to shorten.

2. **Validation**: The application validates the URL to ensure it's well-formed.

3. **Shorten**: Click the "Shorten URL" button to generate the shortened URL.

4. **QR Code**: Optionally, generate a QR code for the shortened URL by clicking the "Generate QR Code" button.

5. **Copy to Clipboard**: Click "Copy to Clipboard" to quickly copy the shortened URL.

## Usage

1. Run the application by executing the Python script.

2. Enter a long URL and click the "Shorten URL" button.

3. Optionally, click "Generate QR Code" to create a QR code for the shortened URL.

4. Click "Copy to Clipboard" to easily share the shortened URL.

## Customization

You can customize the project further by modifying the user interface, adding additional features, or integrating with different URL shortening services.

## Acknowledgments

This project utilizes various Python libraries, including Tkinter for the user interface, pyshorteners for URL shortening, and pyperclip for clipboard operations.

## Author

Mustafa Ghoneim - [LinkedIn](https://www.linkedin.com/in/mustafa-gamal739/)

## Note

Please note that this project is intended for educational and demonstration purposes. When using URL shorteners, be cautious and consider potential security and privacy implications, as well as the reliability of the shortening service.
