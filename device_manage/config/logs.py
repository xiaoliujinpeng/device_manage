
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        'verbose': {
            'format': '{levelname} {asctime} {module}{message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': "./logs/django/info.log",
            'formatter': 'verbose',
            'when': 'D',
            'interval': 2,
            'backupCount': 5,
            'encoding': 'utf-8',
        },

    },
    'loggers': {

        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },

    }
}
