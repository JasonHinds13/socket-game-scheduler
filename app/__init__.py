from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from logging.config import dictConfig
from app.logging_helper.LogFilter import LogFilter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
app.config['ROOM_BACK_OFF'] = getenv("ROOM_BACK_OFF")
app.config['PLAYER_INACTIVITY'] = getenv("PLAYER_INACTIVITY")
app.config['SCHEDULER_ROOM_DEACTIVATION'] = getenv("SCHEDULER_ROOM_DEACTIVATION")
app.config['SCHEDULER_ROOM_DELETION'] = getenv("SCHEDULER_ROOM_DELETION")
log_level = getenv("ROOT_LOG_LEVEL")
default_format = getenv('DEFAULT_FORMAT')
log_path = getenv("LOGGING_FILE_PATH")

# Configure app logger
dictConfig({
    'version': 1,
    'filters': {
        'default_filter': {
            '()': LogFilter
        }
    },
    'formatters': {'default': {
        'format': default_format,
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default',
        'filters': ['default_filter']
    },
        'file': {
        'class': 'logging.handlers.TimedRotatingFileHandler',
        'filename': log_path,
        'formatter': 'default',
        'when': 'midnight',
        'utc': 'True',
        'interval': 1,
        'backupCount': 5,
        'filters': ['default_filter']
        }
    },
    'root': {
        'level': log_level,
        'handlers': ['wsgi', 'file']
    }
})
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning
db = SQLAlchemy(app)
