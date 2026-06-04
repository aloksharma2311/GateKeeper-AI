export class InvestigationService {

  static async getInvestigation(
    scanId: string
  ) {

    console.log(
      "SCAN ID:",
      scanId
    );

    const response =
      await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/api/v1/results/${scanId}`,
        {
          cache: "no-store",
        }
      );

    return response.json();
  }
}