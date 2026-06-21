from .BaseController import BaseController
from fastapi import UploadFile
class DataController(BaseController):

    def __init__(self):
        super().__self__()

    def validate_file(self , File : UploadFile):

        return True