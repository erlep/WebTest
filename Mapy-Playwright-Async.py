# Scrape a Dynamic Website with Python - https://bit.ly/3Dm2GPs
# BeautifulSoup, Selenium, Pyppeteer, Playwright, and Web Scraping API.

# Record scripts:> playwright codegen wikipedia.org

# https://playwright.dev/python/docs/intro
# pip install playwright
# playwright install
#       z VS Code nefunguje
# cmd:> python Mapy-Playwright-Async.py

import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import os

# Use async version of Playwright
async def main():
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
    print(await page.title())
    # page content
    page_content = await page.content()

    # Close browser
    await browser.close()

    # Process extracted content with BeautifulSoup
    soup = BeautifulSoup(page_content, features="lxml")
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

# nefunguje z VS Code pouze z cmd.exe:  python Mapy-Playwright.py
asyncio.run(main())
