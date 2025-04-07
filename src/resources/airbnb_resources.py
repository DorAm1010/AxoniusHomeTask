import enum

class Details(enum.Enum):
    GUESTS = 'Guests'
    TITLE = 'Title'
    RATING = 'Rating'
    DATES = 'Dates'
    CHECK_IN_DATES = 'Check-In Dates'
    CHECK_OUT_DATES = 'Check-Out Dates'
    PPN = 'Price Per Night'
    TOTAL_NIGHTS = 'Total Nights'
    TOTAL_NIGHTS_PRICE = 'All Nights Price'
    CLEANING_FEE = 'Cleaning Fee'
    SERVICE_FEE = 'Service Fee'
    TAXES = 'Taxes'
    TOTAL = 'Total'


class AirBnBActionsResources:

    AIRBNB_PAGE_DOMAIN = 'https://www.airbnb.com/'
    DESTINATION_BOX_CSS = 'input[placeholder="Search destinations"]'
    DESTINATION_BOX_PLACEHOLDER = "Search destinations"
    DESTINATIONS_LIST_FIRST_OPTION = "option-0"
    CALENDAR_SELECTOR_DATE = 'button[data-state--date-string="{}"]'
    SELECT_GUESTS_DROPDOWN_BUTTON_CSS = 'css=div[data-testid="structured-search-input-field-guests-button"] div'
    LITTLE_SELECT_GUESTS_TEST_ID = 'div[data-testid="little-search-guests"]'
    SELECT_GUESTS_PANEL_TEST_ID = 'div[data-testid="structured-search-input-field-guests-panel"]'
    SELECT_GUESTS_BUTTON_TEXT = 'Add guests'
    INCREASE_GUEST_BUTTON_ID = 'button[data-testid="stepper-{}-increase-button"]'
    SEARCH_BUTTON_CSS = 'button[data-testid="structured-search-input-search-button"]'
    BOOK_IT_CARD = '[data-section-id="BOOK_IT_SIDEBAR"]'

    PRICE_PER_NIGHT_XPATH = 'xpath=.//div[contains(@style, "pricing")]//div[@aria-hidden="true"]//span[1]'
    TOTAL_NIGHTS_ROW_XPATH = 'xpath=.//div[contains(text(),"nights")]'
    BOOK_IT_CARD_CHECK_IN_CSS = '[data-testid="change-dates-checkIn"]'
    BOOK_IT_CARD_CHECK_OUT_CSS = '[data-testid="change-dates-checkOut"]'
    BOOK_IT_CARD_GUESTS_XPATH = 'xpath=.//label[@for="GuestPicker-book_it-trigger"]//span'
    BOOK_IT_CARD_ALL_NIGHTS_XPATH = 'xpath=.//section//div[contains(@style, "pricing-guest-secondary-line")]//div[1]//span[2]'
    BOOK_IT_CARD_CLEANING_FEE_XPATH = 'xpath=.//section//div[contains(@style, "pricing-guest-secondary-line")]//div[2]//span/following-sibling::span'
    BOOK_IT_CARD_SERVICE_FEE_XPATH = 'xpath=.//section//div[contains(@style, "pricing-guest-secondary-line")]//div[3]//span/following-sibling::span'
    BOOK_IT_CARD_TAXES_XPATH = 'xpath=.//section//div[contains(@style, "pricing-guest-secondary-line")]//div[4]//span[2]'
    BOOK_IT_CARD_TOTAL_PRICE_XPATH = 'xpath=.//section//div[contains(@style, "pricing-guest-secondary-line")]//div[1]//span[2]//span[@aria-hidden="false"]'
    BOOKING_PAGE_RATING_XPATH = 'xpath=.//span[contains(text(), "out of 5 stars")]'
    BOOKING_PAGE_TITLE_XPATH = 'xpath=.//div[@data-section-id="TITLE_DEFAULT"]//h1'

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


    MODAL_COUNTRYCODE_DROPDOWN_CSS = 'select[data-testid="login-signup-countrycode"]'
    MODAL_COUNTRYCODE_DROPDOWN_XPATH = 'xpath=.//select[@data-testid="login-signup-countrycode"]'
    ISRAEL_OPTION_CSS = 'option[value="972IL"]'
    PHONE_NUMBER_INPUT_CSS = 'input[data-testid="login-signup-phonenumber"]'


    TEL_AVIV_DESTINATION = 'Tel Aviv'
    FIRST_TEST_DATES = "2025-04-17", "2025-04-19"
    FIRST_TEST_GUESTS_DICT = {
        'adults': 2
    }
    FIRST_TEST_EXPECTED_DATES = 'Apr 17 - 19'
    FIRST_TEST_EXPECTED_GUESTS = '2 guests'

    SECOND_TEST_DATES = "2025-04-20", "2025-04-26"
    SECOND_TEST_GUESTS_DICT = {
        'adults': 2,
        'children': 1
    }
    SECOND_TEST_EXPECTED_DATES = 'Apr 17 - 19'
    SECOND_TEST_EXPECTED_GUESTS = '3 guests'
    SECOND_TEST_PHONE = '503454837'

    EXCLUDE = { Details.GUESTS, Details.DATES, Details.CHECK_IN_DATES, Details.CHECK_OUT_DATES, Details.TITLE }
    NUMBER_COMPARISONS = [d for d in set(Details).difference(EXCLUDE)]

    EXPECTED_IN_RESULT_FORMAT = 'Expected {} to be in {}'
