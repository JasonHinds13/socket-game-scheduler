# Socket Game Scheduler
Scheduler for the socket game repository https://github.com/JasonHinds13/socket-game. It takes care of administrative
tasks.

## Config
This application uses environment variables for configuration. A list of config variables are listed below:
* `DEFAULT_FORMAT`: Format of system logs
* `ROOT_LOG_LEVEL`: Root logging level 
* `DATABASE_URL`:  Database url in the format for `DB_DRIVER://USERNAME:PASSWORD@DB_HOST/DATABASE`
* `ROOM_BACK_OFF`:  Back-off period in minute for checking if a room is active. 
* `PLAYER_INACTIVITY`: Number of minutes all users in a room should be inactive for before deactivating the room
* `SCHEDULER_ROOM_DEACTIVATION`: Interval in minutes between room inactivity check firing

## Startup Commands
* `virtualenv venv` (Optional)  
* `source venv/bin/activate` (linux or mac) / `venv\Scripts\activate` (Optional)
* `pip install -r requirements.txt`  
* `python run.py` 