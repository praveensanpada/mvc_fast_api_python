# === main.py ===
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.mongo_hub_routes import router as mongo_hub_routes
from routes.mongo_routes import router as mongo_router
from routes.mysql_routes import router as mysql_routes
import uvicorn
from config.settings import PORT

app = FastAPI(title="Cric DataHub Mongo API")

app.include_router(mongo_hub_routes, prefix="/mongo_hub", tags=["MongoHub"])
app.include_router(mongo_router, prefix="/mongo", tags=["Mongo"])
app.include_router(mysql_routes, prefix="/mysql", tags=["Mysql"])

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Cric DataHub Status</title>
        </head>
        <body style='font-family:Arial, sans-serif;'>
            <h1>🏏 Cric DataHub is running!</h1>
            <p>Server URL: <code>http://0.0.0.0:8088/</code></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)