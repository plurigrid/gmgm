```python
from fastapi import FastAPI
from app.routers import bot

app = FastAPI()

app.include_router(bot.router)
```