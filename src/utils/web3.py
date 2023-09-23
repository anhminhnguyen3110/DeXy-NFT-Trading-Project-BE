from web3 import Web3
from eth_account.messages import encode_defunct
from config.core import Setting
from eth_utils.curried import to_bytes


class Web3Service:
    web3 = Web3(Web3.HTTPProvider(Setting.ETH_RPC))

    @staticmethod
    def recover(message: str, signature: str) -> str:
        try:
            bytes_message = encode_defunct(to_bytes(text=message))
            return Web3Service.web3.eth.account.recover_message(
                bytes_message, signature=signature
            )
        except Exception as e:
            return None

    @staticmethod
    def to_checksum_address(address: str) -> str:
        return Web3Service.web3.to_checksum_address(address)

    @staticmethod
    def is_address(address: str) -> bool:
        return Web3Service.web3.is_address(address)
