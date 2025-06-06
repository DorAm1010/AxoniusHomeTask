class AirBnBBookingPageResources:
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
