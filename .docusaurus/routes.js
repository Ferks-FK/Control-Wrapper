import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/docs/markdown-page',
    component: ComponentCreator('/docs/markdown-page', '62e'),
    exact: true
  },
  {
    path: '/docs/docs',
    component: ComponentCreator('/docs/docs', '51c'),
    routes: [
      {
        path: '/docs/docs/',
        component: ComponentCreator('/docs/docs/', '634'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/category/methods',
        component: ComponentCreator('/docs/docs/category/methods', 'c4d'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/category/tutorial---basics',
        component: ComponentCreator('/docs/docs/category/tutorial---basics', 'ab3'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/category/tutorial---extras',
        component: ComponentCreator('/docs/docs/category/tutorial---extras', 'a37'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/development/users',
        component: ComponentCreator('/docs/docs/development/users', '43b'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/tutorial-basics/congratulations',
        component: ComponentCreator('/docs/docs/tutorial-basics/congratulations', '842'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/tutorial-basics/create-a-blog-post',
        component: ComponentCreator('/docs/docs/tutorial-basics/create-a-blog-post', '646'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/tutorial-basics/create-a-document',
        component: ComponentCreator('/docs/docs/tutorial-basics/create-a-document', '6ba'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/tutorial-basics/create-a-page',
        component: ComponentCreator('/docs/docs/tutorial-basics/create-a-page', 'b34'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/tutorial-basics/deploy-your-site',
        component: ComponentCreator('/docs/docs/tutorial-basics/deploy-your-site', 'bed'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/tutorial-basics/markdown-features',
        component: ComponentCreator('/docs/docs/tutorial-basics/markdown-features', '6f0'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/tutorial-extras/manage-docs-versions',
        component: ComponentCreator('/docs/docs/tutorial-extras/manage-docs-versions', '055'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs/tutorial-extras/translate-your-site',
        component: ComponentCreator('/docs/docs/tutorial-extras/translate-your-site', '946'),
        exact: true,
        sidebar: "tutorialSidebar"
      }
    ]
  },
  {
    path: '/docs/',
    component: ComponentCreator('/docs/', '7f5'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
