<script lang="ts">
import { sendMessage } from '../lib/api';

interface Message {
  role: 'user' | 'bot';
  text: string;
}

let messages: Message[] = [];
let userInput = '';

async function send() {
  if (!userInput) return;
  const reply = await sendMessage(userInput);
  messages = [...messages, { role: 'user', text: userInput }, { role: 'bot', text: reply }];
  userInput = '';
}
</script>

<main>
  <h1>Codex Chat</h1>
  {#each messages as msg}
    <p><strong>{msg.role}:</strong> {msg.text}</p>
  {/each}
  <input bind:value={userInput} placeholder="Type a message" />
  <button on:click={send}>Send</button>
</main>

