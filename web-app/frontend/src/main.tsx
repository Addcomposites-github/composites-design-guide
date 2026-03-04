import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App";

const rootElement = document.getElementById("root");

if (!rootElement) {
  throw new Error(
    "Root element not found. Ensure there is a <div id='root'></div> in index.html."
  );
}

createRoot(rootElement).render(
  <StrictMode>
    <App />
  </StrictMode>
);
