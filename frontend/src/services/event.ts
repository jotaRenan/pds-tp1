import Event from "types/Event";

import api from "./api";
import { getOddsFromEvent } from "./odd";

export async function getEvents() {
  let events: Event[] = [];

  try {
    const response = await api.get("/events/");
    if (response.status === 200) {
      events = response.data;
    }
  } catch (e) {
    // TODO: handle error properly
    console.log(e);
  }

  // Código deselegante
  const promises = events.map(
    async (event) => await getOddsFromEvent(event.event_id)
  );
  const results = await Promise.allSettled(promises);

  // TODO: use Array.prototype.map
  results.forEach((result, index) => {
    if (result.status === "fulfilled") {
      events[index].odd = result.value;
    }
  });
  // Código deselegante

  return events;
}

export async function getEventById(id: string) {
  try {
    const response = await api.get(`/events/${id}/`);
    if (response.status === 200) {
      return response.data;
    }
  } catch (e) {
    // TODO: handle error properly
    console.log(e);
  }

}
