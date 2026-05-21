from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date

app = FastAPI()

expense = []

class Expense(BaseModel):
    id: int | None = None
    amount: float 
    category: str
    description: str | None = None
    expense_date: date = Field(default_factory=date.today)


@app.get('/')
def read_root():
    return {"message" : "types of expenses"}

@app.post("/expenses")
async def create_item(item: Expense):
    global next_id
    item.id = next_id
    next_id += 1
    expense.append(item)
    return item

@app.get("/expenses")
async def get_expense():
    return expense

expense1 = Expense(
    amount = 100,
    category = "shoe",
    description = "Nike airForce"
)
expense.append(expense1)

expense2 = Expense(
    amount = 200,
    category = "watch",
    description = "swatch watch"
)
expense.append(expense2)
