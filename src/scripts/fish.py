from utils.logger import log

def fish(Client) -> None:
	"""One of the basic 7 currency commands - `pls fish`.
 
	Required item(s): Fishing pole

	Args:
		Client (class): The Client for the user.

	Returns:
		None
	"""
 
	Client.send_message("pls fish")

	latest_message = Client.retreive_message("pls fish")

	if latest_message["content"] == "You don't have a fishing pole, you need to go buy one. You're not good enough to catch them with your hands.":
		if Client.config["logging"]["debug"]:
			log(Client.username, "DEBUG", "User does not have item `fishing pole`. Buying fishing pole now.")

		if Client.config["auto buy"] and Client.config["auto buy"]["fishing pole"]:
			from scripts.buy import buy
			buy(Client, "fishing pole")
			return
		elif Client.config["logging"]["warning"]:
			log(
				Client.username,
				"WARNING",
				f"A fishing pole is required for the command `pls fish`. However, since {'auto buy is off for fishing poles,' if Client.config['auto buy']['parent'] else 'auto buy is off for all items,'} the program will not buy one. Aborting command.",
			)
			return