from typing import Any, Dict, List, Optional

from fastapi import Depends

from src.platform.logging.loguru_io import Logger
from src.platform.service.unit_of_work import AbstractUnitOfWork, get_unit_of_work


class ListOrdersUseCase:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    @classmethod
    def depends(cls, uow: AbstractUnitOfWork = Depends(get_unit_of_work)):
        return cls(uow=uow)

    @Logger.io
    async def list_buyer_orders(
        self, buyer_id: int, status: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        async with self.uow:
            orders = await self.uow.orders.get_buyer_orders_with_details(buyer_id)
            if status:
                orders = [order for order in orders if order['status'] == status]

            return orders

    @Logger.io
    async def list_seller_orders(
        self, seller_id: int, status: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        async with self.uow:
            orders = await self.uow.orders.get_seller_orders_with_details(seller_id)

            if status:
                orders = [order for order in orders if order['status'] == status]

            return orders
