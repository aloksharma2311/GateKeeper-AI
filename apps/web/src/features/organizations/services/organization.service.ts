import { OrganizationRepository } from "../repositories/organization.repository";

export class OrganizationService {
  static async ensurePersonalWorkspace(
    userId: string,
    email: string
  ) {
    const existing =
      await OrganizationRepository.findByOwner(
        userId
      );

    if (existing) {
      return existing;
    }

    const username =
      email.split("@")[0];

    const slug =
      `${username}-workspace`;

    return OrganizationRepository.create(
      `${username} Workspace`,
      slug,
      userId
    );
  }
}