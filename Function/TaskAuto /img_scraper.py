import os
import io
import time
import requests
from PIL import Image

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


CHROMEDRIVER = r"DataBase\chromedriver.exe"

service = Service(CHROMEDRIVER)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)


def get_images_from_google(driver, search_query, max_images=10, delay=2):

    url = f"https://www.google.com/search?tbm=isch&q={search_query}"
    driver.get(url)

    image_urls = set()

    while len(image_urls) < max_images:

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        time.sleep(delay)

        thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")

        for thumbnail in thumbnails:

            if len(image_urls) >= max_images:
                break

            try:
                thumbnail.click()
                time.sleep(delay)

                images = driver.find_elements(By.CSS_SELECTOR, "img.n3VNCb")

                for img in images:

                    src = img.get_attribute("src")

                    if src and src.startswith("http"):
                        image_urls.add(src)

                        print(
                            f"Collected {len(image_urls)} / {max_images}"
                        )

                        break

            except Exception:
                continue

    return list(image_urls)


def download_image(folder, url, filename):

    os.makedirs(folder, exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        image = Image.open(io.BytesIO(response.content))

        path = os.path.join(folder, filename)

        image.convert("RGB").save(path, "JPEG")

        print(f"Saved -> {path}")

    except Exception as e:
        print(f"Failed: {e}")


urls = get_images_from_google(
    driver,
    search_query="cats",
    max_images=10
)

for i, url in enumerate(urls):
    download_image(
        "imgs",
        url,
        f"{i}.jpg"
    )

driver.quit()
