from datetime import datetime
from typing import Optional, Literal

from pydantic import ConfigDict, BaseModel
import uuid

from api.enums.options import OpenaiWebFileUploadStrategyOption
from api.models.json import UploadedFileOpenaiWebInfo, UploadedFileExtraInfo


class UploadedFileInfoSchema(BaseModel):
    id: uuid.UUID
    original_filename: str
    size: int
    storage_path: Optional[str] = None
    content_type: Optional[str] = None
    upload_time: datetime
    uploader_id: int
    openai_web_info: Optional[UploadedFileOpenaiWebInfo] = None
    extra_info: Optional[UploadedFileExtraInfo] = None
    model_config = ConfigDict(from_attributes=True)


class StartUploadRequestSchema(BaseModel):
    file_name: str
    file_size: int
    width: Optional[int] = None
    height: Optional[int] = None
    mime_type: Optional[str] = None
    use_case: Literal['my_files', 'multimodal']  # Openai Web：图片使用 multimodal，其它使用 my_files


class StartUploadResponseSchema(BaseModel):
    strategy: OpenaiWebFileUploadStrategyOption
    file_max_size: int
    upload_file_info: Optional[UploadedFileInfoSchema] = None  # 为空意味着后端不暂存文件，前端直接上传到openai
