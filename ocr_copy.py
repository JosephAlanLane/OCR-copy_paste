#!/usr/bin/env python
# coding: utf-8

# In[1]:


# If having issues with script can output an error log to troubleshoot
# import sys
# Redirect stdout and stderr to a file
# sys.stdout = open('output.log', 'w')
# sys.stderr = open('error.log', 'w')

import pytesseract

# Set the Tesseract executable path so proper .exe can be used.
# Must install Tesseract before use (not just pip install ...)
# Can be found at https://tesseract-ocr.github.io/tessdoc/Installation.html
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import ImageGrab
import pyperclip
import keyboard

def process_clipboard_image():
    img = ImageGrab.grabclipboard()
    
    # Convert the image to text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(img)
    
    # Put extracted text back into clipboard
    extracted_text = extracted_text.replace('‘','\'').replace('’','\'')
    pyperclip.copy(extracted_text)

# press ctrl+shift+q to print "Hotkey Detected"
keyboard.add_hotkey('ctrl + shift + q', process_clipboard_image)
keyboard.wait('esc')

