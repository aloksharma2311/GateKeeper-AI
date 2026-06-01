from pydantic import BaseModel


class ScanResponse(BaseModel):
    id: str
    scan_type: str
    status: str
    file_name: str | None = None
    file_path: str | None = None