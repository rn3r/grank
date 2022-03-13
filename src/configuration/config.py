from yaml import safe_load
from utils.logger import log
from discord.gateway import gateway
from requests import get
from json import loads

def load_config(cwd):
	config = safe_load(open(f"{cwd}config.yml", "r"))

	options = ["['commands']", "['commands']['crime']", "['commands']['daily']", "['commands']['beg']", "['commands']['fish']", "['commands']['guess']", "['commands']['hunt']", "['commands']['dig']", "['commands']['search']", "['commands']['highlow']", "['commands']['postmeme']", "['commands']['trivia']", "['custom commands']", "['custom commands']['enabled']", "['shifts']", "['shifts']['enabled']", "['shifts']['active']", "['shifts']['passive']", "['lottery']", "['lottery']['enabled']", "['lottery']['cooldown']", "['stream']", "['stream']['ads']", "['stream']['chat']", "['stream']['donations']", "['auto buy']", "['auto buy']['enabled']", "['auto buy']['laptop']", "['auto buy']['shovel']", "['auto buy']['fishing pole']", "['auto buy']['hunting rifle']", "['auto buy']['keyboard']", "['auto buy']['mouse']", "['auto trade']", "['auto trade']['enabled']", "['auto trade']['trader token']", "['typing indicator']", "['typing indicator']['enabled']", "['typing indicator']['minimum']", "['typing indicator']['maximum']", "['cooldowns']", "['cooldowns']['patron']", "['cooldowns']['timeout']", "['logging']['debug']", "['logging']['warning']"]

	for option in options:
		try:
			exec(f"_ = config{option}")
		except KeyError:
			log(None, "ERROR", f"Unable to find configuration option for `{option}`. Make sure it is present.")


	if config["auto trade"]["enabled"]:
		request = get("https://discord.com/api/v10/users/@me", headers={"authorization": config["auto trade"]["trader_token"]})

		if request.status_code != 200:
			log(None, "ERROR", "Invalid trader token set. Please double-check you entered a valid token in `config.yml`.")

		request = loads(request.text)

		config["auto trade"]["trader"] = {}
		config["auto trade"]["trader"]["username"] = f"{request['username']}#{request['discriminator']}"
		config["auto trade"]["trader"]["user_id"] = request["id"]
		config["auto trade"]["trader"]["session_id"] = gateway(config["auto trade"]["trader_token"])
		
	return config