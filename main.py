import uuid

from apscheduler.schedulers.background import BlockingScheduler

from pastebin_crawler.helpers.logger import Logger
from pastebin_crawler.workers.pastebin_worker import PasteBinWorker

if __name__ == "__main__":
    with Logger().logger.contextualize(task_id=str(uuid.uuid4())):
        background_scheduler = BlockingScheduler()
        background_scheduler.add_job(
            PasteBinWorker().run, "interval", seconds=60 * 2
        )
        background_scheduler.start()
