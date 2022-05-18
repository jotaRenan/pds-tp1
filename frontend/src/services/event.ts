import Event from "types/Event";
import api from "./api";

export async function getEvents() {
	let events: Event[] = [];

	try {
		const response = await api('/getEvents');
		if (response.status === 200) {
			events = await response.json();
		}
	} catch (e) {
		console.log(e);
	}

	return events;
}