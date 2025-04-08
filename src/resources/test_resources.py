class TestResources:
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

    EXPECTED_IN_RESULT_FORMAT = 'Expected {} to be in {}'
