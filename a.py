from notion.client import NotionClient
from datetime import datetime
import yaml

with open("config.yaml",'r') as f:
    config = yaml.load(f,Loader=yaml.FullLoader)
token_v2 = config.pop("token_v2")
Bill_page = config.pop("Bill_page")
Cash_Flow_Calendar_collection = config.pop("Cash_Flow_Calendar_collection")

client = NotionClient(token_v2=token_v2)
page = client.get_block(Bill_page)
cv = client.get_collection_view(Cash_Flow_Calendar_collection)

flag = 0
MonthlyCosts = 0.0
for child in page.children:
    if child.title == None:
        continue
    if "Monthly Costs" in child.title:
        flag = 1
    elif "Saving for" in child.title:
        flag = 0

    if flag == 1:
        try:
            
            ite = float(str(child.title).split("￥")[1])
            MonthlyCosts += ite
        except:
            pass

print(MonthlyCosts)