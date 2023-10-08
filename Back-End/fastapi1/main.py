from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def read_root():
    return { "Name" : "Test Fast API"}


@app.post('/uploadfile/')
async def create_upload_file(file: UploadFile):
    return { 'filename' : file.filename}
