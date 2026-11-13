import json
import time
from PIL import Image
from websocket import create_connection

# --- CONFIGURATION ---
IMAGE_PATH = "pixel_art.png"  
DELAY_BETWEEN_PIXELS = 0.05   # Increased delay to 0.05 (20 pixels/sec) to avoid bans
# ---------------------

def rgb_to_decimal(r, g, b):
    return (r << 16) + (g << 8) + b

def draw_image():
    print("=== Pixel Art Automator ===")
    ws_url = input("1. Enter your full WebSocket URL: ").strip()
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
        ws = create_connection(ws_url, cookie=cookie_string)
    except Exception as e:
        print(f"Failed to connect to server: {e}")
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
            
            # --- NEW AUTO-RECONNECT LOGIC ---
            while True:
                try:
                    ws.send(json.dumps(payload))
                    break  # Success! Break out of the retry loop and move to the next pixel
                except Exception as e:
                    print(f"\n[!] Connection dropped by server: {e}")
                    print("Waiting 5 seconds before reconnecting...")
                    time.sleep(5)
                    
                    try:
                        # Attempt to rebuild the connection using the same URL and cookie
                        ws = create_connection(ws_url, cookie=cookie_string)
                        print("[+] Reconnected! Resuming drawing...")
                    except Exception:
                        pass # If reconnection fails, the while loop will catch it and try again
            # --------------------------------
            
            pixels_placed += 1
            time.sleep(DELAY_BETWEEN_PIXELS) 

    ws.close()
    print(f"Finished! Successfully placed {pixels_placed} pixels.")

if __name__ == "__main__":
    draw_image()