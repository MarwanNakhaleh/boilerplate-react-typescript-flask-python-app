import { ApiResponse } from "../types/ApiResponse";

export const sendRequest = async (url: string, options: any) => {
    const response = await fetch(url, options);
    const data = await response.json();
    if (response.status >= 400) {
        throw new Error(data.errors);
    }
    return data as ApiResponse;
}