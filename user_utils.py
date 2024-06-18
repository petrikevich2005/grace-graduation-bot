#user_utis
import sqlite3
import utils

logger = utils.get_logger('user_utils')

def add_to_database(user_id, username):
	logger.debug("add_to_database...")
	with sqlite3.connect("data.db") as cursor:
		cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (user_id, username, False, False, None, None))
	logger.info(f"user {user_id} added to the database")

def check_user_id(user_id):
	logger.debug("check_user_id...")
	with sqlite3.connect("data.db") as cursor:
		result = cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchone()
	return result is not None

def update_user(user_id, team_code, progress):
	logger.debug("update_user...")
	with sqlite3.connect("data.db") as cursor:
		state = cursor.execute("SELECT user_id FROM users WHERE team_code = ?", (team_code,)).fetchone()
	if state is None or state[0] == user_id:
		with sqlite3.connect("data.db") as cursor:
			cursor.execute("UPDATE users SET team_code = ?, progress = ? WHERE user_id = ?", (team_code, progress, user_id))
		return True
	else:
		return False

def get_team_code(user_id):
	logger.debug("get_team_code...")
	with sqlite3.connect("data.db") as cursor:
		team_code = cursor.execute("SELECT team_code FROM users WHERE user_id = ?", (user_id,)).fetchone()
	if team_code is None:
		return None
	else:
		return team_code[0]

def get_progress(user_id):
	logger.debug("get_progress...")
	with sqlite3.connect("data.db") as cursor:
		progress = cursor.execute("SELECT progress FROM users WHERE user_id = ?", (user_id,)).fetchone()
	if progress is None:
		return None
	else:
		return progress[0]
