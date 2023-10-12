from pydantic import BaseModel, Field

from schemas.pagination.response_dto import BasePaginationResponseDto


class GetTransactionsSubDto(BaseModel):
    transaction_smart_contract_id: int = Field(
        ...,
        title="transaction_smart_contract_id",
        example="1",
        description="The transaction_smart_contract_id of the transaction",
    )

    transaction_user_id: int = Field(
        ...,
        title="transaction_user_id",
        example="1",
        description="The transaction_user_id of the transaction",
    )


class GetTransactionsDto(BasePaginationResponseDto):
    data: list[GetTransactionsSubDto] = Field(
        ...,
        title="transactions",
        description="The transactions of the transaction",
    )
