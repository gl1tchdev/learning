import calendar, time
from fastapi import FastAPI
from rpc import models
from rpc.celery import celery

app = FastAPI()
celery_app = celery

@app.post('/get_md5', response_model=models.Answer)
async def get_hash_of_string(str_handle: models.StringHandle):
    request = models.Request(
        input=str_handle.input,
        timestamp=calendar.timegm(time.gmtime()),
    )
    result = celery_app.send_task('get_md5', args=(models.cls_to_json(request),)).get()
    processed_result: models.Answer = models.json_to_cls(models.Answer, result)
    return processed_result