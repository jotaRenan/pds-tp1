import { Grid, Typography, Button, Toolbar } from "@mui/material";
import { Container } from "@mui/system";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <Container>
      <Toolbar
        component="nav"
        sx={{
          borderBottom: 1,
          borderColor: "divider",
          overflowX: "auto",
        }}
      >
        <Typography
          component="h2"
          variant="h5"
          color="inherit"
          align="left"
          noWrap
          sx={{ flex: 1 }}
        >
          BETinho
        </Typography>
        <Grid>
          <Button variant="outlined" size="large">
            Eventos
          </Button>
          <Button variant="outlined" size="large">
            Criar Conta
          </Button>
          <Button variant="outlined" size="large">
            Entrar
          </Button>
        </Grid>
      </Toolbar>
    </Container>
  );
}
