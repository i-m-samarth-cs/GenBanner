GenBanner 
=========

This **Promotional Content Generator** is a Python-based solution designed to create dynamic promotional banners with various themes and offers. The project allows the generation of banners with product images, promotional text, and customized themes, which can be compiled into a video for marketing or advertising purposes.

### Key Features:
- **Gradient Backgrounds**: Automatically generates visually appealing gradient backgrounds.
- **Dynamic Offer Text**: Adds promotional offers such as discounts, buy-one-get-one-free, and more.
- **Custom Themes**: Supports multiple themes like Diwali, Christmas, Independence Day, etc.
- **Product Images**: Supports overlaying product images from local directories.
- **Video Generation**: Combines the generated banners into a video using `MoviePy`.

---

## Technologies Used

- **Python (3.12)**: The primary programming language for the project.
- **PIL (Pillow)**: For image manipulation, including text, images, and background effects.
- **MoviePy**: Used for video creation from individual banner images.
- **NumPy**: Helps in image data manipulation for video frame conversion.
- **OS**: Provides functionality for file system operations such as loading images from directories.
- **ImageFont (TTF)**: For custom font rendering in banners.
- **Random**: For random selection of images, offers, and themes.

---

## Installation

### Prerequisites:
Ensure you have the following Python libraries installed:
- `Pillow`
- `MoviePy`
- `NumPy`

You can install them using `pip`:

```bash
pip install pillow moviepy numpy
Setting Up the Project:
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/promotional-content-generator.git
Add Product Images:

Place your product images in the respective directories:
vertical-skus/
vegetables/
untagged/
horizontal-skus/
Run the Script:

Run the Python script to generate banners and video:
bash
Copy code
python app.py
Output:

The generated video will be saved as promotional_video.mp4 in the current directory.
Project Structure
php
Copy code
Promotional-Content-Generator/
├── vertical-skus/             # Directory for vertical product images
├── vegetables/                # Directory for vegetable product images
├── untagged/                  # Directory for untagged product images
├── horizontal-skus/           # Directory for horizontal product images
├── app.py                     # Main Python script to run the project
├── Bigbasket.py               # Contains the promotional content generator class
├── requirements.txt           # List of Python dependencies
└── README.md                  # This file
How the Project Works:
Loading Product Images: The product images from the specified directories are loaded using the Pillow library and stored for random selection.

Banner Generation:

The generate_banner() method creates banners by applying a gradient background, overlaying images, and adding theme-specific text and graphical elements (e.g., fireworks, Diya, Christmas tree).
The banner also includes a promotional offer randomly selected from a predefined list.
Video Creation:

MoviePy is used to convert each banner into a video clip, with each frame displaying a banner.
The clips are concatenated to form a video, which is saved as promotional_video.mp4.
Future Enhancements:
AI-based Image Selection: Integrating AI tools to automatically select the most visually appealing product images based on theme and design.
Customizable Templates: Allowing users to define custom templates or layouts for banners.
Dynamic Text Generation: Use NLP to generate customized promotional text based on product categories or sales events.
Cloud Storage Integration: Allow loading product images from cloud storage (e.g., Google Drive or AWS S3).
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -am 'Add new feature').
Push to your branch (git push origin feature-branch).
Create a pull request.
Acknowledgments
Pillow (PIL): For image manipulation.
MoviePy: For video processing.
NumPy: For numerical operations on image data.
Font Resources: For custom fonts used in banners.
