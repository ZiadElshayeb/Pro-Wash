import requests
import os
import json
import uuid
from dotenv import load_dotenv

load_dotenv()

phone_number_id = os.environ.get("WHATSAPP_BUSINESS_PHONE_NUMBER_ID")
access_token = os.environ.get("ACCESS_TOKEN")

to_phone_number = "201013008808"
template_name = "pro_wash_v3"
language_code = "ar"

# ✅ Tracking token (string). Use a UUID or your own short correlation id.
flow_token = f"pro_wash_v3:{uuid.uuid4().hex}"

url = f"https://graph.facebook.com/v16.0/{phone_number_id}/messages"
headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

data = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": to_phone_number,
    "type": "template",
    "template": {
        "name": template_name,
        "language": {"code": language_code},
        "components": [
            {
                "type": "button",
                "sub_type": "flow",
                "index": "0",
                "parameters": [
                    {
                        "type": "action",
                        "action": {
                            "flow_token": flow_token
                        }
                    }
                ]
            }
        ]
    }
}

response = requests.post(url, headers=headers, json=data)
print("Status Code:", response.status_code)
print("Response Body:", response.json() if "application/json" in response.headers.get("content-type","") else response.text)
