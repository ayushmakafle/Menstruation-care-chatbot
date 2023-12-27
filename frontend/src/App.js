// App.jsx

import React, { useState } from 'react';
import ChatWindow from '../src/components/ChatWindow';
import ChatInput from '../src/components/ChatInput';
import './App.css';


const App = () => {
  const [messages, setMessages] = useState([
    { content: 'Welcome! Type your message here.', sender: 'bot' },
  ]);

  const handleSendMessage = async (message) => {
    try {
      const response = await fetch('http://localhost:5000/api/send-message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();

      // Modify the response message to exclude the bot name
      const modifiedResponse = data.response.replace('EaseFlow girly:', '');

      setMessages([
        ...messages,
        { content: message, sender: 'user' },
        { content: modifiedResponse, sender: 'bot' },
      ]);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="app">
      <h1>Chatbot App</h1>
      <ChatWindow messages={messages} />
      <ChatInput onSendMessage={handleSendMessage} />
    </div>
  );
};

export default App;