from src.app.infrastructure.celery.worker import celery_app


@celery_app.task
def test_background_task(name: str):
    print(f"Background task executed {name}")

    return f"Hello {name}"
