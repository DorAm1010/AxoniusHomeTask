from src.resources.airbnb_resources import AirBnBActionsResources as Resources
from typing import Dict


class AirBnBMainPageActions:
    def __init__(self, page):
        self.page = page
        self.destination_input_box = page.get_by_placeholder(Resources.DESTINATION_BOX_PLACEHOLDER)
        # self.select_guests_element = page
        # print("\nGot Here\n")

    def input_destination(self, destination: str):
        self.destination_input_box.fill(destination)

    def select_destination_first_option(self, destination: str):
        self.input_destination(destination)
        self.page.get_by_test_id(Resources.DESTINATIONS_LIST_FIRST_OPTION).click()

    def select_dates_in_calendar(self, start_date: str, end_date: str):
        self.page.locator(Resources.CALENDAR_SELECTOR_DATE.format(start_date)).click()
        self.page.locator(Resources.CALENDAR_SELECTOR_DATE.format(end_date)).click()

    def open_select_guests_options(self):
        self.page.locator(Resources.SELECT_GUESTS_DROPDOWN_BUTTON_CSS).nth(0).click()

    def open_select_guests_options_from_little_button(self):
        self.page.locator(Resources.LITTLE_SELECT_GUESTS_TEST_ID).click()

    def _assert_guests_panel_opened(self):
        select_guests_panel = self.page.locator(Resources.SELECT_GUESTS_PANEL_TEST_ID)
        if not select_guests_panel.is_visible():
            self.open_select_guests_options()
            select_guests_panel = self.page.locator(Resources.SELECT_GUESTS_PANEL_TEST_ID)
        if not select_guests_panel.is_visible():
            self.open_select_guests_options_from_little_button()
        assert select_guests_panel.is_visible(), 'Could not open guests panel'

    def select_guests(self, guests_dict: Dict[str, int]):
        self._assert_guests_panel_opened()
        # button[data-testid="stepper-adults-increase-button"]
        for guests in guests_dict:
            guests_increase_button = self.page.locator(Resources.INCREASE_GUEST_BUTTON_ID.format(guests.lower()))
            for _ in range(guests_dict[guests]):
                guests_increase_button.click()

    def click_search(self):
        # self.page.locator(Resources.SEARCH_BUTTON_CSS).click()
        self.page.get_by_role('button', name='Search').click()

