# SvelteKit UI

Frontend interface for the Codex Assistant. This project uses SvelteKit and enhanced Tailwind CSS.

## Features

- Simple chat panel that sends messages to the MCP backend defined by `VITE_BACKEND_URL`.
- Enhanced Tailwind styling for a cleaner interface.

The chat layout now uses bubble-style messages with alternating colors for user
and assistant responses, providing clearer visual separation.
- Simple chat panel that sends messages to the MCP backend at `http://localhost:8000/chat`.
- Tailwind styling for quick prototyping.
- Styled chat bubbles with timestamps and fade-in animations.
- Automatic scrolling to the latest message.
- Soft gradient background for the main page.
- Global styles from `src/app.css` are imported in `src/routes/+layout.svelte`.

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npx sv create

# create a new project in my-app
npx sv create my-app
```

Set `VITE_BACKEND_URL` in a `.env` file to control which MCP server the UI uses. Example:

```bash
VITE_BACKEND_URL=http://localhost:8000
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.
