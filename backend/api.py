from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from schema import GuestSchema
import psycopg2
from datetime import datetime
import uvicorn

from config import database_config, logger
from send_telegram import send_to_chat


app = FastAPI(title='Wedding site API')

v2_router = APIRouter(prefix='/api/v2')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@v2_router.post('/save_form')
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
                    INSERT INTO guests_form (name, present, marry, twoday, food)
                    VALUES (%(name)s, %(present)s, %(marry)s, %(twoday)s, %(food)s) returning *;
                    """,
                    data.model_dump()
                )

                result = cur.fetchone()
                logger.info(f'Add new guest {result[-1].strftime("%Y/%m/%d %H:%M")}:  {result[:-1]}')

        except Exception as error:
            logger.error(error)
            raise HTTPException(status_code=504, detail="Can't save data to base")

        send_to_chat(data)

        return result


@v2_router.get('/')
async def welcome():
    return 'Hello world'


app.include_router(v2_router)


if __name__ == '__main__':
    server_settings = {
        "host": '0.0.0.0',
        "port": 8080,
        "reload": False,
        "workers": None
    }
    uvicorn.run(app, **server_settings)

