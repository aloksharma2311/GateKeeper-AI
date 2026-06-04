from pathlib import Path

from app.core.supabase import supabase


class StorageService:

    @staticmethod
    def download_scan(
        file_path: str
    ) -> str:

        data = (
            supabase.storage
            .from_("scan-uploads")
            .download(file_path)
        )

        downloads = Path(
            "downloads"
        )

        downloads.mkdir(
            exist_ok=True
        )

        local_file = (
            downloads /
            Path(file_path).name
        )

        with open(
            local_file,
            "wb"
        ) as f:
            f.write(data)

        return str(local_file)