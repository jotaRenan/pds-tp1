import Common from "common";
import EventsTable from "common/components/EventsTable";
import { useEffect, useState } from "react";
import { getEvents } from "services/event";
import Event from "types/Event";

export default function Home() {
  const [events, setEvents] = useState<Event[]>([]);

  useEffect(() => {
    async function fetchEvents() {
      setEvents(await getEvents());
    }
    fetchEvents();
  }, []);

  return (
    <Common>
      <EventsTable events={events} bet={true} />
    </Common>
  );
}
