from app import database_cleanup, app

database_cleanup.initiate_schedule(app.config['SCHEDULER_ROOM_DEACTIVATION'], app.config['SCHEDULER_ROOM_DELETION'])
app.run(host="127.0.0.1")
