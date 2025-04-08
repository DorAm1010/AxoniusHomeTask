class ModalResources:
    ISRAEL_OPTION_CSS = 'option[value="972IL"]'
    PHONE_NUMBER_INPUT_CSS = 'input[data-testid="login-signup-phonenumber"]'


class AirBnBReservationActionsResources:

    RESERVATION_DETAILS_CSS = '[data-section-id="PRODUCT_DETAILS"]'
    RESERVATION_TITLE_XPATH = 'xpath=.//div[@data-testid="checkout-product-details-listing-card"]//div[2]//div | .//div[@id="LISTING_CARD-title"]'
    RESERVATION_RATING_XPATH = 'xpath=.//span[contains(text(), "out of 5")]'
    RESERVATION_DATES_XPATH = 'xpath=.//div[text()="Trip details"]/following-sibling::div//div'
    RESERVATION_GUESTS_XPATH = 'xpath=.//div[text()="Trip details"]/following-sibling::div//div'
    RESERVATION_CALCULATED_PRICE_XPATH = 'xpath=.//div[contains(text(),"nights")]/parent::div/parent::div'
    RESERVATION_CLEANING_FEE_XPATH = 'xpath=.//div[text()="Cleaning fee"]/parent::div/following-sibling::div//span'
    RESERVATION_SERVICE_FEE_XPATH = 'xpath=.//div[text()="Airbnb service fee"]/parent::div/following-sibling::div//span'
    RESERVATION_TAXES_XPATH = 'xpath=.//div[text()="Taxes"]/parent::div/following-sibling::div//span'
    RESERVATION_TOTAL_PRICES_XPATH = 'xpath=.//div[contains(text(), "Total")]/parent::div/following-sibling::div//span'
