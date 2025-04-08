import pytest
from playwright.sync_api import sync_playwright
from src.pom.airbnb_actions import AirBnBMainPageActions
from src.pom.airbnb_results_page_actions import AirBnBResultsActions
from src.pom.airbnb_book_result_page import AirBnBBookResultActions
from src.pom.airbnb_reserve_actions import AirBnBReserveActions, ReservationModalActions
from src.resources.airbnb_resources import AirBnBActionsResources as Resources
from src.resources.general_resources import Details, GeneralResources
from src.resources.test_resources import TestResources
from datetime import datetime


@pytest.fixture(scope="function")
def navigate_to_airbnb():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(Resources.AIRBNB_PAGE_DOMAIN)
        yield page
        print(page.url)
        browser.close()


def test_apartment_for_2_adults(navigate_to_airbnb):
    # fixture yielded value
    page = navigate_to_airbnb

    # test meta
    destination = TestResources.TEL_AVIV_DESTINATION
    start_date, end_date = TestResources.FIRST_TEST_DATES
    guests_dict = TestResources.FIRST_TEST_GUESTS_DICT
    expected_guests = TestResources.FIRST_TEST_EXPECTED_GUESTS
    expected_dates = TestResources.FIRST_TEST_EXPECTED_DATES

    # test flow
    # Search destination+dates+guests
    airbnb_actions = AirBnBMainPageActions(page)
    airbnb_actions.select_destination_first_option(destination)
    airbnb_actions.select_dates_in_calendar(start_date, end_date)
    airbnb_actions.select_guests(guests_dict)
    airbnb_actions.click_search()

    # Validate results
    airbnb_result_actions = AirBnBResultsActions(page)
    destination_search_result = airbnb_result_actions.get_little_search_destination_results()
    dates_search_result = airbnb_result_actions.get_little_search_dates_results()
    guests_search_result = airbnb_result_actions.get_little_search_guests_results()
    assert destination in destination_search_result, TestResources.EXPECTED_IN_RESULT_FORMAT.format(destination, destination_search_result)
    assert 'Apr 17' in dates_search_result and '19' == dates_search_result[-2:], TestResources.EXPECTED_IN_RESULT_FORMAT.format(expected_dates, dates_search_result)
    assert expected_guests in guests_search_result, TestResources.EXPECTED_IN_RESULT_FORMAT.format(expected_guests, guests_search_result)

    highest_rated, rating = airbnb_result_actions.get_highest_rated_result()
    cheapest, min_price = airbnb_result_actions.get_cheapest_result()
    print(f'\nHighest rated result: {rating}')
    print(f'Cheapest result: {min_price}')


def test_apartment_for_2_adults_and_child(navigate_to_airbnb):
    # fixture yielded value
    page = navigate_to_airbnb
    context = page.context
    # test meta
    destination = TestResources.TEL_AVIV_DESTINATION
    start_date, end_date = TestResources.SECOND_TEST_DATES
    guests_dict = TestResources.SECOND_TEST_GUESTS_DICT
    expected_guests = TestResources.SECOND_TEST_EXPECTED_GUESTS
    expected_dates = TestResources.SECOND_TEST_EXPECTED_DATES
    phone = TestResources.SECOND_TEST_PHONE

    expected_guests_in_reservation = '2 adults, 1 child'

    # test flow
    # Search destination+dates+guests
    airbnb_actions = AirBnBMainPageActions(page)
    airbnb_actions.select_destination_first_option(destination)
    airbnb_actions.select_dates_in_calendar(start_date, end_date)
    airbnb_actions.select_guests(guests_dict)
    airbnb_actions.click_search()

    airbnb_result_actions = AirBnBResultsActions(page)
    destination_search_result = airbnb_result_actions.get_little_search_destination_results()
    dates_search_result = airbnb_result_actions.get_little_search_dates_results()
    guests_search_result = airbnb_result_actions.get_little_search_guests_results()
    assert destination in destination_search_result, TestResources.EXPECTED_IN_RESULT_FORMAT.format(destination, destination_search_result)
    assert 'Apr 20' in dates_search_result and '26' == dates_search_result[-2:], TestResources.EXPECTED_IN_RESULT_FORMAT.format(expected_dates, dates_search_result)
    assert expected_guests in guests_search_result, TestResources.EXPECTED_IN_RESULT_FORMAT.format(expected_guests, guests_search_result)

    highest_rated, rating = airbnb_result_actions.get_highest_rated_result()
    assert highest_rated is not None, 'Could not get highest rated result'
    with context.expect_page() as new_page_info:
        highest_rated.click()
    new_tab = new_page_info.value
    new_tab.wait_for_load_state()

    close_translation_button = new_tab.locator('[aria-label="Close"]')

    close_translation_button.click()

    airbnb_booking_actions = AirBnBBookResultActions(new_tab)
    book_it_card_details = airbnb_booking_actions.get_book_it_card_details()
    print(book_it_card_details)
    airbnb_booking_actions.click_on_reserve()

    reserve_actions = AirBnBReserveActions(new_tab)
    reserve_details = reserve_actions.get_reservation_details()
    print(reserve_details)
    # assert guests
    assert reserve_details[Details.GUESTS] == expected_guests_in_reservation, \
        f'Expected guests in reservation to be "{expected_guests_in_reservation}" but got {reserve_details[Details.GUESTS]}'
    assert book_it_card_details[Details.GUESTS] == '3 guests', \
        f'Expected guests in reservation to be "3 guests" but got {reserve_details[Details.GUESTS]}'
    # assert title
    assert reserve_details[Details.TITLE] == book_it_card_details[Details.TITLE], \
        (f'Expected Titles in reservation and booking pages to be equal but got "{reserve_details[Details.TITLE]}"'
         f' in reseervation page and "{book_it_card_details[Details.TITLE]} in booking page')
    # assert dates
    booking_start_dates = book_it_card_details[Details.CHECK_IN_DATES]
    booking_end_dates = book_it_card_details[Details.CHECK_OUT_DATES]
    start_date_object = datetime.strptime(booking_start_dates, '%m/%d/%Y')
    end_date_object = datetime.strptime(booking_end_dates, '%m/%d/%Y')
    formatted_range = (f"{start_date_object.strftime('%b')} {start_date_object.day}\u2009–\u2009{end_date_object.day}"
                       f", {end_date_object.year}")
    assert formatted_range == reserve_details[Details.DATES], \
        (f'Dates in reservation page ({reserve_details[Details.DATES]}) and in booking (start: {booking_start_dates},'
         f' end: {booking_end_dates}) weren`t the same')

    for name in GeneralResources.NUMBER_COMPARISONS:
        assert round(reserve_details[name]) == round(book_it_card_details[name]), \
            (f'Expected {name.value} in reservation details ({reserve_details[name]}) to equal'
             f'the one in booking page details ({book_it_card_details[name]})')
    reserve_actions.click_continue()

    modal_actions = ReservationModalActions(new_tab)
    modal_actions.input_israel_phone(phone)

