from fastapi import APIRouter , Depends , UploadFile , File
from helper import settings , get_settings
from controllers import DataController
data_Router = APIRouter(
    prefix="/Data" ,
    tags=["api","data"]
)

@data_Router.post("/upload/{Project_id}")
async def upload_file(Project_id: str, file: UploadFile = File(...) , settings : settings = Depends(get_settings)):
    return {
            "File_type" : file.content_type
        }