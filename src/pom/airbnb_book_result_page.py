from src.utils import try_parse_float
from src.resources.airbnb_booking_resources import AirBnBBookingPageResources as Resources
from src.resources.general_resources import Details


class AirBnBBookResultActions:
    def __init__(self, page):
        self.page = page
        self.book_it_card = page.locator(Resources.BOOK_IT_CARD)

    def _get_sub_element_inner_text_by_locator(self, element, loc):
        try:
            sub_element = element.locator(loc)
            text = sub_element.inner_text().strip()
            return text
        except Exception as e:
            print(e)
        return ''

    def _get_title(self):
        return self.page.locator(Resources.BOOKING_PAGE_TITLE_XPATH).inner_text()

    def _get_rating(self):
        text = self.page.locator(Resources.BOOKING_PAGE_RATING_XPATH).nth(0).inner_text().split()[1]
        return try_parse_float(text, text_description='Rating')

    def _get_total_nights(self):
        element = self.page.locator(Resources.TOTAL_NIGHTS_ROW_XPATH).nth(0)
        text = element.inner_text().split(' x ')[1].split()[0]
        return int(text)

    def _get_price_per_night(self):
        text = self._get_sub_element_inner_text_by_locator(self.book_it_card, Resources.PRICE_PER_NIGHT_XPATH)
        return try_parse_float(text, text_description='Price Per Night', start_idx=1)

    def _get_check_in_date_in_card(self):
        element = self.book_it_card.locator(Resources.BOOK_IT_CARD_CHECK_IN_CSS)
        return element.inner_text()

    def _get_check_out_date_in_card(self):
        element = self.book_it_card.locator(Resources.BOOK_IT_CARD_CHECK_OUT_CSS)
        return element.inner_text()

    def _get_guests_in_card(self):
        text = self._get_sub_element_inner_text_by_locator(self.book_it_card, Resources.BOOK_IT_CARD_GUESTS_XPATH)
        return ' '.join(text.split())

    def _get_all_nights_prices(self):
        element = self.book_it_card.locator(Resources.BOOK_IT_CARD_ALL_NIGHTS_XPATH).nth(0)
        return try_parse_float(element.inner_text(), text_description='All nights price', start_idx=1)

    def _get_cleaning_fee(self):
        text = self._get_sub_element_inner_text_by_locator(self.book_it_card, Resources.BOOK_IT_CARD_CLEANING_FEE_XPATH)
        return try_parse_float(text, text_description='Cleaning fee', start_idx=1)

    def _get_airbnb_service_fee(self):
        text = self._get_sub_element_inner_text_by_locator(self.book_it_card, Resources.BOOK_IT_CARD_SERVICE_FEE_XPATH)
        return try_parse_float(text, text_description='Service fee', start_idx=1)

    def _get_taxes(self):
        text = self._get_sub_element_inner_text_by_locator(self.book_it_card, Resources.BOOK_IT_CARD_TAXES_XPATH)
        return try_parse_float(text, text_description='Taxes fee', start_idx=1)

    def _get_total_price(self):
        text = self._get_sub_element_inner_text_by_locator(self.book_it_card, Resources.BOOK_IT_CARD_TOTAL_PRICE_XPATH)
        return try_parse_float(text, text_description='Total price', start_idx=1)

    def get_book_it_card_details(self):
        nights = self._get_total_nights()
        return {
            Details.TITLE: self._get_title(),
            Details.RATING: self._get_rating(),
            Details.CHECK_IN_DATES: self._get_check_in_date_in_card(),
            Details.CHECK_OUT_DATES: self._get_check_out_date_in_card(),
            Details.GUESTS: self._get_guests_in_card(),
            Details.PPN: self._get_price_per_night(),
            Details.TOTAL_NIGHTS: nights,
            Details.TOTAL_NIGHTS_PRICE: self._get_all_nights_prices(),
            Details.CLEANING_FEE: self._get_cleaning_fee(),
            Details.SERVICE_FEE: self._get_airbnb_service_fee(),
            Details.TAXES: self._get_taxes(),
            Details.TOTAL: self._get_total_price(),
        }

    def click_on_reserve(self):
        reserve_button = self.book_it_card.get_by_role('button', name='Reserve')
        reserve_button.click()
