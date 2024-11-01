import time
import pyautogui
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

screen_hight = pyautogui.size().height
screen_width = pyautogui.size().width

def take_screenshot():
    # Get current datetime for filename and watermark 
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    folder_path = f'screenshots/{datetime.now().strftime('%B-%d-%Y')}'

    # Create screenshots directory if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Take screenshot and save
    screenshot = pyautogui.screenshot()
    
    rectangle_size = (400, 54)
    lift_from_bottom = 200
    away_from_right = 200

    # Add watermark
    draw = ImageDraw.Draw(screenshot)
    # Load a TrueType font
    font_path = "arial.ttf"  # You can change this to the path of your preferred font
    base_font_size = 20
    font = ImageFont.truetype(font_path, base_font_size)
    # (format: week day, date month year, hour)
    text = f"{datetime.now().strftime('%A, %d %B %Y, %H:%M:%S')}"
    print(screenshot.size)

    # drawing rectangle on the screenshot
    draw.rectangle([(screen_width-rectangle_size[0]-away_from_right, screen_hight-rectangle_size[1]-lift_from_bottom), (screen_width-away_from_right, screen_hight-lift_from_bottom)], fill=(0, 154, 0), width=2, outline=(255, 255, 255))

    # drawing text on the screenshot
    textbbox = draw.textbbox((screen_width-rectangle_size[0]-away_from_right, screen_hight-rectangle_size[1]-lift_from_bottom), text, font=font)
    
    textwidth, textheight = textbbox[2] - textbbox[0], textbbox[3] - textbbox[1]
    width, height = screenshot.size
    x = screen_width - rectangle_size[0] - away_from_right + 25
    y = screen_hight - rectangle_size[1] - lift_from_bottom + 16

    # Increase the text width by 10%
    increased_font_size = int(base_font_size * 1.1)
    increased_font = ImageFont.truetype(font_path, increased_font_size)
    draw.text((x, y), text, font=increased_font, fill=(255, 255, 255))
    
    # Save the screenshot with watermark
    filename = f'{folder_path}/screenshot_{timestamp}.png'
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")

if __name__ == "__main__":
    
    while True:
        take_screenshot()
        # sleep for 1 minute
        time.sleep(60)