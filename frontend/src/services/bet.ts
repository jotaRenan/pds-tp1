import api from "./api";

export async function saveBet(eventId: string, amount: number, result: number) {
  let success = false;

  try {
    const response = await api.post(`/events/${eventId}/bets/`, {
      amount,
      result,
    });
    if (response.status === 204) { // TODO: Mudar pra 200
      success = true;
    }
  } catch (e) {
    console.log(e);
  }

  return success;
}
