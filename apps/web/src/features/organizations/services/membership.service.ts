import { MembershipRepository } from "../repositories/membership.repository";

export class MembershipService {
  static async ensureOwnerMembership(organizationId: string, userId: string) {
    const existing = await MembershipRepository.findMembership(
      organizationId,
      userId,
    );

    if (existing) {
      return existing;
    }

    return await MembershipRepository.createOwnerMembership(
      organizationId,
      userId,
    );
  }
}
