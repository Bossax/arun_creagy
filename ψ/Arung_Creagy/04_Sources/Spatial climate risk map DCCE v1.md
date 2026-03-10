---
type: evergreen
status: current
tags:
  - DCCE
  - risk_assessment
last_updated: 2025-11-04
---
> [!important] [https://ccecenter.dcce.go.th/riskarea.php](https://ccecenter.dcce.go.th/riskarea.php)
> 
> - The platform is built by
>     
>     [Waranyu Wongseree](https://cpre.eng.kmutnb.ac.th/wrw#)
>     
>     [Jarutat](https://sites.google.com/rumail.ru.ac.th/envsciru/%E0%B9%80%E0%B8%81%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%9A%E0%B9%80%E0%B8%A3%E0%B8%B2/%E0%B8%9A%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%81%E0%B8%A3/%E0%B8%9C%E0%B8%8A%E0%B8%A7%E0%B8%A2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B8%B2%E0%B8%88%E0%B8%B2%E0%B8%A3%E0%B8%A2-%E0%B8%94%E0%B8%A3-%E0%B8%88%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%A8%E0%B8%99-%E0%B8%AA%E0%B8%99%E0%B8%95%E0%B8%AA%E0%B8%A3%E0%B8%AA%E0%B8%A1%E0%B8%9A%E0%B8%A3%E0%B8%93?authuser=0)
>     
> - The methodology is created by RU-CORE
>     
>     โครงการเพิมประสิทธิภาพการขับเคลื่อนนโยบายด้านการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ : การพัฒนาระบบฐานข้อมูลความเสี่ยงเชิงพื้นทีจากการเปลี่ยนแปลงสภาพภูมิอากาศ
>     
>     [https://thecreagycom.sharepoint.com/:b:/s/crteam/Ecd8d9VHnYpBiuNoc0D8BfIBLRZdPtBLjCqOS4VV76CQ5Q?e=TDhGkH](https://thecreagycom.sharepoint.com/:b:/s/crteam/Ecd8d9VHnYpBiuNoc0D8BfIBLRZdPtBLjCqOS4VV76CQ5Q?e=TDhGkH)
>     
>     [https://cpre.eng.kmutnb.ac.th/climate-change](https://cpre.eng.kmutnb.ac.th/climate-change)
>     

> [!important] Methodology
> 
> 1. Climate projections from climate down scaling: **SEACLID/CORDEX Southeast Asia Phase 2:** provide high resolution (3 – 5 km × 3 – 5 km) multi-model, multi-scenarios climate change projections (hazard)
> 2. Non-climatic parameters: gathered from socioeconomic/ environmental sources. They represent exposure and vulnerability

  
The 24 ==climatic== extreme indicators are from WMO

The 80 ==vulnerability== and ==exposure== indicators are from domestic sources

The provincial values of an indicator is _normalized_ by the national maximum of that indicator.

This way, we obtain ‘relative’ value of the hazard and vulnerability severity. This is used for risk calculation, which is also relative.

![[image 5.png|image 5.png]]

### Extreme indices

> [!info] www.ipcc.ch  
>  
> [https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_AnnexVI.pdf](https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_AnnexVI.pdf)  

Developed by [Expert Team on Climate Change Detection and Indices (ETCCDI)](https://www.wcrp-climate.org/etccdi)

[https://www.climdex.org/learn/indices/](https://www.climdex.org/learn/indices/)

### Data dictionary

|**รหัส**|**ภัยอันตราย**|**ชนิด**|**ดัชนี**|**ชื่อตัวแปร**|**หน่วย**|**นิยาม**|
|---|---|---|---|---|---|---|
|C01|ความร้อน|ค่าเฉลี่ย|ค่าเฉลี่ยรายปีของอุณหภูมิต่ำสุด|TMAXmean|°C|ค่าเฉลี่ยของอุณหภูมิสูงสุดรายวัน|
|C02|ความร้อน|ค่าเฉลี่ย|ค่าเฉลี่ยรายปีของอุณหภูมิเฉลี่ย|TMINmean|°C|ค่าเฉลี่ยของอุณหภูมิเฉลี่ยรายวัน|
|C03|ความร้อน|ค่าเฉลี่ย|ค่าเฉลี่ยรายปีของอุณหภูมิสูง|TMEANmean|°C|ค่าเฉลี่ยของอุณหภูมิต้ำสุดสุดรายวัน|
|C04|ความร้อน|ความรุนแรง|ค่าต่ำสุดของอุณหภูมิสูงสุด|TXn|°C|ค่าต่ำสุดของอุณหภูมิสูงสุดรายวัน|
|C05|ความร้อน|ความรุนแรง|ค่าต่ำสุดของอุณหภูมิสูงสุด|TNn|°C|ค่าต่ำสุดของอุณหภูมิต่ำสุดรายวัน|
|C06|ความร้อน|ความรุนแรง|ค่าสูงสุดของอุณหภูมิสูงสุด|TXx|°C|ค่าสูงสุดของอุณหภูมิสูงสุดรายวัน|
|C07|ความร้อน|ความรุนแรง|ค่าสูงสุดของอุณหภูมิต่ำสุด|TNx|°C|ค่าสูงสุดของอุณหภูมิต่ำสุดรายวัน|
|C08|ความร้อน|ความรุนแรง|ช่วงอุณหภูมิรอบวัน|DTR|°C|ค่าเฉลี่ยของความแตกต่างระหว่างงอุณหภูมิสูงสุดและอุณหภูมิต่ำสุดรายวัน|

### Represents Vulnerability and exposure

- The **vulnerability** and **exposure** indicators are grouped by hazard type (flood, heat, drought). The diagram represent flood risk indicators
- There should be a report on how these indicators are selected

![[image 1 2.png|image 1 2.png]]

> [!important] They should be able to provide the exposure and vulnerability datasets used for this analysis and methodology of data processing e.g. cleaning data, assure data quality, definition of exposure and vulnerability

  

> ค่าดัชนีทั้งสามส่วนที่วิเคราะห์ได้(แก่ ดัชนีภัยอันตราย ดัชนีปัจจัยที่ไม่ใช่ภูมิอากาศ และดัชนีความเสี่ยงซึ่งแสดงผลในแผนที่ภัยอันตราย แผนที่ปัจจัยที่ไม่ใช่ภูมิอากาศ และแผนที่ความเสี่ยง มีนัยเพื่อการเปรียบเทียบระหว่างช่วงปีและจังหวัด แต่ไม่ได้(มีความหมายในเชิงปริมาณ กล่าวคือเป็นการเปรียบเทียบลำดับของดัชนีแต่ไม่ใช่เป็นการเปรียบเทียบระดับของดัชนี ดัชนีความเสี่ยงที่วิเคราะห์และแสดงผลในฐานข(อมูลได้รับการปรับสเกลดัชนีให(มีค่าอยู่ระหว่าง 0 – 1 ด้วยเทคนิค Minimum-Maximum Normalization ส่งผลให้จังหวัดหนึ่งในปีหนึ่ง ในช่วง ค.ศ.1970 - 2099 ของการวิเคราะห์ความเสี่ยงจากภัยอันตรายแต่ละด้านหรือความเสี่ยงจากภัยอันตรายรวม มีค่าดัชนีสูงสุดเท่ากับ 1 ซึ่งมีความหมายว่าจังหวัดดังกล่าวมีความเสี่ยงจากภัยที่พิจารณาสูงกว่าทุกจังหวัดและเกิดขึ้นในปีดังกล่าว แต่การคาดประมาณการเปลี่ยนแปลงภูมิอากาศจะไม่พิจารณาผลเฉพาะปี ฐานข้อมูลที่พัฒนาขึ้นจึงแสดงผลเป็นช่วงปี ได้แก่ ปีฐาน (ค.ศ. 1970 – 2005)อนาคตอันใกล้ (ค.ศ. 2016 – 2035) อนาคตระยะปานกลาง (ค.ศ. 2046 – 2065) และอนาคตระยะไกล(ค.ศ. 2081 – 2099) ซึ่งให(ผลการวิเคราะห์ในเชิงของการเปรียบเทียบ “ลำดับ” ความเสี่ยงของจังหวัดในแต่ละช่วงปี การวิเคราะหOระดับของความเสี่ยง ควรพิจารณาแผนที่ความเสี่ยงกำหนดปัจจัยเองร่วมกับแผนที่ภูมิอากาศ ทั้งนี้เพื่อให(ทราบว่าจังหวัดที่มีลำดับความเสี่ยงสูงจากแผนที่ความเสี่ยงนั้น มี “ระดับ”การเปลี่ยนแปลงภูมิอากาศ เช่น ปริมาณฝน อุณหภูมิ เป็นต้น แตกต่างไปจากปีฐานมากน้อยเพียงใด

  

## **Hazard map and Exposure of some asset classes**

Grid size 25 km: still too large. The research group wanted to downscale to 5 km

Asset layers:
- Rice cultivation map
- Hospital map

![[image 2 3.png|image 2 3.png]]