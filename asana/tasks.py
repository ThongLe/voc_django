from celery.utils.log import get_task_logger
from celery.app import shared_task

logger = get_task_logger(__name__)


@shared_task(name="test_task")
def test_task():
    logger.info("Test task")
    return True


