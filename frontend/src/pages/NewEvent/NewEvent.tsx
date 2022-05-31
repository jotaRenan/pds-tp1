import { Button, TextField } from "@mui/material";
import Common from "common";
import Team from "types/Team";
import {NewEvent} from "types/NewEvent";
import React, { useState } from "react";
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import PageTitle from "common/components/PageTitle";

function foo(): Team {
  return {} as unknown as Team;
}

export default function NewEventPage() {

  const homeTeam: Team = foo();
  const awayTeam: Team = foo();
  const [start, setStart] = useState<Date | null>(new Date())
  const [description, setDescription] = useState<string>('');
  const location: string = '';


  const sendEvent = async () => {
    const newEvent: NewEvent = {
      away_team: awayTeam,
      home_team: homeTeam,
      start: start?.toISOString() ?? '',
      location,
      description
    }
    console.log(newEvent);
  }


  return (
    <Common>
      <>
        <PageTitle text="Cadastrar Evento" />
        <TextField label="Localização" />
        <TextField label="Descrição" onChange={(e: any) => setDescription(e.target.value)} />
        <DateTimePicker
          label="Horário"
          value={start}
          onChange={(newValue: Date | null) => {
            setStart(newValue);
          }}
          renderInput={(params: any) => <TextField {...params} />}
        />
        <Button onClick={() => sendEvent()}>Criar evento</Button>
      </>
    </Common>
  );
}
