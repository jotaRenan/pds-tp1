import Common from "common";
import EventsTable from "common/components/EventsTable";
import PageTitle from "common/components/PageTitle";

export default function Home() {
  return (
    <Common>
      <>
        <PageTitle text="Eventos em Andamento" />
        <EventsTable bet clickable />
      </>
    </Common>
  );
}
