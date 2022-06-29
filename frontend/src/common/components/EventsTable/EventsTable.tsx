import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Button } from "@mui/material";
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
  }, []); // TODO: fix useEffect warning.

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
          {eventsFiltered.map((event, i) => (
            <TableRow
              hover
              key={JSON.stringify(event)}
              sx={{
                "&:last-child td, &:last-child th": { border: 0 },
                cursor: clickable ? "pointer" : "default",
              }}
              onClick={() =>
                clickable && navigate(`/eventos/${event.event_id}`)
              }
            >
              <TableCell component="th" scope="row">
                {event.home_team.name} x {event.away_team.name}
              </TableCell>
              <BetCell value={event.odd?.home} data-testid={`home-odd-${i+1}`} />
              <BetCell value={event.odd?.draw} data-testid={`draw-odd-${i+1}`} />
              <BetCell value={event.odd?.away} data-testid={`away-odd-${i+1}`} />
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
