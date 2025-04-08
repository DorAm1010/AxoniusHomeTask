class AirBnBResultsResources:
    LITTLE_SEARCH_RESULT_CSS = 'div[data-testid="little-search-location""]'
    CARD_CONTAINER_CSS = 'div[data-testid="card-container"]'
    LITTLE_SEARCH_DESTINATION_RESULTS_CSS = '[data-testid="little-search"]'
    LITTLE_SEARCH_DATES_RESULTS = '[data-testid="little-search-anytime"]'
    LITTLE_SEARCH_GUESTS_RESULT_CSS = '[data-testid="little-search"]'
    ALL_RESULTS_CSS = 'div[data-testid="card-container"]:not(div[aria-hidden="false"] div[data-testid="card-container"])'
    RESULT_RATING_XPATH = 'xpath=.//div[@data-testid="price-availability-row"]/following-sibling::div//span[@aria-hidden="true"]'
    RESULT_PRICE_CSS = '[data-testid="price-availability-row"] button'


