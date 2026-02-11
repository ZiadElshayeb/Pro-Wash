from pydantic import BaseModel

class SendMessageRequest(BaseModel):
    to: str
    template_name: str = "pro_wash_v3"
    language_code: str = "ar"
    consumption_id: str = "unused"