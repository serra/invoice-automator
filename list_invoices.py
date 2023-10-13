import os
import requests

query = """
{
  findInvoices(invoiceLines: {containsAny: {}}) {
    id
    name
    invoiceLines {
      name
    }
  }
}
"""

url = os.environ["SPACE_URL"]
token = os.environ["FIBERY_API_TOKEN"]

headers = {"Content-Type": "application/json", "Authorization": "Token " + token}

response = requests.post(url, json={"query": query}, headers=headers)
print(response.json())
