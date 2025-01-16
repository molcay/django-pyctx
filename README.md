PyCTX for Django
================

**django-pyctx** is a context package to use data between function calls, use timers and log it.

For detailed documentation please visit [Wiki](https://github.com/molcay/django-pyctx/wiki).

Quick Start
-----------

1. Add **django_pyctx** to your ``INSTALLED_APPS``  setting like this:

   ```python
   INSTALLED_APPS = [
    #...,
    "django_pyctx",
   ]
   ```

2. Add **django_pyctx.middlewares.RequestCTXMiddleware** to your ``MIDDLEWARE`` setting like this:

   ```python
   MIDDLEWARE = [
     "django_pyctx.middlewares.RequestCTXMiddleware",
     # ...,
   ]
   ```

> Please add "django_pyctx.middlewares.RequestCTXMiddleware" to at the beginning of the MIDDLEWARE list.

3. Start the development server and enjoy :)

Sample Usage
------------

- You can reach `RequestContext` instance in **views** from `request`: `request.ctx`

- Example django function-based `view`:

    ```python
  from django.http import JsonResponse
  
  
  def index(request):
        y = 5
        with request.ctx.log.timeit('index_timer'):
            request.ctx.log.set_data('isEven', y % 2)
            request.ctx.log.set_data('y', y)
            request.ctx.log.start_timer('timer1')
            import time
            time.sleep(0.3)
            request.ctx.log.stop_timer('timer1')
            time.sleep(0.8)
            return JsonResponse({})
    ```

You can see the stdout. You are probably seeing something like this:

```json
{
  "type": "REQ",
  "ctxId": "a9b66113-aa96-4419-b9ec-961ce0ebf3ae",
  "startTime": "2019-08-23 13:47:46.146172",
  "endTime": "2019-08-23 13:47:47.258287",
  "data": {
    "isEven": 1,
    "y": 5
  },
  "timers": {
    "ALL": 1.112128,
    "request": 1.112115,
    "index_timer": 1.107513,
    "timer1": 0.302767
  },
  "http": {
    "request": {
      "method": "GET",
      "path": "/ctxtest",
      "qs": "",
      "full_path": "/ctxtest",
      "is_secure": false,
      "is_xhr": false,
      "headers": {
        "Content-Length": "",
        "Content-Type": "text/plain",
        "Host": "localhost:8000",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Dnt": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Sec-Fetch-Site": "none",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "tr,en-GB;q=0.9,en;q=0.8,en-US;q=0.7",
        "Cookie": "Pycharm-358d8f24=40efd37d-3767-43c2-8704-8abdbc8e441c; hblid=2S0d7GIKtYrYxbaF3m39N0M07TEBJbrW; olfsk=olfsk09308937734654421; Pycharm-358d92e3=f744a971-3d23-48a3-8188-7818d8efeb90; jenkins-timestamper-offset=-10800000; Pycharm-358d92e4=39469e28-3138-45a1-8133-16b05a158037; __test=1; csrftoken=qAbZmh519QGb6c1h702qe3YOtL8Q0ADakbXqqj4o5G5UznTybJVPigGG1mDBTtgP; Idea-535a2bcb=d87ec75d-65c5-46dd-a04b-6e914b434b5a; lang=en-US; iconSize=32x32; JSESSIONID.3e560a2e=node015mpq963ev6tulzcbplgyu8i1438.node0"
      }
    },
    "client": {
      "ip": "127.0.0.1",
      "host": "",
      "agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    },
    "status": {
      "code": 200,
      "phrase": "OK"
    },
    "server": {
      "name": "1.0.0.127.in-addr.arpa",
      "port": "8000"
    },
    "view": "run"
  }
}
```
> NOTE: this output formatted
