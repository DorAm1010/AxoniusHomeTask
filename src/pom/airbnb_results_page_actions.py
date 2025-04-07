import re
import time


class AirBnBResultsActions:
    def __init__(self, page):
        page.locator('div[data-testid="card-container"]').nth(0).wait_for(timeout=10000)
        self.page = page

    def get_little_search_results(self):
        element_text =  self.page.locator('div[data-testid="little-search-location""]').inner_text()
        return re.sub(r'\s+', ' ', element_text).strip()

    def get_little_search_destination_results(self):
        return self.page.locator('[data-testid="little-search"]').inner_text()

    def get_little_search_dates_results(self):
        element_text =  self.page.locator('[data-testid="little-search-anytime"]').inner_text()
        return re.sub(r'\s+', ' ', element_text).strip()

    def get_little_search_guests_results(self):
        element_text =  self.page.locator('[data-testid="little-search"]').inner_text()
        return re.sub(r'\s+', ' ', element_text).strip()

    def get_highest_rated_result(self):
        max_rating = 0.0
        highest_rated = None
        time.sleep(5)
        results = self.page.locator('div[data-testid="card-container"]:not(div[aria-hidden="false"] div[data-testid="card-container"])')
        count = results.count()
        # TODO - remove list comprehension
        for i in range(count):
            result = results.nth(i)
            try:
                rating = result.locator('xpath=.//div[@data-testid="price-availability-row"]/following-sibling::div//span[@aria-hidden="true"]').text_content()
                rating = float(rating.split()[0])
            except Exception as e:
                continue

            if rating > max_rating or highest_rated is None:
                highest_rated = result
                max_rating = rating
        return highest_rated, max_rating

    def get_cheapest_result(self):
        results = self.page.locator('div[data-testid="card-container"]:not(div[aria-hidden="false"] div[data-testid="card-container"])')
        cheapest = results.nth(0)
        result_price_str = cheapest.locator('[data-testid="price-availability-row"] button').inner_text().split()[0][1:]
        min_price = int(result_price_str.replace(',', ''))
        count = results.count()
        for i in range(1, count):
            result = results.nth(i)
            result_price_str = result.locator('[data-testid="price-availability-row"] button').inner_text().split()[0][1:]
            price = int(result_price_str.replace(',', ''))
            if price < min_price:
                cheapest = result
                min_price = price
        return cheapest, min_price
