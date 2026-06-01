from app.repositories.scan_repository import ScanRepository
from app.repositories.ocr_result_repository import OCRResultRepository
from app.services.storage_service import StorageService
from app.services.ocr_service import OCRService


class ScanProcessorService:

    @staticmethod
    def process(scan_id: str):

        scan = ScanRepository.get_by_id(
            scan_id
        )

        if not scan:
            raise Exception(
                "Scan not found"
            )

        if not scan.get(
            "file_path"
        ):
            raise Exception(
                "Scan has no file"
            )

        ScanRepository.update_status(
            scan_id,
            "processing"
        )

        local_file = (
            StorageService.download_scan(
                scan["file_path"]
            )
        )

        extracted_text = (
            OCRService.extract_text(
                local_file
            )
        )

        OCRResultRepository.create(
            scan_id,
            extracted_text
        )

        ScanRepository.update_status(
            scan_id,
            "completed"
        )

        return {
            "scan_id": scan_id,
            "text": extracted_text,
        }