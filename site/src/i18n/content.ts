export const EN = {
  project: {
    name: 'Multi-Agent Precision Manufacturing and Inspection of Large Optical Mirrors',
    short: 'Large Mirror Intelligent Manufacturing',
    team: 'Project Team',
  },
  hero: {
    lines: [
      'Spaceborne remote sensing',
      'Deep-space exploration',
      'High-energy lasers · large telescopes',
      'Enabling intelligent manufacturing',
      'of large mirrors',
    ],
  },
  research: {
    framework: {
      title: 'Multi-agent coordination framework',
      description:
        'Build an inspection–strategy–execution–decision loop with unified multi-source data, interfaces and knowledge representation.',
      body: `
        <h2>Decision and scheduling agent</h2>
        <p>Large mirror fabrication involves multiple processes, difficult hand-over decisions and limited process adaptivity. The project builds a multi-agent framework in which metrology, polishing strategy, execution and scheduling agents work together.</p>
        <h2>Key technologies</h2>
        <ul>
          <li>Overall multi-agent organisation and interfaces</li>
          <li>Scheduling-driven determination of priority inspection areas</li>
          <li>Strategy constraints across multiple polishing rounds</li>
          <li>Iteration-stop criteria and process-stage switching</li>
          <li>Information coordination and continuous knowledge update</li>
        </ul>
        <h2>Public targets</h2>
        <ul><li>Knowledge base &gt;10,000 entries</li><li>Recommendation adoption &gt;50%</li><li>Single decision &le;5 min</li></ul>
      `,
    },
    inspection: {
      title: 'In-situ active inspection',
      description:
        'Fuse SAP, PMD and dynamic interferometry on a unified spatial datum for in-situ form and surface-defect inspection.',
      body: `
        <h2>Metrology agent</h2>
        <p>The project addresses misalignment after mirror transport, accuracy gaps between process stages and manual surface-defect inspection. It studies laser-vision spatial referencing, multi-modal inspection chains, physics-constrained robustness and active defect inspection.</p>
        <h2>Key technologies</h2>
        <ul>
          <li>Laser-vision spatial datum and SAP–PMD–DI coordination</li>
          <li>Physics-constrained evolution of inspection modes</li>
          <li>Environmental disturbance suppression under complex conditions</li>
          <li>Full-field PMD surface-quality evaluation</li>
          <li>Multi-scale active defect inspection</li>
        </ul>
        <h2>Public targets</h2>
        <ul><li>Typical surface-defect accuracy &ge;90%</li><li>Single 800 mm inspection &le;10 min</li></ul>
      `,
    },
    strategy: {
      title: 'Full-parameter adaptive strategy',
      description:
        'Study generation, evaluation and closed-loop optimisation of complex polishing strategies using transient process models and physical constraints.',
      body: `
        <h2>Polishing-strategy agent</h2>
        <p>The work targets unified transient-process modelling, analysis of complex polishing strategies and full-parameter optimisation. It combines physics-constrained transient modelling, intelligent analysis of polishing characteristics and adaptive closed-loop optimisation.</p>
        <h2>Key technologies</h2>
        <ul>
          <li>Physics-constrained transient process modelling</li>
          <li>Analysis of complex polishing strategies</li>
          <li>Dynamic simulation of edge effects</li>
          <li>Full-parameter strategy generation and evaluation</li>
          <li>Inspection-feedback adaptive optimisation</li>
        </ul>
        <h2>Public targets</h2>
        <ul><li>Polishing efficiency &ge;40% higher</li><li>Edge-effect area and amplitude each reduced by 50%</li></ul>
      `,
    },
    execution: {
      title: 'Long-horizon machine self-sensing',
      description:
        'Use multi-modal time-series data to sense machine degradation and faults, forming a degradation–anomaly–response loop.',
      body: `
        <h2>Execution agent</h2>
        <p>The project studies long-horizon multi-modal degradation sensing, non-intrusive open-set fault detection, hierarchical localisation and autonomous response for polishing machines.</p>
        <h2>Key technologies</h2>
        <ul>
          <li>Long-horizon multi-modal degradation sensing and quantification</li>
          <li>Rapid adaptation across operating conditions</li>
          <li>Non-intrusive open-set fault detection</li>
          <li>Hierarchical fault localisation</li>
          <li>Autonomous degradation/fault response and parameter fine-tuning</li>
        </ul>
        <h2>Public targets</h2>
        <ul><li>Typical fault detection &ge;90%</li><li>Closed-loop response and execution-parameter fine-tuning</li></ul>
      `,
    },
    integration: {
      title: 'Verification and system integration',
      description:
        'Integrate and evaluate the multi-agent system on an 800 mm-class mirror fabrication and inspection workstation.',
      body: `
        <h2>System integration</h2>
        <p>On the jointly developed 800 mm-class mirror fabrication and inspection workstation, the team integrates multi-agent coordination, interfaces, representative mirror polishing and overall performance evaluation.</p>
        <h2>Key tasks</h2>
        <ul>
          <li>Integration of multi-agent coordination functions</li>
          <li>Verification of key methods</li>
          <li>System-level closed-loop verification</li>
          <li>Overall performance evaluation and method refinement</li>
        </ul>
        <h2>Public targets</h2>
        <ul><li>A runnable multi-agent mirror-polishing prototype</li><li>Fabrication of a mirror of &ge;800 mm aperture</li></ul>
      `,
    },
  },
  activities: {
    '2026-07-start': {
      title: 'Project enters execution phase',
      description:
        'The 36-month execution period starts in July 2026, with three institutions jointly addressing five research tasks.',
      body: '<p>The execution period runs from July 2026 to June 2029. The project is led by the Nanjing Institute of Astronomical Optics &amp; Technology, CAS, with the Institute of Industrial Artificial Intelligence, CAS, and Nanjing Nair Optoelectronic Instruments Co., Ltd.</p>',
    },
    '2026-10-kickoff': {
      title: 'Project kick-off and first working meeting',
      description:
        'The meeting covered execution rules, indicator breakdown, task allocation, data acquisition and verification sites.',
      body: '<p>The project follows an execution framework based on the task book, a three-tier plan and five management mechanisms. Overall scheme and interface definition were identified as immediate priorities.</p>',
    },
    '2026-11-repository': {
      title: 'Public information repository launched',
      description:
        'Public notices, key milestones and research information are now published in a single repository.',
      body: '<p>The repository publishes public notices and key milestones. Internal materials, personal contact details and non-public identifiers are excluded.</p>',
    },
  },
  news: {
    '2026-12-p1': {
      title: 'P1 scheme and interfaces frozen',
      summary: 'Schemes for five research tasks, interface relationships, data and knowledge framework, and experimental environment.',
    },
    '2027-02-g1': {
      title: 'G1 overall scheme review',
      summary: 'Review of the overall scheme, interface definitions, requirements and knowledge-base framework.',
    },
    '2027-12-m1': {
      title: 'M1 mid-term milestone',
      summary: 'A runnable mid-term prototype of five agent types, with the knowledge-base framework and main knowledge entries completed.',
    },
    '2028-06-g3': {
      title: 'G3 integration and commissioning',
      summary: 'The inspection–strategy–execution–decision loop is connected and verified on a representative mirror.',
    },
    '2028-12-m2': {
      title: 'M2 targets achieved',
      summary: 'Prototype and main technical indicators achieved; a relatively complete knowledge base, algorithms and software system formed.',
    },
    '2029-06-g5': {
      title: 'G5 project acceptance',
      summary: 'Acceptance materials, third-party testing and financial settlement completed.',
    },
  },
  pages: {
    activitiesUpdates: 'Project updates',
    activitiesMilestones: 'Project milestones',
    publicationsDesc: 'Journal and conference articles produced after the project start. Only public, citable outputs are listed.',
    publicationsEmptyTitle: 'Project articles will appear here.',
    publicationsEmptyText: 'There are currently no public project articles.',
    patentsDesc: 'Patents filed or granted after the project start. Only public bibliographic information is listed.',
    patentsEmptyTitle: 'Project patents will appear here.',
    patentsEmptyText: 'There are currently no public project patents.',
    backToResearch: 'Back to Research',
    backToActivities: 'Back to Activities',
    footerInfo: 'Public project information · 2026–2029',
    imageCredits: 'Cover image',
  },
};
