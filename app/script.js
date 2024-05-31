async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    const reply = data.reply;

    const messagesDiv = document.getElementById('messages');
    const userMessage = document.createElement('div');
    userMessage.textContent = 'You: ' + userInput;
    const botMessage = document.createElement('div');
    botMessage.textContent = 'Bot: ' + reply;

    messagesDiv.appendChild(userMessage);
    messagesDiv.appendChild(botMessage);

    document.getElementById('user-input').value = '';
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Scroll to the bottom
}