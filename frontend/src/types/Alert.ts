export default interface Alert {
	type: "warning" | "error" | "success";
	message: string;
}