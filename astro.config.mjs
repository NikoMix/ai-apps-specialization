// Local development config.
// In CI, the workflow clones the private theme repo and uses its astro.config.mjs instead.
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [
    starlight({
      title: 'AI Apps on Microsoft Azure – Advanced Specialization',
      description:
        'Partner enablement guide for the AI Applications on Microsoft Azure Advanced Specialization audit.',
      logo: {
        alt: 'Microsoft Partner',
        src: './src/assets/logo.svg',
      },
      social: {
        github: 'https://github.com/YOUR_ORG/YOUR_CONTENT_REPO',
      },
      sidebar: [
        { label: 'Home', link: '/' },
        { label: 'Overview', link: '/overview/' },
        { label: 'Pre-Qualification Requirements', link: '/requirements/' },
        { label: 'Audit Process', link: '/audit-process/' },
        {
          label: 'Module A – General Requirements',
          autogenerate: { directory: 'module-a' },
        },
        {
          label: 'Module B – AI Apps Specific',
          autogenerate: { directory: 'module-b' },
        },
        { label: 'Evidence Tracker', link: '/evidence-tracker/' },
        { label: 'FAQ', link: '/faq/' },
      ],
      editLink: {
        baseUrl: 'https://github.com/YOUR_ORG/YOUR_CONTENT_REPO/edit/main/',
      },
    }),
  ],
});
