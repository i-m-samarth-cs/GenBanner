import random
import os
from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mp
import numpy as np

class PromotionalContentGenerator:
    def __init__(self):
        self.product_images = []
        self.promotional_offers = [
            "MAX ₹99 OFF", "UP TO 60% OFF", "UNDER ₹999", "MIN ₹10 OFF",
            "MIN 20% OFF", "STARTS @₹99", "FLAT ₹100 OFF", "FLAT 20% OFF",
            "₹499 STORE", "BUY 2 GET 1 FREE"
        ]
        self.themes = ["Diwali", "Independence Day", "Christmas", "New Year", "Summer Sale"]
        self.color_palettes = [
            ['#FF5733', '#FFC300', '#DAF7A6'],  # Warm
            ['#3498DB', '#85C1E9', '#D6EAF8'],  # Cool
            ['#27AE60', '#82E0AA', '#D5F5E3'],  # Fresh
            ['#8E44AD', '#BB8FCE', '#E8DAEF'],  # Royal
            ['#E74C3C', '#F1948A', '#FADBD8']   # Vibrant
        ]
        self.output_specs = {'width': 1360, 'height': 800, 'format': 'png'}

    def load_product_images(self, image_paths):
        for path in image_paths:
            img = Image.open(path)  # Open images from local file paths
            self.product_images.append(img)

    def generate_gradient_background(self):
        palette = random.choice(self.color_palettes)
        background = Image.new('RGB', (self.output_specs['width'], self.output_specs['height']))
        draw = ImageDraw.Draw(background)
        for i in range(len(palette)):
            start = i / len(palette)
            end = (i + 1) / len(palette)
            for y in range(int(start * self.output_specs['height']), int(end * self.output_specs['height'])):
                color = self.interpolate_color(palette[i], palette[(i+1) % len(palette)], 
                                               (y - start * self.output_specs['height']) / (self.output_specs['height'] / len(palette)))
                draw.line([(0, y), (self.output_specs['width'], y)], fill=color)
        return background

    def interpolate_color(self, color1, color2, factor):
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        r = int(r1 + factor * (r2 - r1))
        g = int(g1 + factor * (g2 - g1))
        b = int(b1 + factor * (b2 - b1))
        return f'#{r:02x}{g:02x}{b:02x}'

    def apply_theme(self, banner, theme):
        draw = ImageDraw.Draw(banner)
        theme_title_font = ImageFont.truetype("arialbd.ttf", 60)  # Bold font for theme title
        offer_font = ImageFont.truetype("arial.ttf", 36)  # Regular font for offer text

        # Theme-specific title and colors
        if theme == "Diwali":
            theme_color = '#FF9900'
            theme_title = "Happy Diwali!"
            self.draw_diya(draw)
        elif theme == "Independence Day":
            theme_color = '#138808'
            theme_title = "Independence Day Sale"
            self.draw_flag(draw)
        elif theme == "Christmas":
            theme_color = '#FF0000'
            theme_title = "Merry Christmas!"
            self.draw_christmas_tree(draw)
        elif theme == "New Year":
            theme_color = '#1E90FF'
            theme_title = "New Year Special!"
            self.draw_fireworks(draw)
        elif theme == "Summer Sale":
            theme_color = '#FFD700'
            theme_title = "Summer Sale Madness"
            self.draw_sun(draw)

        # Position and style the theme title
        title_bbox = draw.textbbox((0, 0), theme_title, font=theme_title_font)
        title_width, title_height = title_bbox[2] - title_bbox[0], title_bbox[3] - title_bbox[1]
        title_position = ((self.output_specs['width'] - title_width) // 2, 50)
        draw.text(title_position, theme_title, fill=theme_color, font=theme_title_font)

        return draw

    def draw_diya(self, draw):
        draw.ellipse([100, 700, 200, 750], fill='orange', outline='yellow')
        draw.polygon([150, 680, 130, 700, 170, 700], fill='red')

    def draw_flag(self, draw):
        colors = ['#FF9933', '#FFFFFF', '#138808']
        for i, color in enumerate(colors):
            draw.rectangle([1200, 100 + i*50, 1300, 150 + i*50], fill=color)

    def draw_christmas_tree(self, draw):
        draw.polygon([1100, 300, 1200, 500, 1000, 500], fill='green')
        draw.rectangle([1070, 500, 1130, 600], fill='brown')

    def draw_fireworks(self, draw):
        draw.line([300, 200, 500, 200], fill='red', width=5)
        draw.line([400, 100, 400, 300], fill='blue', width=5)

    def draw_sun(self, draw):
        draw.ellipse([1200, 100, 1300, 200], fill='yellow')

    def generate_banner(self, offer, theme):
        background = self.generate_gradient_background()

        # Place multiple product images on the banner
        if self.product_images:
            num_products = random.randint(2, 4)
            x_pos = 50
            for i in range(num_products):
                product_image = random.choice(self.product_images)
                product_image.thumbnail((self.output_specs['width'] // 3, self.output_specs['height'] // 3))
                background.paste(product_image, (x_pos, 150), product_image if product_image.mode == 'RGBA' else None)
                x_pos += product_image.width + 20

        # Apply the randomly chosen theme to the banner
        draw = self.apply_theme(background, theme)

        # Add the promotional offer text
        offer_font = ImageFont.truetype("arial.ttf", 36)
        text_bbox = draw.textbbox((0, 0), offer, font=offer_font)
        text_position = ((self.output_specs['width'] - text_bbox[2]) // 2, 
                         (self.output_specs['height'] - text_bbox[3]) // 2 + 100)
        draw.text(text_position, offer, fill='white', font=offer_font)

        return background

    def convert_banners_to_video(self, video_filename, num_banners=10, fps=1):
        # Choose one random theme for the entire video
        theme = random.choice(self.themes)

        # Generate banners with different offers but the same theme
        clips = []
        for _ in range(num_banners):
            offer = random.choice(self.promotional_offers)
            banner = self.generate_banner(offer, theme)
            clip = mp.ImageClip(np.array(banner))
            clip = clip.set_duration(1 / fps)
            clips.append(clip)

        video = mp.concatenate_videoclips(clips, method="compose")
        video.write_videofile(video_filename, fps=fps)

def main():
    generator = PromotionalContentGenerator()

    # Define the directories containing images
    directories = [
        r'C:\Users\samar\Desktop\Google Gen AI\vertical-skus',
        r'C:\Users\samar\Desktop\Google Gen AI\vegetables',
        r'C:\Users\samar\Desktop\Google Gen AI\untagged',
        r'C:\Users\samar\Desktop\Google Gen AI\horizontal-skus'
    ]

    # Initialize an empty list to hold all image paths
    image_paths = []

    # Loop through each directory and add image paths to the list
    for directory in directories:
        for filename in os.listdir(directory):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_paths.append(os.path.join(directory, filename))

  # Load the product images
    generator.load_product_images(image_paths)

    # Convert the banners directly to a video
    video_filename = 'C:/Users/samar/Desktop/Google Gen AI/promotional_video.mp4'
    generator.convert_banners_to_video(video_filename, num_banners=10, fps=1)

    print(f"Video saved as {video_filename}")

if __name__ == '__main__':
    main()
