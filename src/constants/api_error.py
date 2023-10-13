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
    SHOPPING_CART_ITEM_CREATION_FAILED = (
        "Failed! Shopping cart item creation failed"
    )
    CANNOT_ADD_OWN_ITEM_TO_CART = "Failed! Cannot add own item to cart"
    ITEM_ALREADY_IN_CART = "Failed! Item already in cart"
    ITEM_NOT_IN_CART = "Failed! Item not in cart"
    SHOPPING_CART_ITEM_DELETION_FAILED = (
        "Failed! Shopping cart item deletion failed"
    )
    USER_NOT_FOUND = "Failed! User not found"
    CATEGORY_CREATE_FAILED = "Failed! Category create failed"


class ValidationMessages:
    PAGE_MUST_BE_POSITIVE = "Page must be positive"
    PAGE_MUST_BE_LESS_THAN_100 = "Page must be less than 100"
    LIMIT_MUST_BE_POSITIVE = "Limit must be positive"
    LIMIT_MUST_BE_LESS_THAN_100 = "Limit must be less than 100"
    ITEM_ID_MUST_BE_INTEGER = "Item ID must be integer"
    ITEM_ID_MUST_BE_POSITIVE = "Item ID must be positive"
