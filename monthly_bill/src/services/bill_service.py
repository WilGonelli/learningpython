

from schemas.schemas import Bill, BillBase, BillInstances, Mounth

class BillService:

    def __init__(self, db):
        self.db = db


    async def create_bill(self, bill: BillBase):
        pass