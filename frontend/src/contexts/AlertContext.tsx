import SystemAlert from "common/components/SystemAlert";
import { createContext, ReactNode, useState } from "react";
import Alert from "types/Alert";

interface IAlertContext {
  alert?: Alert;
  showAlert: (alert: Alert) => void;
}

export const AlertContext = createContext<IAlertContext>({} as IAlertContext);

export default function AlertProvider({ children }: { children: ReactNode }) {
  const [alert, setAlert] = useState<Alert>();

  function showAlert(alert: Alert) {
    setAlert(alert);
  }

  return (
    <AlertContext.Provider value={{ showAlert, alert }}>
      <>
        <SystemAlert />
        {children}
      </>
    </AlertContext.Provider>
  );
}
