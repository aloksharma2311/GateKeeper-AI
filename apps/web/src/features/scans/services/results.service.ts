export class ResultsService {
  static async getResult(
    scanId: string
  ) {
    const response =
      await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/api/v1/results/${scanId}`,
        {
          cache: "no-store",
        }
      );

    if (!response.ok) {
      throw new Error(
        "Failed to fetch results"
      );
    }

    return response.json();
  }
}