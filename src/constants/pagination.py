from enum import Enum


class SortBy(str, Enum):
    PRICE_LOW_TO_HIGH = "PRICE_LOW_TO_HIGH"
    PRICE_HIGH_TO_LOW = "PRICE_HIGH_TO_LOW"
    NEWEST = "NEWEST"
    OLDEST = "OLDEST"
