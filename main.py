from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - project0001-coll-d4f1137feb854dc6a58575546a17acbf',debug=False,docs_url='/trusting-lichterman-df914912c90511ef9f5b0242ac1200056/docs',openapi_url='/trusting-lichterman-df914912c90511ef9f5b0242ac1200056/openapi.json')

app.include_router(router, prefix='/trusting-lichterman-df914912c90511ef9f5b0242ac1200056/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()