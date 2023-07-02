from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_videos(driver):
  YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'
  driver.get(YOUTUBE_TRENDING_URL)
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos


def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_src = thumbnail_tag.get_attribute('src')
  channel_name = video.find_element(By.CLASS_NAME, 'ytd-channel-name').text
  description = video.find_element(By.ID, 'description-text').text
  dict = {
    'title': title,
    'url': url,
    'thumbnail': thumbnail_src,
    'channel name': channel_name,
    'description': description
  }
  return dict


if __name__ == '__main__':
  print('creating the driver')
  driver = get_driver()
  print('get the videos')
  videos = get_videos(driver)
  print(f'Found {len(videos)} videos')
  print('parsing the videos:')
  videos_data = [parse_video(videos[i]) for i in range(10)]
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending.csv',index=None)
