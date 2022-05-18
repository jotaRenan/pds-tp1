import { EventContext } from "contexts/EventContext";
import { useContext } from "react";

export function useEvent() {
	const context = useContext(EventContext);
	return context;
}