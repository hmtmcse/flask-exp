from dataclasses import dataclass


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0


inventory = InventoryItem(name="Name", unit_price=100)

print(inventory.quantity_on_hand)
