import { useState } from "react";
import axios from "axios";

function ChatPanel({ interaction, setInteraction }) {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const [chatHistory, setChatHistory] = useState([
    {
      sender: "AI",
      text: "Hello! Tell me about your HCP interaction.",
    },
  ]);

  const handleSend = async () => {
    if (!message.trim()) return;

    const userMessage = message;

    setChatHistory((prev) => [
      ...prev,
      {
        sender: "You",
        text: userMessage,
      },
    ]);

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          message: userMessage,
        }
      );

      console.log(response.data);

      // Update form only for log/edit
      if (response.data.tool === "log" || response.data.tool === "edit") {
        setInteraction({
          ...interaction,
          ...response.data,
        });
      }

      let aiMessage = "";

      switch (response.data.tool) {
        case "log":
          aiMessage = "🟢 Interaction Logged Successfully";
          break;

        case "edit":
          aiMessage = "✏️ Interaction Updated Successfully";
          break;

        case "search":
          aiMessage = response.data.message;
          break;

        case "followup":
          aiMessage = response.data.message;
          break;

        case "summary":
          aiMessage = response.data.message;
          break;

        default:
          aiMessage = "✅ Done";
      }

      setChatHistory((prev) => [
        ...prev,
        {
          sender: "AI",
          text: aiMessage,
        },
      ]);

      setMessage("");

    } catch (error) {
      console.error(error);
      alert("Unable to connect to AI Backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Assistant</h2>

      <div
        style={{
          height: "300px",
          overflowY: "auto",
          border: "1px solid #ddd",
          padding: "10px",
          borderRadius: "8px",
          marginBottom: "15px",
          background: "#fafafa",
        }}
      >
        {chatHistory.map((chat, index) => (
          <div key={index} style={{ marginBottom: "10px" }}>
            <strong>{chat.sender}:</strong>
            <br />
            {chat.text}
          </div>
        ))}
      </div>

      <textarea
        rows="5"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your interaction..."
        style={{
          width: "100%",
          padding: "10px",
          borderRadius: "8px",
        }}
      />

      <br />
      <br />

      <button
        onClick={handleSend}
        disabled={loading}
        style={{
          padding: "10px 20px",
          background: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: "6px",
          cursor: "pointer",
        }}
      >
        {loading ? "Thinking..." : "Send"}
      </button>
    </div>
  );
}

export default ChatPanel;