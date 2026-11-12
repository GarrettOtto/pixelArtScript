# Script Instructions

### How to get token from your browser:

1. Go to `place.super.tukios.com`
2. Click `F12` on your keyboard
   1. This will bring up the Dev Tools
3. Click the `Network` tab on the Dev Tools sidebar
   1. If 'Reload page' pops up, click that
4. Search for 'ws' in the filter section
   1. There should be a row that displays something along these lines: 'ws?v=3?session=**session ID here**'
5. Right-click on the URL
6. Hover over `Copy`
7. Click `Copy URL`

Token Example:
`wss://place.super.tukios.com/ws?v=3&session=234cf7fe4d31beb56df4cd696c98ed47`

### How to get Cookie from your browser:

1. Go to `place.super.tukios.com`
2. Click `F12` on your keyboard
   1. This will bring up the Dev Tools
3. Click the `Network` tab on the Dev Tools sidebar
   1. If 'Reload page' pops up, click that
4. Search for 'ws' in the filter section
   1. There should be a row that displays something along these lines: 'ws?v=3?
5. Click on that row
6. Make sure you are in the `Headers` tab
7. Scroll down to where it says `Cookie`
8. Copy the long cookie to the right

Cookie Example:
`__hstc=197013171.5d304dc27f5c7aab230a071bba4da658.1780589945957.1780589945957.1780589945957.1; hubspotutk=5d304dc27f5c7aab230a071bba4da658; _ga_8Q83LVWZV3=GS2.1.s1781196708$o1$g1$t1781196735$j33$l0$h0; _ga=GA1.1.1449257683.1779284362; _ga_HYR7W91QRN=GS2.1.s1794013547$o5$g0$t1794013547$j60$l0$h0; super_session=gggerhwkrwocc4oovhbvzvffttvci2bo; _ga_9M3TSQVS19=GS2.1.s1794322533$o92$g1$t1794324338$j60$l0$h0; _ga_D43LKBQYNX=GS2.1.s1794322534$o92$g1$t1794324338$j60$l0$h0`

### How to use the script:

1. Open a terminal and run `pip install pillow websocket-client` where the script is located
2. Get an image to put into the script so it knows what to create
3. Re-Size the image to be the size that you want it. If you upload a picture with an average pixel ratio of 1080 × 1080 it will use that much space on the canvas
   1. You can do this however you want. Here is how to do it with Photoshop:
      1. Upload image into Photoshop
      2. Go to `Image > Image Size` or click `alt + ctrl + I`
      3. Change dropdown from `Inches` to `Pixels`
      4. Change the `Width` and `Height` pixels to what you want
      5. Save the file
4. Place that image into the root folder of this project (same directory where `pixelArtScript.py` is located)
5. Rename the picture to be `pixel_art.png`
   1. Make sure it is renamed as a `.png` file
6. Open the terminal where the script is located
7. Run the command by running `python pixelArtScript.py`
8. Input your token that you got earlier
9. Input where you want your drawing to be
   1. The X and Y coordinate will be the very top-left pixel of the image that you put into the project

### Prompts that could help:

- Could you help me redesign this image? I want the inside of the chess puzzle pieces to only be a few colors. Currently there are a lot of colors and since I am going to manually click every pixel on a canvas this will take me a long time if all the colors are different. Could you help me with that?
