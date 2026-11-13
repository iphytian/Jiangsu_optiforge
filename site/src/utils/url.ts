const base = import.meta.env.BASE_URL.replace(/\/$/, '');

/** Prefix a site-internal path with the configured Astro base path. */
export function withBase(path: string): string {
  const p = path.startsWith('/') ? path : `/${path}`;
  return `${base}${p}` || '/';
}
