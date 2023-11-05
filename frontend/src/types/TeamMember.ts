import { AccessType } from "./Access";

export type TeamMember = {
    id: number;
    name: string;
    email: string;
    age: number;
    phone: string;
    access: AccessType
}
