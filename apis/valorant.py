import requests

from apis.base import (
    URL_VAL_ORIGIN,
    URL_VAL_GET_MATCHLISTS_BY_PUUID,
    URL_VAL_GET_MATCH,
    URL_VAL_GET_PUUID_BY_RIOT_ID,
    URL_VAL_CONTENTS
)
from apis.base import REGION_VAL_ACC_ASIA
from apis.base import REGION_VAL_CONTENT_AP
from apis.base import API, build_url


class Agent:
    name: str
    character_id: str

    def __init__(self, name: str, character_id: str):
        self.name = name
        self.character_id = character_id

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name


class Round:
    pass


class Match:
    def __init__(self, match_info, players, coaches, teams, round_results):
        self.match_info = match_info
        self.players = players
        self.coaches = coaches
        self.teams = teams
        self.round_results = round_results

    def get_round_analytics(self, round_num: int):
        pass

    def get_all_round_analytics(self):
        pass


class ValorantAPI(API):
    """
    #######################################################################################

    #################### EXAMPLE RESPONSES FOR EACH RESPONSE CODE TYPE ####################

    #######################################################################################

    #####----- CODE 200 -----#####
    REQUEST URL
    https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/billa/gulla

    REQUEST HEADERS
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": "RGAPI-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }

    RESPONSE CODE
    200

    RESPONSE HEADERS
    {
        "Date": "Tue, 17 Oct 2023 14:57:58 GMT",
        "Content-Type": "application/json;charset=utf-8",
        "Transfer-Encoding": "chunked",
        "Connection": "keep-alive",
        "Access-Control-Allow-Headers": "Content-Type, DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range",
        "Access-Control-Allow-Methods": "GET, POST, DELETE, PUT, GET, PUT, DELETE, POST, OPTIONS",
        "Access-Control-Allow-Origin": "*, *",
        "Vary": "Accept-Encoding",
        "X-App-Rate-Limit": "20:1,100:120",
        "X-App-Rate-Limit-Count": "1:1,2:120",
        "X-Method-Rate-Limit": "1000:60",
        "X-Method-Rate-Limit-Count": "2:60",
        "X-Riot-Edge-Trace-Id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "Content-Encoding": "gzip",
        "Access-Control-Expose-Headers": "Content-Length,Content-Range"
    }

    RESPONSE BODY
    {
        "puuid": "xxxx_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxx-xxxxxxxxxxxxxxxxxx",
        "gameName": "biLLa",
        "tagLine": "gulla"
    }



    #####----- CODE 404 -----#####
    REQUEST URL
    https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/bill/gull

    REQUEST HEADERS
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": "RGAPI-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }

    RESPONSE CODE
    404

    RESPONSE HEADERS
    {
        "Date": "Tue, 17 Oct 2023 15:02:54 GMT",
        "Content-Type": "application/json;charset=utf-8",
        "Transfer-Encoding": "chunked",
        "Connection": "keep-alive",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "GET, POST, DELETE, PUT",
        "Access-Control-Allow-Origin": "*",
        "Vary": "Accept-Encoding",
        "X-App-Rate-Limit": "20:1,100:120",
        "X-App-Rate-Limit-Count": "1:1,1:120",
        "X-Method-Rate-Limit": "1000:60",
        "X-Method-Rate-Limit-Count": "1:60",
        "X-Riot-Edge-Trace-Id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "Content-Encoding": "gzip"
    }

    RESPONSE BODY
    {
        "status": {
            "status_code": 404,
            "message": "Data not found - No results found for player with riot id bill#gull"
        }
    }
    """
    def __init__(self, api_key: str, api_url: str):
        super().__init__(api_key, api_url)

    def get_puuid(self, server_region: str, game_name: str, tag_line: str) -> str:
        """
        Gets the player (game_name#tag_line) puuid for the server region `server_region`.

        :param server_region: server region to fetch data from
        :param game_name: the in-game name of player
        :param tag_line: the characters after `#` in Riot ID
        :return: puuid of the player
        """
        return requests.get(
            build_url(
                base_url=self.api_origin_url.format(server_region=server_region),
                path=URL_VAL_GET_PUUID_BY_RIOT_ID.format(
                    game_name=game_name,
                    tag_line=tag_line
                ),
                api_key=self.api_key
            )
        ).json()["puuid"]

    def get_match_ids(self, server_region: str, game_name: str, tag_line: str) -> list:
        """
        Get the last n number of matches played by the player.

        :return: list of match IDs
        """
        return list(
            map(
                lambda x: x["matchId"],
                requests.get(
                    build_url(
                        base_url=self.api_origin_url.format(server_region=server_region),
                        path=URL_VAL_GET_MATCHLISTS_BY_PUUID.format(
                            puuid=self.get_puuid(
                                server_region=server_region,
                                game_name=game_name,
                                tag_line=tag_line
                            )
                        ),
                        api_key=self.api_key
                    )
                ).json()["history"]
            )
        )

    def get_match_details(self, server_region: str, match_id: str) -> Match:
        match = requests.get(
            build_url(
                base_url=self.api_origin_url.format(server_region=server_region),
                path=URL_VAL_GET_MATCH.format(match_id=match_id),
                api_key=self.api_key
            )
        ).json()
        return Match(
            match_info=match['matchInfo'],
            players=match['players'],
            coaches=match['coaches'],
            teams=match['teams'],
            round_results=match['roundResults'],
        )

    def get_agents(self, server_region=REGION_VAL_CONTENT_AP) -> list[Agent]:
        return [
            Agent(name=name, character_id=cid)
            for name, cid in list(
                map(
                    lambda x: (x['name'], x['id']),
                    requests.get(
                        build_url(
                            base_url=self.api_origin_url.format(server_region=server_region),
                            path=URL_VAL_CONTENTS,
                            locale="id-ID",
                            api_key=self.api_key
                        )
                    ).json()["characters"]
                )
            )
        ]


if __name__ == '__main__':
    v = ValorantAPI(open("../.secrets").read(), URL_VAL_ORIGIN)
    # p = v.get_puuid(REGION_VAL_ACC_ASIA, "billa", "gulla")
    # print(p)
    a = sorted(v.get_agents())
    for i in a:
        print("C_ID: ", i.character_id, "\tName: ", i.name)
