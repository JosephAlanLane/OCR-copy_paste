# OCR-copy_paste
It's like copy/pasta (using ctlr+c and ctrl+v) but instead of copying text, it scans an image for text (ctlr+shift+q) and then pastes it (ctrl+v)
I made this because I occasionally see images with text on them and want to copy the text without rewriting it. 

Expected usage looks like this:
1. See text in an image you'd like to extract
2. Take a screenshot of the image using WindowsKey+Shift+s
3. Select the box you want to copy to the clipboard
4. Now that the image is in the clipboard, press ctrl+Shift+q (This performs the OCR)
5. Then paste like normal using ctrl+v and you will find extracted text

Optional: If you want this to run at startup you can export it as a .py or .pyw and put its shortcut in the startup folder. (.pyw is supposed to supressed cmd prompt at start up of program, but it doesn't work on my system and has little support online)
To easily open the startup folder:
1. press WindowsKey+r
2. Type into the dialogbox 'shell:startup' (without quotes)
3. copy/pasta the .py or .pyw into the startup folder 
