# Background Remover Project

A web application built with Django that allows users to upload images and remove backgrounds automatically.

## Features

- Upload images in various formats (JPG, PNG, etc.)
- Automatic background removal using rembg library
- Download processed images with transparent backgrounds
- User-friendly interface
- Mobile responsive design

## Technologies Used

- Django
- Python
- rembg (for background removal)
- OpenCV
- Pillow (Python Imaging Library)
- HTML/CSS

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/maheshh-v/Bgremover-prjct.git
   cd Bgremover-prjct
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Visit `http://127.0.0.1:8000/` in your browser.

## Usage

1. Upload an image through the web interface
2. The application will automatically process the image and remove the background
3. Download the processed image with a transparent background

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- GitHub: [@maheshh-v](https://github.com/maheshh-v) 