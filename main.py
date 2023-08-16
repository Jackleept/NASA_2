import requests
from datetime import datetime

now = datetime.today()
today = now.strftime("%Y-%m-%d")

link = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-08-08&end_date=TODAY&api_key=Gt87ibmZefPpnhl8gfz5gWWiTuftebq6IgJBFNdQ"

link_today = link.replace("TODAY", today)

response = requests.get(link_today)

print(response.json())