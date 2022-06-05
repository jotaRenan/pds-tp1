import { Button, TextareaAutosize, TextField, Typography } from "@mui/material";
import Common from "common";
import { NewEvent } from "types/NewEvent";
import React, { useState } from "react";
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import PageTitle from "common/components/PageTitle";
import { createEvent } from "services/event";
import { useNavigate } from "react-router-dom";

export default function NewEventPage() {
  const navigate = useNavigate();
  const [awayTeam, setAwayTeam] = useState('');
  const [homeTeam, setHomeTeam] = useState('');
  const [start, setStart] = useState<Date | null>(new Date());
  const [description, setDescription] = useState<string>('');
  const [location, setLocation] = useState('');
  const [isLoading, setIsLoading] = useState(false);


  const sendEvent = async () => {
    const newEvent: NewEvent = {
      away_team: awayTeam,
      home_team: homeTeam,
      start: start?.toISOString() ?? '',
      location,
      description
    }
    try {
      setIsLoading(true);
      await createEvent(newEvent);
      alert('evento criado com sucesso');
      navigate('/eventos/');
    } catch (e) {
      alert('erro ao cadastrar evento')
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <Common>
      <>
        <PageTitle text="Cadastrar Evento" />
        <Typography>Insira os dados do evento a ser criado nos campos abaixo.</Typography>
        <form onSubmit={(e) => {sendEvent(); e.preventDefault()}} style={{ marginBottom: 48, display: 'grid', gridTemplateColumns: 'repeat(2, 1fr', gap: 24 }}>
          <TextField style={{ gridColumn: '1 / -1' }} placeholder="Descrição" onChange={(e: any) => setDescription(e.target.value)}  required/>
          <TextField label="Time A" value={homeTeam} onChange={(e) =>setHomeTeam(e.target.value)} required/>
          <TextField label="Time B" value={awayTeam} onChange={(e) =>setAwayTeam(e.target.value)} required/>
          <TextField label="Localização" value={location} onChange={(e) => setLocation(e.target.value)} required/>
          <DateTimePicker
            label="Horário"
            value={start}
            renderInput={(params: any) => <TextField {...params} />}
            onChange={(newValue: Date | null) => setStart(newValue)}
          />
        <Button type="submit" disabled={isLoading} style={{gridColumn: 2}} variant="contained">{isLoading ? 'Carregando...' : 'Criar evento'}</Button>
        </form>
      </>
    </Common>
  );
}