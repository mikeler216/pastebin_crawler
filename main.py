from pastebin_crawler.settings import background_scheduler
from pastebin_crawler.workers.pastebin_worker import PasteBinWorker

if __name__ == "__main__":
    PasteBinWorker().run()
    background_scheduler.add_job(
        PasteBinWorker().run, "interval", seconds=60 * 2
    )
    background_scheduler.start()
