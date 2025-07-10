<script lang="ts">

  import { afterUpdate } from 'svelte';
  import { fade } from 'svelte/transition';

  interface Message {
    role: 'user' | 'assistant';
    content: string;
    timestamp: Date;
  }

  let messages: Message[] = [];
  let input = '';
  let container: HTMLDivElement;

  afterUpdate(() => {
    if (container) {
      container.scrollTop = container.scrollHeight;
    }
  });

  async function sendMessage() {
    if (!input.trim()) return;
    const userMessage: Message = { role: 'user', content: input, timestamp: new Date() };
    messages = [...messages, userMessage];
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    });
    input = '';
    if (res.ok) {
      const data = await res.json();
      const assistantMessage: Message = {
        role: 'assistant',
        content: data.response,
        timestamp: new Date()
      };
      messages = [...messages, assistantMessage];
    } else {
      messages = [
        ...messages,
        { role: 'assistant', content: 'Error contacting server', timestamp: new Date() }
      ];
    }
  }
</script>

<div class="flex flex-col h-full">
  <div class="flex-1 overflow-y-auto p-4 space-y-2" bind:this={container}>
    {#each messages as msg}
      <div
        in:fade
        class="max-w-xs p-3 rounded-lg shadow"
        class:ml-auto={msg.role === 'user'}
        class:bg-blue-500={msg.role === 'user'}
        class:text-white={msg.role === 'user'}
        class:bg-gray-200={msg.role === 'assistant'}
      >
        <p>{msg.content}</p>
        <span class="block text-right text-xs text-gray-500 mt-1">
          {msg.timestamp.toLocaleTimeString()}
        </span>
      </div>
    {/each}
  </div>
  <form class="flex p-4 gap-2" on:submit|preventDefault={sendMessage}>
    <input class="border flex-1 p-2 rounded" bind:value={input} placeholder="Type a message" />
    <button class="bg-blue-500 text-white px-4 py-2 rounded" type="submit">Send</button>
  </form>
</div>

