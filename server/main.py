from rpc import models, celery
from hashlib import md5

app = celery.get_app()

@app.task(name='get_md5')
def process_string(req: str) -> str:
    request = models.json_to_cls(models.Request, req)
    answer = models.Answer(
        output=md5(request.input.encode('utf-8')).hexdigest(),
        timestamp=request.timestamp
    )
    return models.cls_to_json(answer)