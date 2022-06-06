import { Button, Toolbar, Link, Divider, Grid } from "@mui/material";
import { Box, Container } from "@mui/system";
import { useNavigate } from "react-router-dom";

import logo from "assets/logo.png";

export default function Header() {
  const navigation = useNavigate();

  return (
    <Container sx={{ height: "10%", marginTop: "10px" }}>
      <Box sx={{ display: "flex", marginBottom: "10px" }}>
        <Box sx={{ width: "100%", display: "flex", alignItems: "center" }}>
          <img
            src={logo}
            alt="BETinho"
            style={{ width: "5%", minWidth: "40px" }}
          />
          <Link href="/" variant="h4" sx={{ marginLeft: "10px" }}>
            {"BETinho"}
          </Link>
        </Box>
        <Box sx={{ flexShrink: 1, display: "flex" }}>
          <Box sx={{height: "100%"}}>
            <Button
              variant="outlined"
              size="medium"
              onClick={() => navigation("/criar-conta")}
            >
              Criar Conta
            </Button>
          </Box>
          <Box sx={{justifyContent: "center" }}>
            <Button
              sx={{ order: 1, height: "100%" }}
              size="medium"
              onClick={() => navigation("/entrar")}
            >
              Entrar
            </Button>
          </Box>
        </Box>
      </Box>
      <Divider variant="fullWidth" />
    </Container>
  );
}
