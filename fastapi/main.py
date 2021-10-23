from fastapi import FastAPI
# import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from router import router

app = FastAPI()


register_tortoise(
    app,
    db_url="sqlite://database.db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(router)


@app.get('/')
def hello():
    return {'message': 'hello world'}


# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=3000, debug=True)