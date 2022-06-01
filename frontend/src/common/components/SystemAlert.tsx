import { useEffect, useState, forwardRef } from "react";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert, { AlertProps } from "@mui/material/Alert";
import { useAlert } from "hooks/useAlert";

const MyAlert = forwardRef<HTMLDivElement, AlertProps>(function Alert(
  props,
  ref
) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

export default function SystemAlert() {
  const [open, setOpen] = useState(false);
  const { alert } = useAlert();

  useEffect(() => {
    if (alert === undefined) return;
    setOpen(true);
  }, [alert]);

  const handleClose = (
    event?: React.SyntheticEvent | Event,
    reason?: string
  ) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  return (
    <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
      <MyAlert
        onClose={handleClose}
        severity={alert?.type}
        sx={{ width: "100%" }}
      >
        {alert?.message}
      </MyAlert>
    </Snackbar>
  );
}
