import "./App.css";
import { useState } from "react";
import Header from "./components/Header";
import InteractionForm from "./components/InteractionForm";
import ChatPanel from "./components/ChatPanel";

function App() {

  const [interaction, setInteraction] = useState({
    hcpName: "",
    date: "",
    product: "",
    sentiment: "",
    brochure: false,
    followup: false,
    summary: ""
  });

  return (
<div className="app">

    <Header/>

    <div className="container">

        <div className="card">
            <InteractionForm interaction={interaction}/>
        </div>

        <div className="card">
            {/* <ChatPanel setInteraction={setInteraction}/> */}
            <ChatPanel
    interaction={interaction}
    setInteraction={setInteraction}
/>
        </div>

    </div>

</div>
    
  );
}

export default App;