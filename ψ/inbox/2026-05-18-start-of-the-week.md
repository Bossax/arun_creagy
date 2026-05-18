this week, P Mom, the project manager of the cri project will visit Chiang Rai to communicate the project to local officials and potentially request raw LPA filing that is held by the Local Administrations Organizations such as Tessaban, PAO. We have faced and issues of data granularity of LPA indicators. We were informed by the department of provincial administration that the LPA data that they have in the database is aggregated or already assessed by provincial committees. So, they cannot tell the score of indicator x under category Y. They can tell the total performance of category y of a Tessaban. This is why we stumbled and thought that CRI phase 2, the resilience indicator, might not be achievable given the data management conditions of DOPA. My recommendation to DCCE is that, in this project, we build a strong case why CRI will benefit the society and DOPA. Then, DCCE needs to continually engage DOPA to improve their data collection practice to satisfy CRI use case. 

---

Last week, I made a notebook to visualize DDPM disaster statistics data for Chiang Rai. This week, we will apply the same logic to the entire country. This is what I think we need to do

1. clean the administrative boundary shapefiles: the province , district, and sub-district codes in the shapefiles are missing for some areas that are misnamed. For example, "กิ่งอำเภอ" is a relic that should be removed. See [wikipedia](https://th.wikipedia.org/wiki/%E0%B8%81%E0%B8%B4%E0%B9%88%E0%B8%87%E0%B8%AD%E0%B8%B3%E0%B9%80%E0%B8%A0%E0%B8%AD). We need to assign every tambon (sub-district) a code. We need to debug as we go. 
2. when we clean the shapefiles, we need to demote the original or archive it and promote the cleaned ones to silver layer.
3. when done, we can then perform the data analysis for every tambon in this country. We need to figure out how to store the data for visualization on a web app. 
4. We need to have an option to export data of a province in excel workbook or csv too. The name of the areas must be in Thai

---
We need to process the CRDB workshop outputs. The files are in Excel and Word [C:\Users\sitth\OneDrive - The Creagy Company Limited\DCCE Climate Risk DataBase - Documents\03_Working_file\Stakeholder Engagement\Workshop\สรุปการประชุม]

check the workshop master design v2, project evidence registry, use cases, NCAIF design to understand what aspects we need to extract from these materials. Then  I need to think a bit further. 

---

I need to steer and move CRDB forward after the workshop. Recall important dates from  [[ψ/incubate/DCCE/CRDB/inbox_note/2026-05-13-project-reorientation-after-workshop|2026-05-13-project-reorientation-after-workshop]]. I need to figure out the next steps. For now, without systemic digging, I feel that I need to scope down the topics for the 10 climate risk and adaptation articles per TOR 5.5. 

