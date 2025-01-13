from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
from datetime import datetime

from config import database_config


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GuestSchema(BaseModel):
    fullnames: str
    is_present: bool
    will_congratulating: bool
    meat_or_fish: str


@app.post('/save_form')
async def save_form(data: GuestSchema):
    with psycopg2.connect(
        database=database_config.DB_NAME,
        user=database_config.DB_USER,
        password=database_config.DB_PASSWORD,
        host=database_config.DB_HOST,
        port=database_config.DB_PORT
    ) as conn:
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO guests_form (fullnames, is_present, will_congratulating, meat_or_fish)
                    VALUES (%(fullnames)s, %(is_present)s, %(will_congratulating)s, %(meat_or_fish)s) returning *;
                    """,
                    data.model_dump()
                )

                result = cur.fetchone()
                print(f'Add new guest {result[-1].strftime("%Y/%m/%d %H:%M")}:  {result[:-1]}')

                return result
        except Exception as error:
            print(error)
            raise HTTPException(status_code=504, detail="Can't save data to base")



