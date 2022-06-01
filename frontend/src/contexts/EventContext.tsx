import { createContext, ReactNode, useState } from "react";
import { getEvents } from "services/event";
import Event from "types/Event";

interface IEventContext {
  events: Event[];
  fetchEvents: () => void;
}

export const EventContext = createContext<IEventContext>({} as IEventContext);

export default function EventsProvider({ children }: { children: ReactNode }) {
  const [events, setEvents] = useState<Event[]>([]);

  async function fetchEvents() {
	  const events = await getEvents();
	  setEvents(events);
  }

  return (
    <EventContext.Provider value={{ events, fetchEvents }}>
      {children}
    </EventContext.Provider>
  );
}
