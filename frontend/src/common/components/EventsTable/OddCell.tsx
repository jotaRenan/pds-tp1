import { TableCell, Tooltip } from "@mui/material";
import { useMemo } from "react";

interface BetCellProps {
  value?: number;
}

export default function BetCell({ value }: BetCellProps) {
  const tooltipMessage = useMemo(
    () =>
      value === 0
        ? "Ainda não há apostas nesse resultado, por isso a ODD ainda não foi calculada 😉"
        : "",
    [value]
  );

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
    <TableCell align="right">
      {tooltipMessage ? (
        <Tooltip title={tooltipMessage} placement="top">
          <span>{oddValue(value)}</span>
        </Tooltip>
      ) : (
        <span>{oddValue(value)}</span>
      )}
    </TableCell>
  );
}
