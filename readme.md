# أداة التقييم الذاتي لضوابط CIS للجهات الحكومية الكويتية
# CIS Benchmark Compliance Checker for Kuwait Government Entities

<div dir="rtl">

## نظرة عامة

أداة تقييم ذاتي شاملة مصممة خصيصاً للجهات الحكومية الكويتية لتقييم جاهزيتها الأمنية السيبرانية وفقاً لإطار ضوابط مركز أمان الإنترنت (CIS Controls v8). تم تطوير هذه الأداة بناءً على البحث العلمي: ["رفع مستوى استعدادات الأمن السيبراني في الجهات الحكومية بدولة الكويت من خلال تطبيق ضوابط إطار مركز أمان الإنترنت (CIS)"](https://www.researchgate.net/publication/384449388).

</div>

## Overview

A self-assessment tool specifically designed for Kuwait government entities to evaluate their cybersecurity readiness according to the CIS Controls v8 framework. This tool is based on scientific research about elevating cybersecurity preparedness in Kuwait government agencies through CIS framework implementation.

---

## 🎯 Key Features | المميزات الرئيسية

<div dir="rtl">

### للمستخدمين العرب:
- **واجهة ثنائية اللغة**: دعم كامل للعربية والإنجليزية مع تصميم RTL احترافي
- **18 ضابط أمني**: تقييم شامل لجميع ضوابط CIS Controls v8 (153 إجراء وقائي)
- **ثلاث مجموعات تنفيذية**: IG1 (56 إجراء)، IG2 (74 إجراء)، IG3 (23 إجراء)
- **تقييم مستوى النضج**: 5 مستويات من الأولي إلى المحسّن
- **تقارير تفصيلية**: تقارير PDF واضحة باللغة العربية مع توصيات عملية
- **سياق كويتي**: مواءمة مع رؤية الكويت 2035 والاستراتيجية الوطنية للأمن السيبراني

</div>

### For English Users:
- **Bilingual Interface**: Full Arabic and English support with professional RTL design
- **18 Security Controls**: Comprehensive assessment of all CIS Controls v8 (153 safeguards)
- **Three Implementation Groups**: IG1 (56 safeguards), IG2 (74 safeguards), IG3 (23 safeguards)
- **Maturity Assessment**: 5 levels from Initial to Optimized
- **Detailed Reports**: Clear PDF reports in Arabic with actionable recommendations
- **Kuwait Context**: Aligned with Kuwait Vision 2035 and National Cybersecurity Strategy

---

## 📊 CIS Controls v8 Structure | هيكل ضوابط CIS

| # | Control (English) | الضابط (عربي) | Safeguards | IG1 | IG2 | IG3 |
|---|---|---|:---:|:---:|:---:|:---:|
| 1 | Inventory and Control of Enterprise Assets | جرد ومراقبة أصول المؤسسة | 5 | 4 | 1 | 0 |
| 2 | Inventory and Control of Software Assets | جرد ومراقبة الأصول البرمجية | 7 | 4 | 3 | 0 |
| 3 | Data Protection | حماية البيانات | 14 | 6 | 5 | 3 |
| 4 | Secure Configuration | التكوين الآمن للأصول | 12 | 7 | 4 | 1 |
| 5 | Account Management | إدارة الحسابات | 6 | 4 | 2 | 0 |
| 6 | Access Control Management | إدارة التحكم في الوصول | 8 | 5 | 2 | 1 |
| 7 | Continuous Vulnerability Management | الإدارة المستمرة للثغرات | 7 | 4 | 3 | 0 |
| 8 | Audit Log Management | إدارة سجلات التدقيق | 12 | 5 | 5 | 2 |
| 9 | Email and Web Browser Protections | حماية البريد والمتصفح | 7 | 5 | 2 | 0 |
| 10 | Malware Defenses | الدفاعات ضد البرمجيات الخبيثة | 7 | 5 | 2 | 0 |
| 11 | Data Recovery | استعادة البيانات | 5 | 4 | 1 | 0 |
| 12 | Network Infrastructure Management | إدارة البنية التحتية للشبكة | 8 | 4 | 3 | 1 |
| 13 | Network Monitoring and Defense | مراقبة الشبكة والدفاع | 11 | 3 | 5 | 3 |
| 14 | Security Awareness and Training | التوعية الأمنية والتدريب | 9 | 5 | 4 | 0 |
| 15 | Service Provider Management | إدارة مقدمي الخدمات | 7 | 3 | 3 | 1 |
| 16 | Application Software Security | أمن البرمجيات التطبيقية | 14 | 3 | 7 | 4 |
| 17 | Incident Response Management | إدارة الاستجابة للحوادث | 9 | 4 | 4 | 1 |
| 18 | Penetration Testing | اختبار الاختراق | 5 | 0 | 2 | 3 |
| **TOTAL** | | **المجموع** | **153** | **75** | **58** | **20** |

---

## 🚀 Getting Started | البدء السريع

### Option 1: Web Application | التطبيق عبر الإنترنت

<div dir="rtl">

**الطريقة الأسهل**: قم بزيارة الأداة مباشرة عبر الرابط:
```
https://siteq8.github.io/CIS-Kuwait-Assessment/
```

</div>

**Easiest method**: Visit the tool directly at the link above.

### Option 2: Local Installation | التثبيت المحلي

```bash
# Clone the repository
git clone https://github.com/SiteQ8/CIS-Kuwait-Assessment.git

# Navigate to directory
cd CIS-Kuwait-Assessment

# Open in browser
open index.html
# Or for Windows:
start index.html
```

---

## 📖 How to Use | كيفية الاستخدام

<div dir="rtl">

### خطوات التقييم:

1. **معلومات الجهة**: أدخل اسم الجهة، القطاع، الحجم، ومعلومات الاتصال
2. **اختيار المجموعة التنفيذية**: حدد IG1، IG2، أو IG3 بناءً على حجم ومتطلبات جهتك
3. **التقييم الذاتي**: أجب على أسئلة التقييم الرئيسية لكل من الضوابط الـ18
4. **عرض النتائج**: اطلع على لوحة النتائج الشاملة مع الرسوم البيانية
5. **التوصيات**: راجع التوصيات ذات الأولوية لتحسين الوضع الأمني
6. **التصدير**: احفظ التقرير بصيغة PDF أو Excel أو أرسله بالبريد الإلكتروني

</div>

### Assessment Steps:

1. **Entity Information**: Enter entity name, sector, size, and contact information
2. **Implementation Group Selection**: Choose IG1, IG2, or IG3 based on your entity's size and requirements
3. **Self-Assessment**: Answer key assessment questions for each of the 18 controls
4. **View Results**: Review comprehensive results dashboard with visualizations
5. **Recommendations**: Review prioritized recommendations for security improvement
6. **Export**: Save report as PDF or Excel, or email results

---

## 🎓 Implementation Groups Guide | دليل المجموعات التنفيذية

<div dir="rtl">

### المجموعة التنفيذية 1 (IG1) - النظافة السيبرانية الأساسية
- **الجهات المستهدفة**: المؤسسات الصغيرة والمتوسطة (<500 موظف)
- **الإجراءات الوقائية**: 56 إجراء أساسي
- **التركيز**: النظافة السيبرانية الأساسية والحماية من الهجمات الشائعة
- **الموارد**: محدودة، خبرة أمنية أساسية

### المجموعة التنفيذية 2 (IG2) - الحماية المتقدمة
- **الجهات المستهدفة**: المؤسسات المتوسطة (500-2000 موظف)
- **الإجراءات الوقائية**: 130 إجراء (IG1 + 74 إجراء إضافي)
- **التركيز**: بيئات معقدة، بيانات حساسة، هجمات متطورة
- **الموارد**: موارد معتدلة، فريق أمن مخصص

### المجموعة التنفيذية 3 (IG3) - الأمن الشامل
- **الجهات المستهدفة**: المؤسسات الكبيرة والحساسة (>2000 موظف)
- **الإجراءات الوقائية**: 153 إجراء (جميع الإجراءات)
- **التركيز**: بيانات عالية الحساسية، هجمات موجهة ومتقدمة
- **الموارد**: موارد كبيرة، خبراء أمن متخصصون

</div>

---

## 🏛️ Kuwait Context | السياق الكويتي

<div dir="rtl">

### مواءمة مع الاستراتيجيات الوطنية:

#### رؤية الكويت 2035
- تحول رقمي شامل للخدمات الحكومية
- تعزيز البنية التحتية للأمن السيبراني
- بناء قدرات وطنية في مجال الأمن السيبراني

#### الاستراتيجية الوطنية للأمن السيبراني
- إنشاء المركز الوطني للأمن السيبراني (NCSC) - 2022
- الوصول إلى مستوى نضج 5 في الأمن السيبراني
- استثمار مليار دولار على مدى 5 سنوات

#### إطار البنك المركزي الكويتي (CBK CSF)
- متطلبات خاصة للقطاع المصرفي والمالي
- توافق مع ضوابط CIS للمؤسسات المالية

</div>

---

## 📊 Maturity Levels | مستويات النضج

| Score | Level | المستوى | Description الوصف |
|:---:|---|---|---|
| 0-25% | Initial | أولي | Ad-hoc processes, no formal controls قليل من الضوابط الرسمية |
| 26-50% | Developing | متطور | Some documented processes بعض العمليات الموثقة |
| 51-75% | Defined | محدد | Standardized, documented processes عمليات موحدة وموثقة |
| 76-90% | Managed | مُدار | Measured and monitored controls ضوابط مقاسة ومراقبة |
| 91-100% | Optimized | محسّن | Continuous improvement culture ثقافة التحسين المستمر |

---

## 🛠️ Technical Implementation | التنفيذ التقني

### Technologies Used:
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: CSS Grid, Flexbox, RTL Support
- **Charts**: Chart.js for data visualization
- **PDF Export**: jsPDF with Arabic support
- **Storage**: Client-side JavaScript objects (no localStorage/cookies due to sandbox)

### File Structure:
```
CIS-Kuwait-Assessment/
├── README.md              # This file
├── docs/
│   ├── implementation-guide.csv
|   ├── index.html              # Main application file
│   ├── user-manual-ar.md
│   └── user-manual-en.md
└── assets/
    ├── images/
    └── data/
```

---

## 📚 Resources | المصادر

<div dir="rtl">

### المراجع الأساسية:

1. **البحث الأساسي**: 
   - [رفع مستوى استعدادات الأمن السيبراني في الجهات الحكومية الكويتية](https://www.researchgate.net/publication/384449388)

2. **إطار CIS Controls**:
   - [CIS Controls v8 Official Documentation](https://www.cisecurity.org/controls/v8)
   - [CIS Implementation Groups](https://www.cisecurity.org/controls/implementation-groups)

3. **الاستراتيجية الوطنية**:
   - [Kuwait National Cybersecurity Strategy](https://citra.gov.kw/sites/en/LegalReferences/English%20Cyber%20Security%20Strategy.pdf)
   - [المركز الوطني للأمن السيبراني NCSC](https://ncsc.gov.kw)

4. **أدوات مساعدة**:
   - [CIS CSAT - Self-Assessment Tool](https://www.cisecurity.org/insights/blog/cis-csat-free-tool-assessing-implementation-of-cis-controls)
   - [OpenSCAP - Open Source Security Automation](https://www.open-scap.org)

</div>

---

## 🤝 Contributing | المساهمة

<div dir="rtl">

نرحب بالمساهمات من المجتمع! إذا كنت ترغب في المساهمة:

1. Fork المستودع
2. أنشئ فرع للميزة الجديدة (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add some AmazingFeature'`)
4. Push إلى الفرع (`git push origin feature/AmazingFeature`)
5. افتح Pull Request

</div>

We welcome contributions from the community! Please follow the steps above to contribute.

---

## 📧 Contact | التواصل

**Developer | المطور**: SiteQ8  
**Email | البريد الإلكتروني**: Site@hotmail.com  
**GitHub**: [@SiteQ8](https://github.com/SiteQ8)

<div dir="rtl">

### للدعم والاستفسارات:
- افتح issue في GitHub
- راسلنا على البريد الإلكتروني
- انضم إلى مجتمع الأمن السيبراني الكويتي

</div>

---

## 📄 License | الترخيص

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<div dir="rtl">

هذا المشروع مرخص بموجب ترخيص MIT - انظر ملف الترخيص للتفاصيل.

</div>

---

## 🙏 Acknowledgments | شكر وتقدير

<div dir="rtl">

- **مركز أمان الإنترنت (CIS)** لتطوير وصيانة إطار الضوابط الأمنية
- **الباحثون والمساهمون** في البحث العلمي الأساسي
- **الجهات الحكومية الكويتية** التي قدمت ملاحظات قيمة

</div>

- **Center for Internet Security (CIS)** for developing and maintaining the Controls framework
- **Researchers and contributors** to the foundational research
- **Kuwait government entities** that provided valuable feedback

---

## 🔐 Security Notice | ملاحظة أمنية

<div dir="rtl">

**مهم**: هذه الأداة للتقييم الذاتي فقط. لا تدخل معلومات حساسة أو سرية. البيانات المدخلة تبقى في متصفحك ولا يتم إرسالها إلى أي خادم خارجي.

</div>

**Important**: This tool is for self-assessment only. Do not enter sensitive or classified information. All data remains in your browser and is not transmitted to external servers.

---

## 📅 Roadmap | خارطة الطريق

<div dir="rtl">

### المزايا المستقبلية:
- [ ] تكامل مع أنظمة SIEM
- [ ] API للتكامل مع أدوات أخرى
- [ ] قاعدة بيانات للمقارنات القياسية
- [ ] تقارير متقدمة بالذكاء الاصطناعي
- [ ] تطبيق جوال (iOS & Android)
- [ ] نظام إدارة المخاطر المتكامل

</div>

### Future Features:
- [ ] Integration with SIEM systems
- [ ] API for integration with other tools
- [ ] Benchmark database
- [ ] AI-powered advanced reporting
- [ ] Mobile app (iOS & Android)
- [ ] Integrated risk management system

---

<div align="center" dir="rtl">

### صُنع بـ ❤️ في الكويت | Made with ❤️ in Kuwait

**Version 0.0.1** | Based on CIS Controls v8.1

</div>
