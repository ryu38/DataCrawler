from icrawler import crawler
from icrawler.builtin import BingImageCrawler, GoogleImageCrawler

keyword = 'cat sleeping'

base_dir = './cat/'

save_filename = keyword.replace(' ', '_')
base_dir += save_filename

img_crler = BingImageCrawler(storage={'root_dir': base_dir})
img_crler.crawl(keyword=keyword, max_num=1000)