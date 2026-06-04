type Props = {
  scan: {
    id: string;
    scan_type: string;
    status: string;
    file_name: string | null;
    created_at: string;
  };
};

export function ScanCard({
  scan,
}: Props) {
  return (
    <div className="rounded-lg border p-4">
      <h3 className="font-semibold">
        {scan.file_name ??
          "Unnamed File"}
      </h3>

      <p className="text-sm text-gray-500">
        Type:
        {" "}
        {scan.scan_type}
      </p>

      <p className="text-sm text-gray-500">
        Status:
        {" "}
        {scan.status}
      </p>

      <p className="text-sm text-gray-500">
        {new Date(
          scan.created_at
        ).toLocaleString()}
      </p>
    </div>
  );
}