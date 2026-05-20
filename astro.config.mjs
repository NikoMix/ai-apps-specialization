import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// When deploying to GitHub Pages, set the SITE env variable to your Pages URL,
// e.g. https://YOUR_ORG.github.io/YOUR_REPO_NAME
// GitHub Actions: add a repo variable ASTRO_SITE or hard-code below.
const site = process.env.ASTRO_SITE ?? 'https://example.github.io/ai-apps-specialization';

export default defineConfig({
  site,
  integrations: [
    starlight({
      title: 'AI Apps on Microsoft Azure – Advanced Specialization',
      description:
        'Partner enablement guide for the AI Applications on Microsoft Azure Advanced Specialization audit.',
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: process.env.ASTRO_GITHUB_URL ?? 'https://github.com/YOUR_ORG/YOUR_REPO',
        },
      ],
      sidebar: [
        { label: 'Home', link: '/' },
        { label: 'Overview', link: '/overview/' },
        { label: 'Pre-Qualification Requirements', link: '/requirements/' },
        { label: 'Audit Process', link: '/audit-process/' },
        {
          label: 'Module A – General Requirements',
          items: [{ autogenerate: { directory: 'module-a' } }],
        },
        {
          label: 'Module B – AI Apps Specific',
          items: [{ autogenerate: { directory: 'module-b' } }],
        },
        { label: 'Evidence Tracker', link: '/evidence-tracker/' },
        { label: 'FAQ', link: '/faq/' },
      ],
      editLink: {
        baseUrl:
          (process.env.ASTRO_GITHUB_URL ?? 'https://github.com/YOUR_ORG/YOUR_REPO') +
          '/edit/main/',
      },
    }),
  ],
});
