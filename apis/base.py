import urllib.parse

# URL
URL_VAL_ORIGIN = "https://{server_region}.api.riotgames.com"
URL_VAL_CONTENTS = "/val/content/v1/contents"
URL_VAL_GET_PUUID_BY_RIOT_ID = "/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
URL_VAL_GET_MATCHLISTS_BY_PUUID = "/val/match/v1/matchlists/by-puuid/{puuid}"
URL_VAL_GET_MATCH = "/val/match/v1/matches/{match_id}"
URL_VAL_RANKED_LEADERBOARD_BY_ACT = "/val/ranked/v1/leaderboards/by-act/{act_id}"


# SERVER REGIONS
REGION_VAL_ACC_ASIA = "asia"
REGION_VAL_ACC_AMERICAS = "americas"
REGION_VAL_ACC_EUROPE = "europe"
REGION_VAL_ACC_ALL = [REGION_VAL_ACC_ASIA, REGION_VAL_ACC_AMERICAS, REGION_VAL_ACC_EUROPE]

REGION_VAL_CONTENT_AP = 'ap'
REGION_VAL_CONTENTS_BR = 'br'
REGION_VAL_CONTENTS_ESPORTS = 'esports'
REGION_VAL_CONTENTS_EU = 'eu'
REGION_VAL_CONTENTS_KR = 'kr'
REGION_VAL_CONTENTS_LATAM = 'latam'
REGION_VAL_CONTENTS_NA = 'na'
REGION_VAL_CONTENTS_ALL = [REGION_VAL_CONTENT_AP, REGION_VAL_CONTENTS_BR, REGION_VAL_CONTENTS_ESPORTS,
                           REGION_VAL_CONTENTS_EU, REGION_VAL_CONTENTS_KR, REGION_VAL_CONTENTS_LATAM,
                           REGION_VAL_CONTENTS_NA]


def build_url(base_url: str, path: str, **kwargs):
    url_parts = list(urllib.parse.urlparse(base_url))
    url_parts[2] = path
    url_parts[4] = urllib.parse.urlencode(kwargs)
    return urllib.parse.urlunparse(url_parts)


class API:
    api_key: str
    api_origin_url: str

    def __init__(self, api_key: str, api_origin_url: str):
        self.api_key = api_key
        self.api_origin_url = api_origin_url


class User:
    pass


if __name__ == '__main__':
    # Test URL building
    print(build_url(
        URL_VAL_ORIGIN.format(server_region=REGION_VAL_ACC_ASIA),
        URL_VAL_GET_PUUID_BY_RIOT_ID.format(game_name="billa", tag_line="gulla"),
        api_key="api_key",
        puuid="some-&puuid"
    ))
