import { AlertContext } from "contexts/AlertContext";
import { useContext } from "react";

export function useAlert() {
	const context = useContext(AlertContext);
	return context;
}