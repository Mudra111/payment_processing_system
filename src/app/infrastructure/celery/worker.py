from celery import Celery

from src.app.core.config import settings

# celery app
celery_app = Celery(
    "payment_processing", broker=settings.REDIS_URL, backend="redis://localhost:6379/1"
)

celery_app.conf.update(
    task_serializer="json",
    accept_content="json",
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    imports=["src.app.infrastructure.celery.tasks"],
)
