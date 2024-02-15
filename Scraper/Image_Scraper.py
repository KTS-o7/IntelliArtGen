import argparse
import time
from bing_image_downloader import downloader

def download_images(keywords, limit, print_urls=False):
    start_time = time.time()
    downloader.download(keywords, limit=limit, output_dir='datasetScraped', adult_filter_off=True, force_replace=False, timeout=60)
    end_time = time.time()
    
    print("Time taken to download images: ", end_time - start_time, "seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download images from Bing')
    parser.add_argument('-k', '--keywords', type=str, help='Keywords for the images')
    parser.add_argument('-l', '--limit', type=int, help='Limit on number of images to download')
    parser.add_argument('-p', '--print_urls', type=bool, help='Whether to print the URLs of the downloaded images')
    
    args = parser.parse_args()
    
    download_images(args.keywords, args.limit, args.print_urls)
