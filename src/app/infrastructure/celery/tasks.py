from src.app.infrastructure.celery.worker import celery_app


@celery_app.task
def test_background_task(name: str):
    print(f"Background task executed {name}")

    return f"Hello {name}"


@celery_app.task
def payment_task(payment_id: int):
    print(f"payment processing start : {payment_id}")

    return "Payment processing started"
