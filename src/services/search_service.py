from repositories.item_repository import ItemRepository
from repositories.user_repository import UserRepository
from schemas.search.request_dto import SearchRequestDto
from schemas.search.response_dto import (
    Item,
    ItemsPaginationResponseDto,
    SearchResponseDto,
    User,
    UsersPaginationResponseDto,
)
from utils.parse_image import parse_image_to_base64
from utils.database import get_session


class SearchService:
    def __init__(self):
        self.db = get_session()
        self.user_repo = UserRepository(self.db)
        self.item_repo = ItemRepository(self.db)
        pass

    def search_users_and_items(
        self, payload: SearchRequestDto
    ) -> SearchResponseDto:
        users = self.user_repo.search_users(payload)
        items = self.item_repo.search_items(payload)

        res_users: list[User] = []
        res_items: list[Item] = []

        for user in users:
            user_image = parse_image_to_base64(user.user_image)
            res_users.append(
                User(
                    user_id=user.user_id,
                    user_name=user.user_name,
                    user_wallet_address=user.user_wallet_address,
                    user_image=user_image,
                )
            )

        for item in items:
            item_image = parse_image_to_base64(item.item_image)
            res_items.append(
                Item(
                    item_id=item.item_id,
                    item_name=item.item_name,
                    item_owner_address=item.user.user_wallet_address,
                    item_image=item_image,
                )
            )

        users_total_pages = (
            len(res_users) + payload.limit - 1
        ) // payload.limit
        items_total_pages = (
            len(res_items) + payload.limit - 1
        ) // payload.limit

        return SearchResponseDto(
            users=UsersPaginationResponseDto(
                data=res_users,
                total_items=len(res_users),
                item_per_page=payload.limit,
                total_pages=users_total_pages,
            ),
            items=ItemsPaginationResponseDto(
                data=res_items,
                total_items=len(res_items),
                item_per_page=payload.limit,
                total_pages=items_total_pages,
            ),
        )
