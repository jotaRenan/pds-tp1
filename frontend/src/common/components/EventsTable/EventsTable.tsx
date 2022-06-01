import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Button } from "@mui/material";
import Event from "types/Event";
import { useNavigate } from "react-router-dom";
import { useEvent } from "hooks/useEvent";
import { useEffect, useMemo } from "react";
import BetCell from "./OddCell";

interface EventsTableProps {
  eventId?: string;
  bet?: boolean;
  clickable?: boolean;
}

export default function EventsTable({
  eventId,
  bet,
  clickable,
}: EventsTableProps) {
  const { events, fetchEvents } = useEvent();
  const navigate = useNavigate();

  const eventsFiltered = useMemo(() => {
	if (!eventId) {
		return events;
	}
	return events.filter(event => event.event_id === eventId);
  }, [events, eventId])

  useEffect(() => {
    fetchEvents();
  }, []);

  function oddValue(value?: number) {
    if (value === undefined) {
      return "-";
    }
    if (value === 0) {
      return "N/A";
    }
    return value.toFixed(2);
  }

  return (
    <TableContainer component={Paper} sx={{ maxHeight: "75%" }}>
      <Table sx={{ height: "100%" }}>
        <TableHead>
          <TableRow>
            <TableCell></TableCell>
            <TableCell align="right">1</TableCell>
            <TableCell align="right">X</TableCell>
            <TableCell align="right">2</TableCell>
            {bet && <TableCell align="right" width="15%"></TableCell>}
          </TableRow>
        </TableHead>
        <TableBody>
          {eventsFiltered.map((event) => (
            <TableRow
              hover
              key={JSON.stringify(event)}
              sx={{
                "&:last-child td, &:last-child th": { border: 0 },
                cursor: "pointer",
              }}
              onClick={() =>
                clickable && navigate(`/eventos/${event.event_id}`)
              }
            >
              <TableCell component="th" scope="row">
                {event.home_team.name} x {event.away_team.name}
              </TableCell>
			  <BetCell value={event.odd?.home}/>
			  <BetCell value={event.odd?.draw}/>
			  <BetCell value={event.odd?.away}/>
              {bet && (
                <TableCell align="right">
                  <Button
                    variant="contained"
                    onClick={(e) => {
                      e.stopPropagation();
                      navigate(`/apostar/${event.event_id}`);
                    }}
                  >
                    Apostar
                  </Button>
                </TableCell>
              )}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

EventsTable.defaultProps = {
  eventId: "",
  bet: false,
  clickable: false,
};
