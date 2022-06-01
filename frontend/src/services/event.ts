import Event from "types/Event";

import api from "./api";
import { getOddsFromEvent } from "./odd";

const eventsMock: Event[] = [
  {
    event_id: "0036e757dd9c40eebae807f13f8f5236",
    description: "Jogo de ida das oitavas de final da Copa do Brasil 2022",
    home_team: { id: "0", name: "Cruzeiro" },
    away_team: { id: "1", name: "Atlético" },
    location: "Mineirão",
    result: { away: 10, draw: 1, home: 1 },
    start: "?",
  },
  {
    event_id: "0036e757dd9c40eebae807f13f8f5236",
    description: "Jogo de ida das oitavas de final da Copa do Brasil 2022",
    home_team: { id: "0", name: "Cruzeiro" },
    away_team: { id: "1", name: "Atlético" },
    location: "Mineirão",
    result: { away: 10, draw: 1, home: 1 },
    start: "?",
  },
];

export async function getEvents() {
  let events: Event[] = [];

  try {
    const response = await api.get("/events/");
    if (response.status === 200) {
      events = response.data;
    }
  } catch (e) {
    console.log(e);
  }

  // Código deselegante
  const promises = events.map(
    async (event) => await getOddsFromEvent(event.event_id)
  );
  const results = await Promise.allSettled(promises);

  results.forEach((result, index) => {
    if (result.status === "fulfilled") {
      events[index].odd = result.value;
    }
  });
  // Código deselegante

  return events;
}

export async function getEventById(id: string) {
  let event: Event;

  try {
    const response = await api.get(`/events/${id}/`); // TODO: check
    if (response.status === 200) {
      event = response.data;
    }
  } catch (e) {
    console.log(e);
  }

  event = eventsMock[0]; // TODO: remove

  return event;
}
