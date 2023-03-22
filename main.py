import requests, os
from dotenv import load_dotenv

# load the dot env
load_dotenv()
# get the RAPID API KEY
RAPID_KEY = os.environ['YH_FINANCE_API_KEY']

def getFinancials(symbol:str):
    """  
    Given symbol : str = ticker quote for corporate stock
    Return json format of the API data
    """
    import requests

    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-financials"

    querystring = {"symbol":symbol}

    headers = {
        "X-RapidAPI-Key": RAPID_KEY,
        "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return response

def main():
    print(f'YH finance API\n')
    
    # requests get-financials
    financials = getFinancials('tlkm.jk')
    # print(f'whole data: {financials}')
    print(f"stock code: {financials['quoteType']['symbol']}")

if __name__ == '__main__':
    main()