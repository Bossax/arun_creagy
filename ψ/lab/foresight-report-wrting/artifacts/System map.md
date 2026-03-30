graph TD
    %% Central Node
    Violence((สถานการณ์ความรุนแรง))

    %% Top Left: Climate & Social
    Climate[Climate change] --> QoL[คุณภาพชีวิตของประชาชน]
    Social[Social values] --> Accept[การยอมรับความหลากหลาย]
    Accept --> QoL
    QoL -- "-" --> Violence

    %% Middle Left: Medical & Economy
    MedTech[Medical Technology] --> LifeExp[อายุขัยเฉลี่ย]
    Economy[เศรษฐกิจ] --> Household[รายจ่ายของครัวเรือน]
    Household --> Debt[ปัญหาหนี้สิน]
    Debt -- "+" --> Violence
    EconGrowth[เศรษฐกิจของภูมิภาค] -- "-" --> Violence

    %% Bottom: AI & Education
    AGI[ความก้าวหน้าของ AGI] --> AIChat[AI Chatbot ในการเรียนรู้]
    AGI --> EduQuality[คุณภาพการศึกษา]
    AIChat --> EduQuality
    EduQuality --> YouthSkill[ทักษะอาชีพของเด็ก]
    YouthSkill --> JobOpp[โอกาสในการทำงาน]
    JobOpp -- "-" --> Violence

    %% Right: Robotics & Geopolitics
    Robotics[Robotics] --> MilTech[เทคโนโลยีการทหารแบบแม่นยำ]
    MilTech -- "+" --> Violence
    Geopolitics[Geopolitics] --> Border[ความขัดแย้งชายแดน]
    Border -- "+" --> Violence

    %% Far Right: Unrest
    Unrest[ความไม่สงบ] --> Religion[ความขัดแย้งทางศาสนา]
    Religion -- "+" --> Violence
    GovTrust[ความเชื่อมั่นในรัฐบาล] -- "-" --> Unrest
    Unrest -- "+" --> Violence

    %% Styling
    style Violence fill:#f96,stroke:#333,stroke-width:4px
    style Economy fill:#f99
    style Education fill:#ff9
    style AI_Section fill:#ccf