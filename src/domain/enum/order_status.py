from enum import StrEnum


class OrderStatus(StrEnum):
    PENDING_PAYMENT = 'pending_payment'
    PAID = 'paid'
    CANCELLED = 'cancelled'
    COMPLETED = 'completed'
