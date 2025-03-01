import time


class QueryTimer:
    """
    Taken from: https://docs.djangoproject.com/en/5.1/topics/db/instrumentation/#database-instrumentation
    """
    def __init__(self):
        self.queries = []

    def __call__(self, execute, sql, params, many, context):
        current_query = {"sql": sql, "params": params, "many": many}
        start = time.monotonic()
        try:
            result = execute(sql, params, many, context)
        except Exception as e:
            current_query["status"] = "error"
            current_query["exception"] = e
            raise
        else:
            current_query["status"] = "ok"
            return result
        finally:
            duration = time.monotonic() - start
            current_query["duration"] = duration
            self.queries.append(current_query)

    def to_log_list(self):
        return [
            {
                'sql': item['sql'],
                'status': item['status'],
                'duration': item['duration'],
            }
            for item in self.queries
        ]
