import os
import requests
from html.parser import HTMLParser

class ImageExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image_urls = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    self.image_urls.append(value)

def download_images(url, output_dir='images'):
    """
    Download all images from a given webpage and save them as JPEG files.

    Parameters:
    url (str): The URL of the webpage to download images from.
    output_dir (str): The directory to save the downloaded images (default is 'images').
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Fetch the webpage content
    response = requests.get(url)
    extractor = ImageExtractor()
    extractor.feed(response.text)

    # Download and save each image
    for i, image_url in enumerate(extractor.image_urls):
        try:
            image_response = requests.get(image_url)
            image_filename = os.path.join(output_dir, f'image_{i+1}.jpg')
            with open(image_filename, 'wb') as file:
                file.write(image_response.content)
            print(f'Downloaded and saved {image_filename}')
        except requests.exceptions.RequestException as e:
            print(f'Error downloading image: {e}')

# Example usage
download_images('https://unsplash.com/s/photos/dark-food-photography')