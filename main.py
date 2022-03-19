from project import create_app

app = create_app()

celery = app.celery_app  # type: ignore


@app.get("/")
async def root():
    return {"message": "Hello World"}


@celery.task
def divide(x, y):
    import time

    time.sleep(5)
    return x / y
