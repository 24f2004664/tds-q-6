from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("q-fastapi.csv")

records = df.to_dict(orient="records")


@app.get("/api")
async def get_students(
    class_: list[str] | None = Query(
        default=None,
        alias="class"
    )
):

    if not class_:
        return {
            "students": records
        }

    filtered = [
        row
        for row in records
        if row["class"] in class_
    ]

    return {
        "students": filtered
    }
