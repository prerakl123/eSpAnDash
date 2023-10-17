class ValorantAPI:
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
        "X-Riot-Token": "RGAPI-10e73955-bb43-46d3-b9dd-54f224f5b28b"
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
        "X-Riot-Edge-Trace-Id": "d1c9a1d8-5068-4647-a7e0-d25cd4c5ff54",
        "Content-Encoding": "gzip",
        "Access-Control-Expose-Headers": "Content-Length,Content-Range"
    }

    RESPONSE BODY
    {
        "puuid": "xMJm_rDBAQ0JdeqEg7m5JBiF42tieSQg3M2AaIw8IbeTZaA9F-cL9isbwRV-2Uf8e3xzHfH5PsTAug",
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
        "X-Riot-Token": "RGAPI-10e73955-bb43-46d3-b9dd-54f224f5b28b"
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
        "X-Riot-Edge-Trace-Id": "703c06ca-b80d-402b-80c0-9cafa94cb161",
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
    def __init__(self):
        pass
