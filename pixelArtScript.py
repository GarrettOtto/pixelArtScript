import json
import time
from PIL import Image
from websocket import create_connection

# --- CONFIGURATION ---
IMAGE_PATH = "pixel_art.png"  # Path to the image you want to upload
DELAY_BETWEEN_PIXELS = 0.02   # Rate limit in seconds
# ---------------------

def rgb_to_decimal(r, g, b):
    """Converts RGB values to the decimal integer format the server expects."""
    return (r << 16) + (g << 8) + b

def draw_image():
    print("=== Pixel Art Automator ===")
    ws_url = input("1. Enter your full WebSocket URL: ").strip()
    
    # NEW: Ask for the cookie string to pass authentication
    cookie_string = input("2. Enter your Cookie string (paste everything after 'Cookie: '): ").strip()
    
    try:
        start_x = int(input("3. Enter the starting X coordinate: "))
        start_y = int(input("4. Enter the starting Y coordinate: "))
    except ValueError:
        print("\nError: X and Y coordinates must be whole numbers. Please run the script again.")
        return

    print(f"\nLoading image from {IMAGE_PATH}...")
    try:
        img = Image.open(IMAGE_PATH).convert("RGBA")
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    width, height = img.size
    print(f"Image loaded. Size: {width}x{height} pixels.")

    print("Connecting to WebSocket server...")
    try:
        # NEW: Pass the cookie string into the connection request
        ws = create_connection(ws_url, cookie=cookie_string)
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        print("Make sure you copied the entire Cookie string from the Request Headers.")
        return

    print(f"Connection established. Drawing at ({start_x}, {start_y})...")
    pixels_placed = 0

    for y in range(height):
        for x in range(width):
            r, g, b, a = img.getpixel((x, y))
            
            if a == 0:
                continue 
                
            color_decimal = rgb_to_decimal(r, g, b)
            target_x = start_x + x
            target_y = start_y + y
            
            payload = {
                "x": target_x,
                "y": target_y,
                "c": color_decimal,
                "s": 1
            }
            
            ws.send(json.dumps(payload))
            pixels_placed += 1
            time.sleep(DELAY_BETWEEN_PIXELS) 

    ws.close()
    print(f"Finished! Successfully placed {pixels_placed} pixels.")

if __name__ == "__main__":
    draw_image()