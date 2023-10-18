from repositories.item_repository import ItemRepository
from repositories.user_repository import UserRepository
from schemas.search.request_dto import SearchRequestDto
from schemas.search.response_dto import (
    ItemSearchDto,
    ItemsPaginationResponseDto,
    SearchResponseDto,
    UserSearchDto,
    UsersPaginationResponseDto,
)
from utils.parse_image import parse_image_to_base64


class SearchService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.item_repo = ItemRepository()
        pass

    def search_users_and_items(
        self, payload: SearchRequestDto, db
    ) -> SearchResponseDto:
        [users, users_count] = self.user_repo.search_users(payload, db)
        [items, items_count] = self.item_repo.search_items(payload, db)

        res_users = [
            UserSearchDto(
                user_id=user.user_id,
                user_name=user.user_name,
                user_wallet_address=user.user_wallet_address,
                user_image=parse_image_to_base64(user.user_image),
            )
            for user in users
        ]

        res_items = [
            ItemSearchDto(
                item_id=item.item_id,
                item_name=item.item_name,
                item_owner_address=item.user.user_wallet_address,
                item_image=parse_image_to_base64(item.item_image),
            )
            for item in items
        ]

        return SearchResponseDto(
            users=UsersPaginationResponseDto(
                data=res_users,
                total_items=users_count,
                items_per_page=payload.limit,
            ),
            items=ItemsPaginationResponseDto(
                data=res_items,
                total_items=items_count,
                items_per_page=payload.limit,
            ),
        )
