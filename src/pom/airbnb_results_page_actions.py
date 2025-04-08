import re

from src.resources.airbnb_results_resources import AirBnBResultsResources as Resources


class AirBnBResultsActions:
    def __init__(self, page):
        page.locator(Resources.CARD_CONTAINER_CSS).nth(0).wait_for(timeout=10000)
        self.page = page

    def get_little_search_results(self):
        element_text =  self.page.locator(Resources.LITTLE_SEARCH_RESULT_CSS).inner_text()
        return re.sub(r'\s+', ' ', element_text).strip()

    def get_little_search_destination_results(self):
        return self.page.locator(Resources.LITTLE_SEARCH_DESTINATION_RESULTS_CSS).inner_text()

    def get_little_search_dates_results(self):
        element_text =  self.page.locator(Resources.LITTLE_SEARCH_DATES_RESULTS).inner_text()
        return re.sub(r'\s+', ' ', element_text).strip()

    def get_little_search_guests_results(self):
        element_text =  self.page.locator(Resources.LITTLE_SEARCH_GUESTS_RESULT_CSS).inner_text()
        return re.sub(r'\s+', ' ', element_text).strip()

    def get_highest_rated_result(self):
        max_rating = 0.0
        highest_rated = None
        # wait until there are at least 3 results - AirBnB loads one result first sometimes making
        # the following line find only one result
        self.page.wait_for_function(
            """(selector) => document.querySelectorAll(selector).length >= 3""",
            arg=Resources.ALL_RESULTS_CSS,
            timeout=10000
        )

        results = self.page.locator(Resources.ALL_RESULTS_CSS)
        count = results.count()
        for i in range(count):
            result = results.nth(i)
            try:
                rating = result.locator(Resources.RESULT_RATING_XPATH).text_content()
                rating = float(rating.split()[0])
            except Exception as e:
                continue

            if rating > max_rating or highest_rated is None:
                highest_rated = result
                max_rating = rating
        return highest_rated, max_rating

    def get_cheapest_result(self):
        results = self.page.locator(Resources.ALL_RESULTS_CSS)
        cheapest = results.nth(0)
        result_price_str = cheapest.locator(Resources.RESULT_PRICE_CSS).inner_text().split()[0][1:]
        min_price = int(result_price_str.replace(',', ''))
        count = results.count()
        for i in range(1, count):
            result = results.nth(i)
            result_price_str = result.locator(Resources.RESULT_PRICE_CSS).inner_text().split()[0][1:]
            price = int(result_price_str.replace(',', ''))
            if price < min_price:
                cheapest = result
                min_price = price
        return cheapest, min_price
