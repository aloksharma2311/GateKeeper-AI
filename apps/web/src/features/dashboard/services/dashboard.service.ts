export class DashboardService {

  static async getStats() {

    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/api/v1/dashboard`,
      {
        cache: "no-store",

        headers: {
          "organization-id":
            process.env.NEXT_PUBLIC_ORGANIZATION_ID!
        }
      }
    );

    if (!response.ok) {

      const error =
        await response.text();

      console.error(error);

      throw new Error(
        "Failed to fetch dashboard stats"
      );
    }

    return response.json();
  }
}