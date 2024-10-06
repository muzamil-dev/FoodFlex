import React, { useState } from 'react';
import axios from 'axios';
import '../styles/chatBot.css';

const ChatBot = () => {
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hello! How would you like to customize your recipe today?' }
  ]);
  const [userMessage, setUserMessage] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async (message) => {
    const newMessages = [...messages, { sender: 'user', text: message }];
    setMessages(newMessages);
    setLoading(true);
  
    try {
      // Check if userId is available
      const userId = localStorage.getItem('userId');
      if (!userId) {
        throw new Error('User ID not found. Please login again.');
      }
  
      // Send user message to backend API
      const response = await axios.post('http://localhost:8000/chatbot/chat_with_ai/', {
        message: userMessage,
        userId: userId
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
  
      // Append the chatbot's response to the chat
      const botResponse = response.data.reply;
      setMessages([...newMessages, { sender: 'bot', text: botResponse }]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages([...newMessages, { sender: 'bot', text: 'Sorry, there was an error.' }]);
    } finally {
      setLoading(false);
    }
  };  
  

  const handleSubmit = (e) => {
    e.preventDefault();
    if (userMessage.trim() !== '') {
      sendMessage(userMessage);
      setUserMessage('');
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={`chat-message ${msg.sender}`}>
            <p>{msg.text}</p>
          </div>
        ))}
        {loading && <div className="chat-message bot">Thinking...</div>}
      </div>
      <form onSubmit={handleSubmit} className="chat-form">
        <input
          type="text"
          placeholder="Type a message..."
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default ChatBot;
