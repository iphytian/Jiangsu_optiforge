// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';
import react from '@astrojs/react';

// https://astro.build/config
const base = process.env.SITE_BASE || '/';

export default defineConfig({
  site: 'https://iphytian.github.io',
  base,
  compressHTML: true,
  build: {
    inlineStylesheets: 'always',
    assetsInlineLimit: 10240, // 10KB to inline achievements.css (7.5KB)
  },
  vite: {
    plugins: [tailwindcss()],
    build: {
      assetsInlineLimit: 10240,
    }
  },

  integrations: [react()]
});
