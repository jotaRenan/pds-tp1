import Common from "common";
import EventsTable from "common/components/EventsTable";
import PageTitle from "common/components/PageTitle";
import PleaseWait from "common/components/PleaseWait";
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
      <>
        <PageTitle text="Eventos em Andamento" />
        {events.length > 0 ? (
          <EventsTable events={events} bet clickable />
        ) : (
          <PleaseWait />
        )}
      </>
    </Common>
  );
}
