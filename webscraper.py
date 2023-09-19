import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Replace with the URL of the webpage containing the video
url = "https://www.eporner.com/video-d6rsf9v8U8d/hot-grand-daughter/"

# Send an HTTP GET request to the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find video elements based on HTML tags and attributes
    video_tags = soup.find_all('video')  # Example: <video src="video_url.mp4"></video>

    if video_tags:
        # Extract the video source URL from the first video tag
        video_url = video_tags[0].get('src')

        if video_url:
            print(f"Video URL found using BeautifulSoup: {video_url}")
        else:
            # If 'src' attribute is not found, fall back to using Selenium
            print("No 'src' attribute found in video element. Trying Selenium...")

            # Create a WebDriver instance (you'll need to download the appropriate WebDriver for your browser)
            driver = webdriver.Chrome('C:\\Users\\jezow\\Downloads\\chromedriver-win64')

            try:
                # Open the webpage
                driver.get(url)

                # Wait for the video to load (you may need to adjust the wait time)
                driver.implicitly_wait(10)

                # Find the video element
                video_element = driver.find_element_by_tag_name('video')

                # Get the video source URL
                video_url = video_element.get_attribute('src')

                print(f"Video URL found using Selenium: {video_url}")

            except Exception as e:
                print(f"Error with Selenium: {e}")

            finally:
                # Close the browser
                driver.quit()

    else:
        print('No video element found on the webpage using BeautifulSoup.')
else:
    print('Failed to fetch webpage using requests.')

# Download the video (you can use the requests library as in the previous example)
if video_url:
    video_response = requests.get(video_url)
    if video_response.status_code == 200:
        with open('downloaded_video.mp4', 'wb') as file:
            file.write(video_response.content)
        print('Video downloaded successfully.')
    else:
        print('Failed to download video.')
