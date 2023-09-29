from enum import Enum


class SortBy(str, Enum):
    PRICE_LOW_TO_HIGH = "price_low_to_high"
    PRICE_HIGH_TO_LOW = "price_high_to_low"
    NEWEST = "newest"
    OLDEST = "oldest"
