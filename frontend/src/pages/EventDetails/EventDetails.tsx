import {
  Button,
  Grid,
  InputAdornment,
  MenuItem,
  TextField,
} from "@mui/material";
import Common from "common";
import EventsTable from "common/components/EventsTable";
import PageTitle from "common/components/PageTitle";
import PleaseWait from "common/components/PleaseWait";
import { useAlert } from "hooks/useAlert";
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
  const { showAlert } = useAlert();

  const [event, setEvent] = useState<Event>();
  const [result, setResult] = useState("");
  const [amount, setAmount] = useState("");
  const [requesting, setRequesting] = useState(false);

  useEffect(() => {
    async function fetchEvent() {
      if (!id) {
        navigate("/404");
        return;
      }
      setRequesting(true);
      const event = await getEventById(id);
      if (!event) {
        navigate("/404");
        return;
      }
      setRequesting(false);
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
    if (event && event.event_id && result && amount) {
      setRequesting(true);
      const success = await saveBet(
        event.event_id,
        Number(amount),
        Number(result)
      );
      setRequesting(false);
      if (success) {
        navigate("/");
        showAlert({
          type: "success",
          message: "Aposta realizada com sucesso!",
        });
      } else {
        showAlert({
          type: "error",
          message:
            "Ocorreu um erro ao salvar a aposta. Por favor, tente novamente.",
        });
      }
    } else {
      showAlert({
        type: "warning",
        message: "Preencha todos os campos para realizar a aposta!",
      });
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
                <EventTitle
                  label="Início"
                  value={new Date(event.start).toLocaleString("pt-BR", {
                    day: "2-digit",
                    month: "2-digit",
                    year: "numeric",
                    hour: "2-digit",
                    minute: "2-digit",
                  })}
                />
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
                label="ODDs (mandante, empate e visitante)"
                value=""
              />
            </Grid>
            <EventsTable eventId={id} />
            {bet && (
              <Grid sx={{ marginTop: "20px" }} container>
                <Grid item xs={6}>
                  <TextField
                    id="result"
                    fullWidth
                    value={result}
                    onChange={(e) => setResult(e.target.value)}
                    select
                    label="Palpite"
                  >
                    <MenuItem value="1">Vitória do Mandante</MenuItem>
                    <MenuItem value="2">Empate</MenuItem>
                    <MenuItem value="3">Vitória do Visitante</MenuItem>
                  </TextField>
                </Grid>
                <Grid item xs={6}>
                  <TextField
                    label="Valor da Aposta"
                    type="number"
                    inputProps={{
                      step: "0.01",
                      min: "0.01",
                      lang: "pt-BR",
                    }}
                    InputProps={{
                      startAdornment: (
                        <InputAdornment position="start">
                          <span>R$</span>
                        </InputAdornment>
                      ),
                    }}
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
                    disabled={requesting}
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
