import heroImage from './assets/hero-applications.jpg';

export const SITE = {
  website: 'https://iphytian.github.io/Jiangsu_optiforge/',
  author: '项目组',
  description:
    '面向航天遥感、深空探测、高能激光与大型望远镜应用，开展基于多智能体的大口径光学镜面精密制造与检测技术研发。',
  title: '基于多智能体的大口径光学镜面精密制造与检测技术研发',
  ogImage: 'astropaper-og.jpg',
  lightAndDarkMode: true,
  postPerPage: 3,
  scheduledPostMargin: 15 * 60 * 1000,

  labName: '基于多智能体的大口径光学镜面精密制造与检测技术研发',
  labNameShort: '大口径镜面智能制造',
  university: '项目组',
  logo: '/assets/logo-project.svg',
  avatar: '/assets/logo-project.svg',
  email: '',

  hero: {
    title: '面向航天遥感 · 深空探测 · 高能激光 · 大型望远镜，实现大口径镜面智能制造。',
    subtitle: '基于多智能体的大口径光学镜面精密制造与检测技术研发',
    action: '查看文章',
    image: heroImage,
  },

  nav: [
    { text: '首页', link: '/', key: 'home' },
    { text: '研究方向', link: '/research', key: 'research' },
    { text: '项目进展', link: '/activities', key: 'activities' },
    { text: '文章', link: '/publications', key: 'publications' },
    { text: '专利', link: '/patents', key: 'patents' },
  ],

  customPages: [],

  i18n: {
    enabled: true,
    defaultLocale: 'zh',
  },
};

export const LOCALE = {
  lang: 'zh-CN',
  langTag: ['zh-CN'],
} as const;

export const LOGO_IMAGE = {
  enable: true,
  svg: true,
  width: 216,
  height: 46,
};

export const SOCIALS = [];

export const DEFAULT_LANG: 'zh' | 'en' | 'ja' | 'ko' | 'fr' | 'de' | 'es' | 'ru' = 'zh';
