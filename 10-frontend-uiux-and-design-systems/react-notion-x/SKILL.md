---
name: react-notion-x
description: Render Notion pages as a full React app or Next.js site using react-notion-x. Use when building a Notion-powered blog, portfolio, documentation site, or CMS where content is managed in Notion and rendered via the NotionAPI or unofficial notion-client.
metadata:
  author: notionx
  version: "7.2.4"
---

# react-notion-x Guide & Patterns

`react-notion-x` renders Notion pages as performant, SEO-friendly React components in Next.js, supporting all standard Notion block types.

---

## 1. Installation

```bash
# Core packages
npm install react-notion-x notion-client

# Optional renderers for extra block types
npm install prismjs react-pdf react-tweet katex
```

---

## 2. Fetching Notion Pages (Server-Side)

Always fetch Notion data server-side to avoid exposing API tokens:

```ts
// lib/notion.ts
import { NotionAPI } from "notion-client";

export const notion = new NotionAPI({
  authToken: process.env.NOTION_TOKEN, // Optional: for private pages
  activeUser: process.env.NOTION_ACTIVE_USER, // Optional
});

export async function getPage(pageId: string) {
  return notion.getPage(pageId);
}
```

---

## 3. Next.js App Router Integration

```tsx
// app/blog/[slug]/page.tsx
import { NotionRenderer } from "react-notion-x";
import { getPage } from "@/lib/notion";
import "react-notion-x/src/styles.css";
import "prismjs/themes/prism-tomorrow.css";
import "katex/dist/katex.min.css";

// Dynamic imports for heavy optional blocks
import dynamic from "next/dynamic";
const Code = dynamic(() => import("react-notion-x/build/third-party/code").then(m => m.Code));
const Equation = dynamic(() => import("react-notion-x/build/third-party/equation").then(m => m.Equation));
const Pdf = dynamic(() => import("react-notion-x/build/third-party/pdf").then(m => m.Pdf), { ssr: false });
const Tweet = dynamic(() => import("react-notion-x/build/third-party/tweet").then(m => m.Tweet), { ssr: false });

interface PageProps {
  params: { slug: string };
}

export default async function NotionPage({ params }: PageProps) {
  // Map your slug to a Notion Page ID
  const pageId = "your-notion-page-id-here"; 
  const recordMap = await getPage(pageId);

  return (
    <NotionRenderer
      recordMap={recordMap}
      fullPage={true}
      darkMode={false}
      rootPageId={pageId}
      components={{
        Code,
        Equation,
        Pdf,
        Tweet,
        // Override Next.js Link for SPA navigation
        nextLink: ({ href, children, ...rest }) => (
          <a href={href} {...rest}>{children}</a>
        ),
      }}
    />
  );
}
```

---

## 4. Notion as CMS: Dynamic Routing by Slug

```ts
// lib/notion-site.ts
import { getPage } from "./notion";

// Map human-readable slugs to Notion page IDs
export const siteConfig = {
  pages: {
    "getting-started": "abc123notionpageid",
    "about-me": "def456notionpageid",
    "projects": "ghi789notionpageid",
  }
};

// Generate static routes for all blog posts
export async function getAllPageIds(): Promise<string[]> {
  return Object.values(siteConfig.pages);
}
```

```tsx
// app/blog/[slug]/page.tsx — Static generation
export async function generateStaticParams() {
  return Object.keys(siteConfig.pages).map(slug => ({ slug }));
}

export default async function BlogPost({ params }: { params: { slug: string } }) {
  const pageId = siteConfig.pages[params.slug];
  if (!pageId) return notFound();
  const recordMap = await getPage(pageId);
  return <NotionRenderer recordMap={recordMap} fullPage darkMode={false} />;
}
```

---

## 5. Custom Styling & Theming

Override default Notion styles without touching the library source:

```css
/* globals.css */
.notion-page {
  max-width: 760px;
  padding: 0 1rem;
}

/* Customize heading colors */
.notion-h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #1a1a2e;
}

/* Custom callout background */
.notion-callout {
  background: #f0f9ff;
  border-left: 4px solid #3b82f6;
  border-radius: 0.5rem;
}
```

---

## 6. Performance Checklist

1. **Always use `generateStaticParams`** for known pages (ISR or full static).
2. **Dynamic import all third-party renderers** (`Code`, `Equation`, `Pdf`, `Tweet`) with `ssr: false` where needed.
3. **Cache API responses** using Next.js `fetch` cache or Redis for public pages.
4. **Image optimization:** Wrap `NotionRenderer` with a custom `mapImageUrl` function to route images through Next.js `<Image>` optimization.

