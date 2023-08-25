```python
from fastapi import APIRouter
from app.models.message import Message
from app.models.response import Response
from ascii_art_generator import generate_ascii_art

router = APIRouter()

@router.post("/", response_model=Response)
async def respond_to_message(message: Message):
    if message.text == "!art":
        art = generate_ascii_art()
        return {"text": art}
    else:
        return {"text": "gmgm"}
```