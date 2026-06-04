export class ResultsService {
  static async getResult(
    scanId: string
  ) {
    const response =
      await fetch(
        `http://127.0.0.1:8000/api/v1/results/${scanId}`,
        {
          cache: "no-store",
        }
      );

    if (!response.ok) {
      throw new Error(
        "Failed to load result"
      );
    }

    return response.json();
  }
}