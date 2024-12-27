from rq import Queue
from redis import Redis
import sendreq

q = Queue(connection=Redis(), default_timeout=1800)

def queue_tasks(z, conc):
    _ = q.enqueue_many(
        [
            Queue.prepare_data(
                "sendreq.send_req", args=("https://dev.syphoon.com/api", "https://www.test.internal", "GET", "", conc), result_ttl=1
            )
            for _ in range(z)
        ]
    )