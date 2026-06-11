# import the required libraries
import asyncio
import csv

import nodriver as uc


async def scraper():

    # start a new Chrome instance
    driver = await uc.start(headless=False)

    # visit the target website
    page = await driver.get("https://www.scrapingcourse.com/ecommerce/")

    # extract all the product containers
    products = await page.select_all(".product")

    # wait for the content to load
    page.sleep(15)

    # product array to collect data
    product_data = []

    # loop through each container to extract names and prices
    for product in products:
        product_name = await product.query_selector(".woocommerce-loop-product__title")

        product_price = await product.query_selector(".price")

        # get all product texts into a dictionary
        data = {"Name": product_name.text_all, "Price": product_price.text_all}

        # append each product data to the product data array
        product_data.append(data)

    # save the data to a CSV file
    keys = product_data[0].keys()
    with open("product_data.csv", "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(product_data)
        print("CSV created successfully")

    # close the page
    await page.close()


# run the scraper function with asyncio
if __name__ == "__main__":
    asyncio.run(scraper())
