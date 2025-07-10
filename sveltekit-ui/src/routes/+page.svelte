<script lang="ts">
  import Chat from '$lib/Chat.svelte';
</script>

<div class="flex flex-col h-screen bg-gradient-to-b from-slate-50 via-slate-100 to-slate-200">
  <header class="p-4 bg-gray-800 text-white text-lg">Codex Chat</header>
  <Chat class="flex-1" />
</div>
