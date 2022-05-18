import { createContext, ReactNode } from "react";

interface IEventContext {
  whatever: any;
}

export const EventContext = createContext<IEventContext>({} as IEventContext);

export default function EventsProvider({ children }: { children: ReactNode }) {
  return (
    <EventContext.Provider value={{ whatever: "" }}>
      {children}
    </EventContext.Provider>
  );
}
