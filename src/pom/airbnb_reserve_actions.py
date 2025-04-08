import time
from src.resources.airbnb_reservation_resources import AirBnBReservationActionsResources as Resources, ModalResources
from src.resources.general_resources import Details
from src.utils import try_parse_float


class ReservationModalActions:
    def __init__(self, page):
        self.page = page

    def select_israel_prefix(self):
        self.page.select_option('select[id="country"]', value='972IL')

    def input_israel_phone(self, phone: str):
        self.select_israel_prefix()
        input_field = self.page.locator(ModalResources.PHONE_NUMBER_INPUT_CSS)
        input_field.fill(phone)
        time.sleep(10)

class AirBnBReserveActions:
    def __init__(self, page):
        page.locator(Resources.RESERVATION_DETAILS_CSS).nth(0).wait_for(timeout=10000)
        self.page = page
        self.reservation_details = page.locator(Resources.RESERVATION_DETAILS_CSS)

    def _get_sub_element_inner_text_by_locator(self, element, loc):
        try:
            sub_element = element.locator(loc)
            text = sub_element.inner_text().strip()
            return text
        except Exception as e:
            print(e)
        return ''

    def _get_reservation_title(self):
        time.sleep(2)
        title = self.page.locator(Resources.RESERVATION_TITLE_XPATH).nth(0)
        return title.inner_text()

    def _get_reservation_rating(self):
        rating = self.page.locator(Resources.RESERVATION_RATING_XPATH).nth(0)
        return float(rating.inner_text().split()[1])

    def _get_reservation_dates(self):
        dates = self.reservation_details.locator(Resources.RESERVATION_DATES_XPATH).nth(0)
        return dates.inner_text()

    def _get_reservation_guests(self):
        guests = self.reservation_details.locator(Resources.RESERVATION_GUESTS_XPATH).nth(1)
        return guests.inner_text()

    def _get_calculated_price(self):
        price = self.page.locator(Resources.RESERVATION_CALCULATED_PRICE_XPATH).nth(0)
        return price.inner_text().split('\n')

    def _get_cleaning_fee(self):
        fee = self.reservation_details.locator(Resources.RESERVATION_CLEANING_FEE_XPATH).inner_text()
        return try_parse_float(fee, text_description='Cleaning fee', start_idx=1)

    def _get_airbnb_service_fee(self):
        fee = self.reservation_details.locator(Resources.RESERVATION_SERVICE_FEE_XPATH).inner_text()
        return try_parse_float(fee, text_description='Service fee', start_idx=1)

    def _get_taxes(self):
        taxes = self._get_sub_element_inner_text_by_locator(self.reservation_details, Resources.RESERVATION_TAXES_XPATH)
        return try_parse_float(taxes, text_description='Taxes', start_idx=1)

    def _get_total_price(self):
        text = self._get_sub_element_inner_text_by_locator(
            self.reservation_details, Resources.RESERVATION_TOTAL_PRICES_XPATH)
        return try_parse_float(text, text_description='Total price', start_idx=1)

    def get_reservation_details(self):
        calculation, all_nights_price = self._get_calculated_price()
        ppn, nights = calculation.split(' x ')
        ppn = try_parse_float(ppn, text_description=Details.PPN.value, start_idx=1)
        nights = int(try_parse_float(nights.split()[0], text_description=Details.TOTAL_NIGHTS.value))
        all_nights_price = try_parse_float(all_nights_price,
                                           text_description=Details.TOTAL_NIGHTS_PRICE.value, start_idx=1)
        result = {
            Details.TITLE: self._get_reservation_title(),
            Details.RATING: self._get_reservation_rating(),
            Details.DATES: self._get_reservation_dates(),
            Details.GUESTS: self._get_reservation_guests(),
            Details.PPN: ppn,
            Details.TOTAL_NIGHTS: nights,
            Details.TOTAL_NIGHTS_PRICE: all_nights_price,
            Details.CLEANING_FEE: self._get_cleaning_fee(),
            Details.SERVICE_FEE: self._get_airbnb_service_fee(),
            Details.TAXES: self._get_taxes(),
            Details.TOTAL: self._get_total_price(),
        }
        return result

    def click_continue(self):
        self.page.get_by_role('button', name='Continue').click()
