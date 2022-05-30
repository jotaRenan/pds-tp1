import {
  Grid,
  Typography,
  Button,
  Toolbar,
  Link,
  Divider,
} from "@mui/material";
import { Container } from "@mui/system";
import { useNavigate } from "react-router-dom";

export default function Header() {
  const navigation = useNavigate();

  return (
    <>
      <Container sx={{ height: "10%" }}>
        <Toolbar
          component="nav"
          sx={{
            justifyContent: "center",
            alignItems: "center",
            height: "100%",
          }}
        >
          <Link href="/" variant="h4" sx={{ flex: 1 }}>
            {"BETinho"}
          </Link>
          <Button
            variant="outlined"
            size="large"
            onClick={() => navigation("/criar-conta")}
          >
            Criar Conta
          </Button>
          <Button size="large" onClick={() => navigation("/entrar")}>
            Entrar
          </Button>
        </Toolbar>
      </Container>
      <Divider variant="fullWidth" />
    </>
  );
}
