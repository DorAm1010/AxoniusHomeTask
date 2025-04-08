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


class GeneralResources:
    EXCLUDE = { Details.GUESTS, Details.DATES, Details.CHECK_IN_DATES, Details.CHECK_OUT_DATES, Details.TITLE }
    NUMBER_COMPARISONS = [d for d in set(Details).difference(EXCLUDE)]
