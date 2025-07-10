<script lang="ts">

  interface Message {
    role: 'user' | 'assistant';
    content: string;
  }

  let messages: Message[] = [];
  let input = '';

  async function sendMessage() {
    if (!input.trim()) return;
    const userMessage: Message = { role: 'user', content: input };
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
        content: data.response
      };
      messages = [...messages, assistantMessage];
    } else {
      messages = [...messages, { role: 'assistant', content: 'Error contacting server' }];
    }
  }
</script>

<div class="flex flex-col h-full">
  <div class="flex-1 overflow-y-auto p-4 space-y-2">
    {#each messages as msg}
      <div class="p-2 rounded-md" class:ml-auto={msg.role === 'user'} class:bg-blue-100={msg.role === 'user'} class:bg-gray-100={msg.role === 'assistant'}>
        {msg.content}
      </div>
    {/each}
  </div>
  <form class="flex p-4 gap-2" on:submit|preventDefault={sendMessage}>
    <input class="border flex-1 p-2 rounded" bind:value={input} placeholder="Type a message" />
    <button class="bg-blue-500 text-white px-4 py-2 rounded" type="submit">Send</button>
  </form>
</div>

