from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()
FILE_PATH = "archives.json"

class Record(BaseModel):
    id: int
    title: str
    content: str
    category: str
    date_added: str

def read_file():
    try:
        with open(FILE_PATH, "r") as file:
            return json.loads(file.read())
    except:
        return []

def write_file(records):
    with open(FILE_PATH, "w") as file:
        json.dump(records, file)

@app.get("/")
async def home():
    return {"message": "Welcome to Archives API"}

@app.post("/records/")
async def create_record(record: Record):
    records = read_file()
    
    record_dict = record.dict()
    records.append(record_dict)
    write_file(records)
    return {"message": "Record created"}

@app.get("/records/")
async def get_records():
    return {"records": read_file()}

@app.get("/records/{id}")
async def get_record(id: int):
    records = read_file()
    for record in records:
        if record["id"] == id:
            return record
    return {"message": "404 Not Found"}


@app.put("/records/{id}")
async def update_record(id: int, updated_data: dict):
    records = read_file()
    for record in records:
        if record["id"] == id:
            
            if "title" in updated_data:
                record["title"] = updated_data["title"]
            if "content" in updated_data:
                record["content"] = updated_data["content"]
            if "category" in updated_data:
                record["category"] = updated_data["category"]
            
            write_file(records)
            return {"message": "Record updated", "record": record}
    
    return {"message": "Record not found"}


@app.delete("/records/{id}")
async def delete_record(id: int):
    records = read_file()
    new_records = []
    found = False
    
    for record in records:
        if record["id"] != id:
            new_records.append(record)
        else:
            found = True

    write_file(new_records)
    if found:
        return {"message": "Deleted"}
    else:
        return {"message": "Record not found"}

@app.get("/records/search/")
async def search_records(title: str = None, category: str = None):
    if title is None and category is None:
        return {"message": "Enter a  title or category"}
    
    records = read_file()
    results = []
    
    for record in records:
        title_match = not title or title in record["title"]
        category_match = not category or category == record["category"]
    
    if title_match and category_match:
            results.append(record)
    
    return {"results": results}