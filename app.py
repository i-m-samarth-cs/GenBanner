from flask import Flask, render_template, request, jsonify
import random
import os
from Bigbasket import PromotionalContentGenerator  # Import your class

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the front-end

@app.route('/generate-video', methods=['POST'])
def generate_video():
    directories = request.json.get('directories')
    num_banners = request.json.get('num_banners', 10)
    fps = request.json.get('fps', 1)
    
    generator = PromotionalContentGenerator()

    # Load product images from directories
    image_paths = []
    for directory in directories:
        for filename in os.listdir(directory):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_paths.append(os.path.join(directory, filename))
    
    generator.load_product_images(image_paths)

    random_number = random.randint(1000, 9999)
    video_filename = f'static/promotional_video_{random_number}.mp4'

    # Generate video
    generator.convert_banners_to_video(video_filename, num_banners=num_banners, fps=fps)

    return jsonify({'video_url': video_filename})

if __name__ == '__main__':
    app.run(debug=True)
