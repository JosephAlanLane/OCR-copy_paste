# OCR-copy_paste
It's like copy/pasta but instead of normal text enables one to take a copied image with text in it, perform Optical Character Recognition on the image, and then outputs the text using ctrl+v

Usage looks like this:
1. See text in an image you'd like to extract
2. Take a screenshot of the image using WindowsKey+Shift+s
3. Select the box you want to copy to the clipboard
4. Now that the image is in the clipboard, press ctrl+Shift+q (This performs the OCR)
5. Then paste like normal using ctrl+v and you will find extracted text

Optional: If you want this to run at startup you can export it as a .py or .pyw and put it in the startup folder. (.pyw is supposed to supressed cmd prompt at start up of program, but it doesn't work on my system and has little support online)
To easily open the startup folder:
1. press WindowsKey+r
2. Type into the dialogbox 'shell:startup' (without quotes)
3. copy/pasta the .py or .pyw into the startup folder 
