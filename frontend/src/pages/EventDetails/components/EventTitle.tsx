import { Grid, Typography } from "@mui/material";

interface EventTitleProps {
  label: string;
  value: string;
}

export default function EventTitle({ label, value }: EventTitleProps) {
  return (
    <Grid sx={{ marginBottom: "10px" }} container>
      <Typography variant="h6" color="primary">
        {label}:&nbsp;
      </Typography>
      <Typography variant="h6">{value}</Typography>
    </Grid>
  );
}
