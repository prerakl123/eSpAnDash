# URL
URL_VAL_ORIGIN = "https://{server_region}.api.riotgames.com"
URL_VAL_CONTENTS = "/val/content/v1/contents"
URL_VAL_GET_MATCHLISTS_BY_PUUID = "/val/match/v1/matchlists/by-puuid/{puuid}"
URL_VAL_GET_MATCH = "/val/match/v1/matches/{match_id}"

# URL QUERY PARAMETERS
QUERY_PARAM_VAL_API_KEY = "api_key"

# SERVER REGIONS
REGION_VAL_ASIA = "asia"
REGION_VAL_AMERICAS = "americas"
REGION_VAL_EUROPE = "europe"


class API:
    api_key: str
    api_url: str


class User:
    pass
