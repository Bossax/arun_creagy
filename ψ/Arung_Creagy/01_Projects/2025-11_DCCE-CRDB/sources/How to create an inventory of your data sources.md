---
type: web clipped
status: raw
tags:
capture_date:
url: https://www.lightsondata.com/how-to-create-an-inventory-of-your-data-sources/
relevance to: "[["
sticker: emoji//1f310
---
by

[![data sources inventory template](https://i0.wp.com/www.lightsondata.com/wp-content/uploads/2018/07/Data-Sources-Inventory2.png?fit=800%2C326&ssl=1)](https://www.lightsondata.com/how-to-create-an-inventory-of-your-data-sources/ "How to create an inventory of your data sources")

A data sources inventory is meant to record basic information about the different systems across and/or outside your ecosystem from which you are capturing, producing, acquiring or procuring data. The data sources tend to be well known to their end users and administrators, but not so much to the organization as a whole. I believe that having this shared knowledge brings a lot of value in identifying efficiencies, finding new data sources to complement your own unit’s needs, helping validate and resolve data quality issues, and a first step to take if you’re implementing a master data management program/ strategy. Nevertheless, understanding your data provenance and your technical ecosystem is a deliverable of a good data governance program and part of the [data quality management trifecta](https://www.lightsondata.com/the-trifecta-of-the-best-data-quality-management/).

## What do you need to capture in your data sources inventory?

The following is a list of metadata I recommend capturing. Based on the complexity of your own technical environment and maturity of your data governance program, you might choose to add other attributes or remove some.

**ID:** A unique ID is always a great idea to have for putting together any inventory in order to reference data quality issues quicker between technical staff, business analysts and business users. The ID could even be numerical or an alpha code derived from the name of the system if that makes it easier to reference.

**System/ application name:** Self-explanatory field, but good to note that a lot of organizations have their internal application names which don’t necessarily correspond with the commercial name of the system. I recommend noting the internal name as this is the one widely used in your environment. For example, Workday’s Human Capital Management product, might be called Human Resource System internally, so please note that here.

**Acronym:** A lot of organizations tend to love TLAs (Three Letter Acronyms). As in the example above, HRS would be the acronym for the human resources system, which even though it might seem obvious to what it represents, that is not the case to those never having heard about it, such as some new employees. It’s of low effort to record, but has a high benefit.

---

##### Spoiler: I’m offering a free template of a data sources inventory at the end of this article.

---

**Platform/ commercial name:** Continuing the same naming topic, what is the commercial name of the system? For the HRS example it would be Human Capital Management. Again, this is most useful for new employees, but it also creates that overall awareness into the actual name of the system which can be useful to reference in the hiring process, conferences, external presentations, etc.

**Vendor:** Who is the vendor providing this system? This information helps identify if multiple different systems are provided by the same vendor. This can potentially identify cost efficiencies in terms of licencing, support, and/ or training costs.

**Absolute path/ URL:** This is a link to the system’s end user or back-end interface for quick access.

**Detailed description:** Any details to offer further context and insight into where the issue was found, what system(s), processes, reports, etc. are known to be affected before an in-depth analysis is done.

**Status:** Use this field to track the status of the system. Is it active, historical/ deprecated, or future?

**Data classification:** What classification group is the data housed in this system part of? – *Read more about the different [data classification groups](https://www.lightsondata.com/data-classification-help-with-gdpr-compliance/) you might have.*

**Business owner:** What is the business area, unit, department owning this system? In smaller organizations this could even be a single individual

**Business contact:** State the name(s) of the person(s) taking business decisions regarding this system. This is usually an institutional contact. A second name is sometimes advised to have on file as a back-up go-to person.

**Technical contact:** Who is the IT individual(s) in charge with its maintenance and technical support? This could be internal to your organization or included in the ongoing support provided by the vendor.

**Physical location:** Is the system on site, does it have a co-location, is it in the cloud? For privacy and security concerns this is useful information to have, though it’s probably documented as part of privacy and security audits and checks – if that’s the case you can just refer to those catalogs. Otherwise I recommend capturing it within the inventory in order to start creating awareness.

**Data inventory link:** This is a link towards the type of data housed in this system. If this information is not detailed anywhere else, you can offer information about the type of data housed in the system at a very high level (ex: student data, fundraising data, personal health data, etc.). I can cover this topic in a later article.

**Data model link:** This is another link towards the physical or logical data model of the system. This is useful for your MDM and data integration strategies, though from experience very few would have this before the data sources inventory is complete.

**Last updated date:** This date field helps you keep track of when changes have been made to a particular entry in this inventory – this can be excluded from the inventory if you’re maintaining this through a custom database, data governance or document management tool as this tends to be automatically recorded in those cases.

**Changes notes:** If there is no document management control in place, I recommend outlining the changes made to the metadata of the inventory’s entry.

---

#### Free template:

![data sources inventory template](https://i0.wp.com/www.lightsondata.com/wp-content/uploads/2018/07/Data-Sources-Inventory2.png?fit=800%2C326&ssl=1)

[Download “Data Sources Inventory Template” Data-Sources-Inventory.xlsx – Downloaded 5410 times – 20.58 KB](https://www.lightsondata.com/download/445/?tmstv=1767768768)

---

#### Conclusion

Making the data sources inventory available to your business users and especially the data stewards, data owners, and data custodians will not only bring better understanding of your organization’s technical environment, but could also create cost and operational efficiency opportunities, and consolidation of data quality and data integration efforts. Have you implemented your data sources inventory, yet? What were the drivers and benefits from doing so? What else have you recorded in it?

About the author

#### George Firican

George Firican is the Director of Data Governance and Business Intelligence at the University of British Columbia, which is ranked among the top 20 public universities in the world. His passion for data led him towards award-winning program implementations in the data governance, data quality, and business intelligence fields. Due to his desire for continuous improvement and knowledge sharing, he founded LightsOnData, a website which offers free templates, definitions, best practices, articles and other useful resources to help with data governance and data management questions and challenges. He also has over twelve years of project management and business/technical analysis experience in the higher education, fundraising, software and web development, and e-commerce industries.

## You may also like:

Wayne Yaddow

01/29/2020