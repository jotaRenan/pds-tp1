import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { IconButton } from "@mui/material";
import { useNavigate } from "react-router-dom";

interface BackButtonProps {
  href: string;
}

export default function BackButton({ href }: BackButtonProps) {
  const navigate = useNavigate();

  return (
    <IconButton
      color="primary"
      aria-label="voltar"
      onClick={() => navigate(href)}
    >
      <ArrowBackIcon fontSize="large" />
    </IconButton>
  );
}
