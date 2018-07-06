from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.core.management import call_command
from celery.utils.log import get_task_logger

# from photos.utils import save_latest_flickr_image

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='1')),
    name="create_hit_command"
)
def create_hit_command():
    logger.info("Start task")
    now = datetime.now()
    # result = scrapers.scraper_example(now.day, now.minute)
    logger.info("Task finished:")
    """args = []
    options = {'label':0,'image_limit':10}
    call_command('create_hits', *args, **options)
    logger.info("Saved image from Flickr")"""
