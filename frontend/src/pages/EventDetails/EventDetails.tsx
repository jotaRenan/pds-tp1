import { Button, Grid, MenuItem, Select, TextField } from "@mui/material";
import Common from "common";
import EventsTable from "common/components/EventsTable";
import PageTitle from "common/components/PageTitle";
import PleaseWait from "common/components/PleaseWait";
import { useEffect, useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { saveBet } from "services/bet";
import { getEventById } from "services/event";
import Event from "types/Event";
import EventTitle from "./components/EventTitle";

interface EventDetailsProps {
  bet?: boolean;
}

export default function EventDetails({ bet }: EventDetailsProps) {
  const { id } = useParams();
  const navigate = useNavigate();

  const [event, setEvent] = useState<Event>();
  const [result, setResult] = useState("0");
  const [amount, setAmount] = useState("");

  useEffect(() => {
    async function fetchEvent() {
      if (!id) {
        navigate("/404");
        return;
      }
      const event = await getEventById(id);
      if (!event) {
        navigate("/404");
        return;
      }
      setEvent(event);
    }
    fetchEvent();
  }, [id, navigate]);

  const title = useMemo(() => {
    const base = bet ? "Apostar no Evento" : "Detalhes do Evento";
    if (!event) return base;
    return `${base} - ${event.home_team.name} x ${event.away_team.name}`;
  }, [bet, event]);

  async function onClickSaveBet() {
    if (event && event.id && result && amount) {
      const success = await saveBet(event.id, Number(amount), Number(amount));
      if (success) {
        navigate("/");
      }
      navigate("/"); // TODO: remover
    }
  }

  return (
    <Common>
      <>
        <PageTitle text={title} backButtonUrl="/" />
        {event ? (
          <>
            <Grid container>
              <Grid item xs={12}>
                <EventTitle label="Descrição" value={event.description} />
              </Grid>
              <Grid item xs={6}>
                <EventTitle label="Local" value={event.location} />
              </Grid>
              <Grid item xs={6}>
                <EventTitle label="Início" value={event.start} />
              </Grid>
              <Grid item xs={6}>
                <EventTitle label="Mandante" value={event.home_team.name} />
              </Grid>
              <Grid item xs={6}>
                <EventTitle label="Visitante" value={event.away_team.name} />
              </Grid>
            </Grid>
            <Grid item xs={12}>
              <EventTitle
                label="ODDS (mandante, empate e visitante)"
                value=""
              />
            </Grid>
            <EventsTable events={[event]} />
            {bet && (
              <Grid sx={{ marginTop: "20px" }} container>
                <Grid item xs={6}>
                  <Select
                    fullWidth
                    value={result}
                    label="dasdas"
                    onChange={(e) => setResult(e.target.value)}
                  >
                    <MenuItem value="1">Vitória do Mandante</MenuItem>
                    <MenuItem value="2">Empate</MenuItem>
                    <MenuItem value="3">Vitória do Visitante</MenuItem>
                  </Select>
                </Grid>
                <Grid item xs={6}>
                  <TextField
                    label="Valor da Aposta"
                    type="number"
                    fullWidth
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                  />
                </Grid>
                <Grid item xs={12} sx={{ marginTop: "20px" }}>
                  <Button
                    fullWidth
                    variant="contained"
                    size="large"
                    onClick={onClickSaveBet}
                  >
                    Betar!
                  </Button>
                </Grid>
              </Grid>
            )}
          </>
        ) : (
          <PleaseWait />
        )}
      </>
    </Common>
  );
}

EventDetails.defaultProps = {
  bet: false,
};
