from config.core import Setting
from services.event_service import EventService
from utils.web3 import Web3Service
from abi.contract_abi import contract
import asyncio


class ContractService:
    def __init__(self):
        self.contract = Web3Service.web3.eth.contract(
            address=Setting.SMART_CONTRACT, abi=contract
        )
        self.eventService = EventService()

    async def activate(self):
        event_filter = self.contract.events.TransactionAccepted.create_filter(
            fromBlock="latest"
        )

        while True:
            event_logs = event_filter.get_new_entries()
            if event_logs:
                for event in event_logs:
                    await self.eventService.handler(event["args"])

            await asyncio.sleep(1)


contract = ContractService()


async def start_contract_service():
    await contract.activate()


loop = asyncio.get_event_loop()
loop.create_task(start_contract_service())
