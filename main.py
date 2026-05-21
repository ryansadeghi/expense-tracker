from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import date

app = FastAPI()
next_id = 1

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

@app.get("/expenses/{id}")
async def get_one_expense(id: int):
    for item in expense:
        if item.id == id:
            return item
    raise HTTPException(status_code = 404, detail = "Expense not found")


@app.delete("/expenses/{id}")
async def delete_one_expense(id: int):
    for item in expense:
        if item.id == id:
            expense.remove(item)
            return {"Message" : "Item has been deleted"}
    raise HTTPException(status_code = 404, detail = "Item could not be found")