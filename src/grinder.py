from datetime import datetime
from sys import exc_info
from time import sleep

from scripts.adventure import adventure
from scripts.beg import beg
from scripts.blackjack import blackjack
from scripts.crime import crime
from scripts.custom import custom
from scripts.daily import daily
from scripts.dig import dig
from scripts.fish import fish
from scripts.guess import guess
from scripts.highlow import highlow
from scripts.hunt import hunt
from scripts.lottery import lottery
from scripts.postmeme import postmeme
from scripts.search import search
from scripts.snakeeyes import snakeeyes
from scripts.stream import stream
from scripts.trivia import trivia
from scripts.vote import vote
from scripts.work import work
from utils.Shared import data


def grind(Client):
    if Client.Repository.database["confirmations"] == "False":
        try:
            Client.send_message("pls settings confirmations nah")
            Client.Repository.database["confirmations"] = "True"
            Client.Repository.database_write()
        except Exception:
            if Client.Repository.config["logging"]["warning"]:
                Client.log(
                    "WARNING",
                    f"An unexpected error occured during the running of the `pls settings confirmations nah` command: `{exc_info()}`.",
                )

    while True:
        if Client.Repository.config["custom commands"]["enabled"]:
            while True:
                try:
                    for key in Client.Repository.config["custom commands"]:
                        if key == "enabled":
                            continue
                        if Client.Repository.config["custom commands"][key]["enabled"]:
                            try:
                                exec(
                                    f"if (datetime.now() - datetime.strptime(Client.Repository.database['custom command cooldowns']['{key.replace(' ', '_')}'], '%Y-%m-%d %H:%M:%S.%f')).total_seconds() > Client.Repository.config['custom commands'][key]['cooldown']: custom(Client, key); Client.Repository.database['custom command cooldowns']['{key.replace(' ', '_')}'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'); Client.Repository.database_write(); sleep(Client.Repository.config['cooldowns']['commands']['value'] if Client.Repository.config['cooldowns']['commands']['enabled'] else 0.5)"
                                )
                            except KeyError:
                                custom(Client, key)

                                exec(f"Client.Repository.database['custom command cooldowns']['{key.replace(' ', '_')}'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'); Client.Repository.database_write()")
                    break
                except Exception:
                    Client.log(
                        "WARNING",
                        f"An unexpected error occured during the running of the custom commands: `{exc_info()}`.",
                    )

        if (
            Client.Repository.config["commands"]["adventure"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["adventure"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config["cooldowns"]["adventure"]:
                try:
                    adventure(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls adventure` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "adventure"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])
        if (
            Client.Repository.config["commands"]["beg"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["beg"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["beg"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["beg"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "beg"
            ][
                "default"
            ]:
                try:
                    beg(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls beg` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "beg"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["blackjack"]["enabled"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["blackjack"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["blackjack"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["blackjack"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "blackjack"
            ][
                "default"
            ]:
                try:
                    blackjack(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls blackjack` command: `{exc_info()}`.",
                        )

                        try:
                            Client.clear_lag("pls blackjack")
                        except Exception:
                            Client.log(
                                "WARNING",
                                f"Failed to clear lag from the `pls blackjack` command failing: `{exc_info()}`. Backlash expected (if commands keep failing after this, it would be advisable to close Grank, wait a few minutues, and re-open Grank).",
                            )

                Client.Repository.database["cooldowns"][
                    "blackjack"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["crime"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["crime"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["crime"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["crime"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "crime"
            ][
                "default"
            ]:
                try:
                    crime(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls crime` command: `{exc_info()}`.",
                        )

                        try:
                            Client.clear_lag("pls crime")
                        except Exception:
                            Client.log(
                                "WARNING",
                                f"Failed to clear lag from the `pls crime` command failing: `{exc_info()}`. Backlash expected (if commands keep failing after this, it would be advisable to close Grank, wait a few minutues, and re-open Grank).",
                            )

                Client.Repository.database["cooldowns"][
                    "crime"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["daily"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["daily"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config["cooldowns"]["daily"]:
                try:
                    daily(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls daily` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "daily"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])
        if (
            Client.Repository.config["commands"]["dig"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["dig"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["dig"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["dig"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "dig"
            ][
                "default"
            ]:
                try:
                    dig(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls dig` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "dig"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["fish"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["fish"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["fish"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["fish"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "fish"
            ][
                "default"
            ]:
                try:
                    fish(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls fish` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "fish"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["guess"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["guess"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config["cooldowns"]["guess"]:
                try:
                    guess(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls guess` command: `{exc_info()}`.",
                        )

                    Client.send_message("end")

                Client.Repository.database["cooldowns"][
                    "guess"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["highlow"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["highlow"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["highlow"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["highlow"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "highlow"
            ][
                "default"
            ]:
                try:
                    highlow(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls highlow` command: `{exc_info()}`.",
                        )

                        try:
                            Client.clear_lag("pls highlow")
                        except Exception:
                            Client.log(
                                "WARNING",
                                f"Failed to clear lag from the `pls highlow` command failing: `{exc_info()}`. Backlash expected (if commands keep failing after this, it would be advisable to close Grank, wait a few minutues, and re-open Grank).",
                            )

                Client.Repository.database["cooldowns"][
                    "highlow"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["hunt"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["hunt"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["hunt"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["hunt"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "hunt"
            ][
                "default"
            ]:
                try:
                    hunt(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls hunt` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "hunt"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["lottery"]["enabled"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["lottery"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config["lottery"]["cooldown"]:
                try:
                    lottery(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls lottery` command: `{exc_info()}`.",
                        )

                        try:
                            Client.clear_lag("pls lottery")
                        except Exception:
                            Client.log(
                                "WARNING",
                                f"Failed to clear lag from the `pls lottery` command failing: `{exc_info()}`. Backlash expected (if commands keep failing after this, it would be advisable to close Grank, wait a few minutues, and re-open Grank).",
                            )

                Client.Repository.database["cooldowns"][
                    "lottery"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["postmeme"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["postmeme"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["postmeme"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["postmeme"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "postmeme"
            ][
                "default"
            ]:
                try:
                    postmeme(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls postmeme` command: `{exc_info()}`.",
                        )

                        try:
                            Client.clear_lag("pls postmeme")
                        except Exception:
                            Client.log(
                                "WARNING",
                                f"Failed to clear lag from the `pls postmeme` command failing: `{exc_info()}`. Backlash expected (if commands keep failing after this, it would be advisable to close Grank, wait a few minutues, and re-open Grank).",
                            )

                Client.Repository.database["cooldowns"][
                    "postmeme"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["search"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["search"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["search"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["search"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "search"
            ][
                "default"
            ]:
                try:
                    search(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls search` command: `{exc_info()}`.",
                        )

                        try:
                            Client.clear_lag("pls search")
                        except Exception:
                            Client.log(
                                "WARNING",
                                f"Failed to clear lag from the `pls search` command failing: `{exc_info()}`. Backlash expected (if commands keep failing after this, it would be advisable to close Grank, wait a few minutues, and re-open Grank).",
                            )

                Client.Repository.database["cooldowns"][
                    "search"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["snakeeyes"]["enabled"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["snakeeyes"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["snakeeyes"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["snakeeyes"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "snakeeyes"
            ][
                "default"
            ]:
                try:
                    snakeeyes(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls snakeeyes` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "snakeeyes"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["stream"]["enabled"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["stream"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config["cooldowns"]["stream"]:
                try:
                    stream(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls stream` command: `{exc_info()}`.",
                        )

                        try:
                            Client.clear_lag("pls stream", -1)
                        except Exception:
                            Client.log(
                                "WARNING",
                                f"Failed to clear lag from the `pls stream` command failing: `{exc_info()}`. Backlash expected (if commands keep failing after this, it would be advisable to close Grank, wait a few minutues, and re-open Grank).",
                            )

                Client.Repository.database["cooldowns"][
                    "stream"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])
        if (
            Client.Repository.config["commands"]["trivia"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                Client.Repository.config["settings"]["patron"]
                and (
                    datetime.now()
                    - datetime.strptime(
                        Client.Repository.database["cooldowns"]["trivia"],
                        "%Y-%m-%d %H:%M:%S.%f",
                    )
                ).total_seconds()
                > Client.Repository.config["cooldowns"]["trivia"]["patron"]
            ) or (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["trivia"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config[
                "cooldowns"
            ][
                "trivia"
            ][
                "default"
            ]:
                try:
                    trivia(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls trivia` command: `{exc_info()}`.",
                        )

                        try:
                            Client.clear_lag("pls trivia")
                        except Exception:
                            Client.log(
                                "WARNING",
                                f"Failed to clear lag from the `pls trivia` command failing: `{exc_info()}`. Backlash expected (if commands keep failing after this, it would be advisable to close Grank, wait a few minutues, and re-open Grank).",
                            )

                Client.Repository.database["cooldowns"][
                    "trivia"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        if (
            Client.Repository.config["commands"]["vote"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["vote"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config["cooldowns"]["vote"]:
                try:
                    vote(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls vote` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "vote"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])
        if (
            Client.Repository.config["commands"]["work"]
            and data[Client.username]
            and data["channels"][Client.channel_id][Client.token]
        ):
            if (
                datetime.now()
                - datetime.strptime(
                    Client.Repository.database["cooldowns"]["work"],
                    "%Y-%m-%d %H:%M:%S.%f",
                )
            ).total_seconds() > Client.Repository.config["cooldowns"]["work"]:
                try:
                    work(Client)
                except Exception:
                    if Client.Repository.config["logging"]["warning"]:
                        Client.log(
                            "WARNING",
                            f"An unexpected error occured during the running of the `pls work` command: `{exc_info()}`.",
                        )

                Client.Repository.database["cooldowns"][
                    "work"
                ] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                Client.Repository.database_write()

                if Client.Repository.config["cooldowns"]["commands"]["enabled"]:
                    sleep(Client.Repository.config["cooldowns"]["commands"]["value"])

        while (
            not data[Client.username]
            or not data["channels"][Client.channel_id][Client.token]
        ):
            if not data["channels"][Client.channel_id][Client.token]:
                Client.Repository.info["stats"]["commands_ran"] = (
                    Client.lifetime_commands_ran
                    + data["stats"][Client.token]["commands_ran"]
                )
                Client.Repository.info["stats"]["buttons_clicked"] = (
                    Client.lifetime_buttons_clicked
                    + data["stats"][Client.token]["buttons_clicked"]
                )
                Client.Repository.info["stats"]["dropdowns_selected"] = (
                    Client.lifetime_dropdowns_selected
                    + data["stats"][Client.token]["dropdowns_selected"]
                )
                Client.Repository.info["stats"]["coins_gained"] = (
                    Client.lifetime_coins_gained
                    + data["stats"][Client.token]["coins_gained"]
                )
                Client.Repository.info_write()
                return
