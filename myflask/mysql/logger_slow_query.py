import logging
from logging.handlers import RotatingFileHandler

from flask_sqlalchemy import get_debug_queries

"""
main process
"""

app.config['DATABASE_QUERY_TIMEOUT'] = 0.001
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler('slow_query.log', maxBytes=10000, backupCount=10)
handler.setlevel(logging.WARN)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= app.config['DATABASE_QUERY_TIMEOUT']:
            app.logger.warn(
                ('Context:{}\nSLOW QUERY: {}\nParameters: {}\n'
                'Duration: {}\n').format(query.context, query.statement,
                                    query.parameters, query.duration))
    return response