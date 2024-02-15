# IntelliArtGen

Repo housing a ML project to generate art using GAN networks

Dataset link : [Kaggle Link](https://www.kaggle.com/datasets/thedownhill/art-images-drawings-painting-sculpture-engraving/data)

## Work needed to be done

1. Data set Preparation
   - ~~Data scraping~~
   - Homogenization
2. Code refactoring
   - modify code to process the scraped data.

## Updates

- Scraper folder has means to scrape the images using bing image downloader

```bash
pip install bing-image-downloader
```

- Key words can be supplied in a file called `keywordList.txt`
- Commands to run the scraper

```python
python Image_Scraper.py --limit 100 -k "Keyword"
```

```python
python better_Scraper.py --limit 100 -f path/to/file

```
