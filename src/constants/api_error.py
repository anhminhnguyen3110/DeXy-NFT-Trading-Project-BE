class ErrorMessages:
    USER_ALREADY_EXISTS = "Failed! User with this wallet address already exists"
    USER_IS_NOT_EXISTING = (
        "Failed! User with this wallet address does not exist"
    )
    INVALID_SIGNATURE = "Failed! Invalid signature"
    CATEGORY_IS_NOT_EXISTING = "Failed! Category with this ID does not exist"
    ITEM_CREATION_FAILED = "Failed! Item creation failed"
    ITEM_IS_NOT_EXISTING = "Failed! Item with this ID does not exist"
    CATEGORY_GET_FAILED = "Failed! Category get failed"


class ValidationMessages:
    PAGE_MUST_BE_POSITIVE = "Page must be positive"
    PAGE_MUST_BE_LESS_THAN_100 = "Page must be less than 100"
    LIMIT_MUST_BE_POSITIVE = "Limit must be positive"
    LIMIT_MUST_BE_LESS_THAN_100 = "Limit must be less than 100"
