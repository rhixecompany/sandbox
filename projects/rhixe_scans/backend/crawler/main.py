# import the required libraries

import csv

import nodriver as uc


async def scraper(url):

    # start a new Chrome instance
    driver = await uc.start(headless=False)

    # visit the target website
    page = await driver.get(url)

    # extract all the product containers
    products = await page.select_all(".product")

    # wait for the content to load
    page.sleep(15)  # type: ignore  # noqa: PGH003

    # product array to collect data
    product_data = []

    # loop through each container to extract names and prices
    for product in products:
        product_name = await product.query_selector(".woocommerce-loop-product__title")

        product_price = await product.query_selector(".price")

        # get all product texts into a dictionary
        data = {"Name": product_name.text_all, "Price": product_price.text_all}  # type: ignore  # noqa: PGH003

        # append each product data to the product data array
        product_data.append(data)

    # save the data to a CSV file
    keys = product_data[0].keys()
    with open(  # noqa: ASYNC230, PTH123
        "product_data.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(product_data)
        print("CSV created successfully")  # noqa: T201

    # close the page
    await page.close()
