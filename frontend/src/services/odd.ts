import { Odd } from "types/Odd";
import api from "./api";

export async function getOddsFromEvent(eventId: string) {
  let odd: Odd | undefined;

  const response = await api.get(`/events/${eventId}/odds/`);

  if (response.status === 200) {
    odd = response.data;
  }

  return odd;
}
