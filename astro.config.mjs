import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const repo = process.env.GITHUB_REPOSITORY ?? 'YOUR_ORG/ai-apps-specialization';
const [owner, repoName] = repo.split('/');
const isUserOrOrgPage = repoName?.toLowerCase() === `${owner?.toLowerCase()}.github.io`;

const site =
  process.env.ASTRO_SITE ??
  (isUserOrOrgPage ? `https://${owner}.github.io` : `https://${owner}.github.io/${repoName}`);

const base = process.env.ASTRO_BASE ?? (isUserOrOrgPage ? '/' : `/${repoName}/`);
const githubUrl = process.env.ASTRO_GITHUB_URL ?? `https://github.com/${repo}`;

export default defineConfig({
  site,
  base,
  integrations: [
    starlight({
      title: 'AI Apps on Microsoft Azure – Advanced Specialization',
      description:
        'Partner enablement guide for the AI Applications on Microsoft Azure Advanced Specialization audit.',
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: githubUrl,
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
        {
          label: 'Engagement Playbook',
          items: [
            { label: 'Qualification Questionnaire', link: '/engagement/qualification-questionnaire/' },
            { label: 'Assessment Platform Inputs', link: '/engagement/assessment-platform-inputs/' },
            { label: 'Discovery Workshop', link: '/engagement/discovery-workshop/' },
            { label: 'Project Plan Template', link: '/engagement/project-plan/' },
            { label: 'Microsoft Assessments', link: '/engagement/assessments/' },
            { label: 'Well-Architected Framework Assessment', link: '/engagement/waf-assessment/' },
            { label: 'Reference Architectures', link: '/engagement/reference-architectures/' },
            { label: 'Resources and Samples', link: '/engagement/resources-and-samples/' },
            { label: 'Definition of Done', link: '/engagement/definition-of-done/' },
            { label: 'Offering One-Pager', link: '/engagement/offering-one-pager/' },
            {
              label: 'Deliverables',
              items: [
                { label: 'Architecture Design', link: '/engagement/deliverables/hld-template/' },
                { label: 'Technical Design', link: '/engagement/deliverables/lld-template/' },
                { label: 'Knowledge Transfer Plan', link: '/engagement/deliverables/kt-plan-template/' },
                { label: 'Hypercare Plan', link: '/engagement/deliverables/hypercare-plan-template/' },
                { label: 'Runbook Template', link: '/engagement/deliverables/runbook-template/' },
              ],
            },
          ],
        },
        {
          label: 'Innersource',
          items: [{ autogenerate: { directory: 'innersource' } }],
        },
        { label: 'Evidence Tracker', link: '/evidence-tracker/' },
        { label: 'FAQ', link: '/faq/' },
      ],
      editLink: {
        baseUrl: `${githubUrl}/edit/main/`,
      },
    }),
  ],
});
