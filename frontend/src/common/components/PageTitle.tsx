import { Typography, Divider, Grid } from "@mui/material";
import BackButton from "./BackButton";

interface PageTitleProps {
  text: string;
  backButtonUrl?: string;
}

export default function PageTitle({ text, backButtonUrl }: PageTitleProps) {
  return (
    <Grid sx={{ marginBottom: "40px", marginTop: "40px" }}>
      <Typography variant="h5" align="left" color="primary">
        {backButtonUrl && <BackButton data-testid="back-button" href={backButtonUrl} />}
        {text}
      </Typography>
      <Divider variant="fullWidth" />
    </Grid>
  );
}
