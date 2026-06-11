# import the required libraries
import asyncio

import nodriver as uc


async def scraper(page, product_data):
    # extract all the product containers
    products = await page.select_all(".product-item")

    # loop through each container to extract names and prices
    for product in products:
        product_name = await product.query_selector(".product-name")
        product_price = await product.query_selector(".product-price")

        # get all product texts into a dictionary
        data = {"Name": product_name.text_all, "Price": product_price.text_all}

        # append each product data to the product data array
        product_data.append(data)

    # print the output data
    print(product_data)


async def scroller():

    # start a new Chrome instance
    driver = await uc.start()

    # visit the target website
    page = await driver.get("https://www.scrapingcourse.com/infinite-scrolling")

    # product array to collect data
    product_data = []

    # execute initial scrolling
    await page.scroll_down(1500)

    # get the value of the initial page height
    last_height = await page.evaluate("document.body.scrollHeight")

    while True:
        # scroll down the page
        await page.scroll_down(1500)

        # wait for content to load after scrolling
        await page.sleep(5)

        # get the value of the new page height
        new_height = await page.evaluate("document.body.scrollHeight")

        # if the height hasn't changed, it means we are at the bottom of the page
        if new_height == last_height:
            break

        # update the last height for the next iteration
        last_height = new_height

    # scrape the entire page after scrolling is complete
    await scraper(page, product_data)

    # close the page
    await page.close()


# run the scraper function with asyncio
if __name__ == "__main__":
    asyncio.run(scroller())
