import argparse
import time
from bing_image_downloader import downloader

def download_images(keywords, limit, print_urls=False):
    start_time = time.time()
    downloader.download(keywords, limit=limit, output_dir='datasetBetterScraped', adult_filter_off=True, force_replace=False, timeout=60)
    end_time = time.time()
    
    print("Time taken to download images: ", end_time - start_time, "seconds")

def download_images_from_file(file_path, limit, print_urls=False):
    with open(file_path, 'r') as f:
        keywords = [line.strip() for line in f]

    for keyword in keywords:
        print(f"Downloading images for: {keyword}")
        download_images(keyword, limit, print_urls)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download images from Bing')
    parser.add_argument('-f', '--file', type=str, help='File containing keywords for the images')
    parser.add_argument('-k', '--keywords', type=str, help='Keywords for the images')
    parser.add_argument('-l', '--limit', type=int, help='Limit on number of images to download')
    parser.add_argument('-p', '--print_urls', type=bool, help='Whether to print the URLs of the downloaded images')
    
    args = parser.parse_args()
    
    if args.file:
        download_images_from_file(args.file, args.limit, args.print_urls)
    elif args.keywords:
        download_images(args.keywords, args.limit, args.print_urls)
    else:
        print("Error: Either a file or keywords must be provided")
