# Scrape a Dynamic Website with Python - https://bit.ly/3Dm2GPs
# BeautifulSoup, Selenium, Pyppeteer, Playwright, and Web Scraping API.
# Hybrid verze muze pouzivat bud Selenium nebo Playwright dle ZZZZ

# pip install selenium
# pip install playwright
# playwright install
#       z VS Code nefunguje
# cmd:> python Mapy-Hybrid.py

# https://playwright.dev/python/docs/intro
# '''
# pip install --upgrade pip
# pip install playwright
# playwright install
# '''
# playwright vs selenium - https://bit.ly/3aA7UuI
# Puppeteer, Selenium, Playwright, Cypress – how to choose? - https://bit.ly/3aCUMVJ

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import os

# selenium
def page_content_selenium():
  # selenium - How to bypass the message-“your connection is not private” on non-secure page using Selenium? - https://is.gd/7NDpuF
  options = webdriver.ChromeOptions()
  options.add_argument('--ignore-ssl-errors=yes')
  options.add_argument('--ignore-certificate-errors')
  driver = webdriver.Chrome('d:/Utils/chromedriver/chromedriver.exe', options=options)
  # Load the HTML page
  driver.get(r'https://bit.ly/3izRnLE')
  # page content
  page_content = driver.page_source
  # Closes the current window
  driver.close()
  return page_content
# playwright
def page_content_playwright():
  # Use async version of Playwright
  async def page_get():
    async with async_playwright() as p:
      # Launch the browser
      browser = await p.chromium.launch()
      # Open a new browser page
      page = await browser.new_page()
      # Create a URI for our test file
      page_path = "file://" + os.getcwd() + "/test.html"
      page_path = r'https://bit.ly/3izRnLE'
      # Open our test file in the opened page
      await page.goto(page_path, timeout=0)
      # print(await page.title())
      # page content
      page_content = await page.content()
      # Close browser
      await browser.close()
      return page_content

  # nefunguje z VS Code pouze z cmd.exe:  python Mapy-Playwright.py
  page_content = asyncio.run(page_get())
  return page_content

# selenium <-> playwright
JeSelenium = False
if JeSelenium:
  page_content = page_content_selenium
else:
  page_content = page_content_playwright

# Parse processed webpage with BeautifulSoup
soup = BeautifulSoup(page_content(), features="lxml")
item = soup.find(itemprop="price").get_text()

# 34,40 Kč => 34.40
item = item.replace(" Kč", "")
item = item.replace(",", ".")
# item
item = float(item)
print("item:", item, '|| type:', type(item))
# Cena
Cena = '{:.2f}'.format(item)
print("Cena:", Cena, '|| type:', type(Cena))
