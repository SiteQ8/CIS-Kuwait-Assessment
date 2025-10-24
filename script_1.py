
# Create comprehensive data structure for the CIS Controls assessment tool in YAML format
import yaml

# This will form the complete data backbone for the application

assessment_data = {
    "metadata": {
        "title_ar": "أداة التقييم الذاتي لضوابط إطار CIS",
        "title_en": "CIS Controls Self-Assessment Tool",
        "version": "8.1",
        "target_audience": "الجهات الحكومية الكويتية - Kuwait Government Entities",
        "implementation_groups": {
            "IG1": {
                "name_ar": "المجموعة التنفيذية 1",
                "name_en": "Implementation Group 1",
                "description_ar": "النظافة السيبرانية الأساسية للمؤسسات الصغيرة والمتوسطة",
                "safeguards": 56
            },
            "IG2": {
                "name_ar": "المجموعة التنفيذية 2",
                "name_en": "Implementation Group 2", 
                "description_ar": "ضوابط إضافية للمؤسسات المتوسطة ذات البيانات الحساسة",
                "safeguards": 74
            },
            "IG3": {
                "name_ar": "المجموعة التنفيذية 3",
                "name_en": "Implementation Group 3",
                "description_ar": "ضوابط شاملة للمؤسسات الكبيرة والبيانات عالية الحساسية",
                "safeguards": 23
            }
        }
    },
    
    "controls": [
        {
            "id": "CIS-1",
            "number": 1,
            "name_ar": "جرد ومراقبة أصول المؤسسة",
            "name_en": "Inventory and Control of Enterprise Assets",
            "description_ar": "إدارة جميع الأصول المادية والافتراضية والسحابية لضمان المساءلة والمراقبة والحماية",
            "why_critical_ar": "لا يمكن الدفاع عن ما لا تعرفه. الأصول غير المسجلة تشكل نقاط دخول للمهاجمين",
            "total_safeguards": 5,
            "ig1_safeguards": 4,
            "ig2_safeguards": 1,
            "ig3_safeguards": 0,
            "key_questions_ar": [
                "هل تمتلك جرد محدث لجميع الأجهزة المتصلة بالشبكة؟",
                "هل يتم تحديث سجل الأصول بشكل آلي عند اكتشاف أجهزة جديدة؟",
                "هل تم تصنيف الأصول حسب أهميتها للعمليات؟",
                "هل يتم إزالة الأجهزة غير المصرح بها فوراً؟"
            ]
        },
        {
            "id": "CIS-2",
            "number": 2,
            "name_ar": "جرد ومراقبة الأصول البرمجية",
            "name_en": "Inventory and Control of Software Assets",
            "description_ar": "إدارة جميع البرمجيات لضمان تثبيت وتشغيل البرامج المصرح بها فقط",
            "why_critical_ar": "البرمجيات غير المصرح بها قد تحتوي على ثغرات أمنية أو برامج خبيثة",
            "total_safeguards": 7,
            "ig1_safeguards": 4,
            "ig2_safeguards": 3,
            "ig3_safeguards": 0,
            "key_questions_ar": [
                "هل تمتلك قائمة بجميع البرمجيات المثبتة على الأنظمة؟",
                "هل يتم حظر تثبيت البرمجيات غير المصرح بها؟",
                "هل يتم فحص البرمجيات الجديدة قبل الموافقة عليها؟",
                "هل يتم تحديث سجل البرمجيات المصرح بها بشكل دوري؟"
            ]
        },
        {
            "id": "CIS-3",
            "number": 3,
            "name_ar": "حماية البيانات",
            "name_en": "Data Protection",
            "description_ar": "تطوير إجراءات لتحديد وتصنيف وحماية والتخلص الآمن من البيانات",
            "why_critical_ar": "البيانات هي أثمن أصول المؤسسة ويجب حمايتها من السرقة والتسريب",
            "total_safeguards": 14,
            "ig1_safeguards": 6,
            "ig2_safeguards": 5,
            "ig3_safeguards": 3,
            "key_questions_ar": [
                "هل تم تصنيف البيانات حسب درجة حساسيتها؟",
                "هل يتم تشفير البيانات الحساسة أثناء النقل والتخزين؟",
                "هل توجد سياسات للاحتفاظ بالبيانات والتخلص منها؟",
                "هل يتم تسجيل الوصول إلى البيانات الحساسة؟"
            ]
        },
        {
            "id": "CIS-4",
            "number": 4,
            "name_ar": "التكوين الآمن للأصول والبرمجيات",
            "name_en": "Secure Configuration of Enterprise Assets and Software",
            "description_ar": "إعداد الأصول والبرمجيات وفق معايير أمنية لمنع الاستغلال",
            "why_critical_ar": "الإعدادات الافتراضية غالباً تكون غير آمنة وتسهل اختراق الأنظمة",
            "total_safeguards": 12,
            "ig1_safeguards": 7,
            "ig2_safeguards": 4,
            "ig3_safeguards": 1,
            "key_questions_ar": [
                "هل يتم تطبيق معايير التكوين الآمن على جميع الأنظمة؟",
                "هل يتم تعطيل الخدمات والحسابات غير الضرورية؟",
                "هل يتم مراقبة الانحرافات عن إعدادات الأمان المعتمدة؟",
                "هل توجد عملية لمراجعة واعتماد التكوينات الجديدة؟"
            ]
        },
        {
            "id": "CIS-5",
            "number": 5,
            "name_ar": "إدارة الحسابات",
            "name_en": "Account Management",
            "description_ar": "استخدام عمليات وأدوات لإدارة بيانات اعتماد المستخدمين والحسابات الإدارية",
            "why_critical_ar": "الحسابات غير المدارة بشكل صحيح توفر نقاط دخول سهلة للمهاجمين",
            "total_safeguards": 6,
            "ig1_safeguards": 4,
            "ig2_safeguards": 2,
            "ig3_safeguards": 0,
            "key_questions_ar": [
                "هل يتم تعطيل أو حذف حسابات الموظفين المغادرين فوراً؟",
                "هل يتم مراجعة صلاحيات المستخدمين بشكل دوري؟",
                "هل تطبق سياسات كلمات مرور قوية؟",
                "هل يتم رصد محاولات الوصول المشبوهة للحسابات؟"
            ]
        },
        {
            "id": "CIS-6",
            "number": 6,
            "name_ar": "إدارة التحكم في الوصول",
            "name_en": "Access Control Management",
            "description_ar": "استخدام عمليات وأدوات لإنشاء وتعيين وإدارة الوصول لبيانات الاعتماد",
            "why_critical_ar": "التحكم الضعيف في الوصول يسمح للمهاجمين بالتحرك بحرية داخل الشبكة",
            "total_safeguards": 8,
            "ig1_safeguards": 5,
            "ig2_safeguards": 2,
            "ig3_safeguards": 1,
            "key_questions_ar": [
                "هل يتم تطبيق مبدأ أقل الصلاحيات الضرورية؟",
                "هل يتطلب الوصول للأنظمة الحساسة المصادقة متعددة العوامل؟",
                "هل يتم مراقبة ومراجعة صلاحيات الوصول بانتظام؟",
                "هل توجد ضوابط للوصول عن بعد؟"
            ]
        },
        {
            "id": "CIS-7",
            "number": 7,
            "name_ar": "الإدارة المستمرة للثغرات",
            "name_en": "Continuous Vulnerability Management",
            "description_ar": "تطوير وتنفيذ خطة لتقييم ومعالجة الثغرات الأمنية بشكل مستمر",
            "why_critical_ar": "الثغرات غير المصححة هي الطريقة الأكثر شيوعاً لاختراق الأنظمة",
            "total_safeguards": 7,
            "ig1_safeguards": 4,
            "ig2_safeguards": 3,
            "ig3_safeguards": 0,
            "key_questions_ar": [
                "هل يتم إجراء فحوصات دورية للثغرات الأمنية؟",
                "هل توجد عملية لتحديد أولويات معالجة الثغرات؟",
                "هل يتم تطبيق التحديثات الأمنية في الوقت المناسب؟",
                "هل يتم تتبع ومراقبة حالة معالجة الثغرات؟"
            ]
        },
        {
            "id": "CIS-8",
            "number": 8,
            "name_ar": "إدارة سجلات التدقيق",
            "name_en": "Audit Log Management",
            "description_ar": "جمع وإدارة وتحليل سجلات التدقيق للأحداث للكشف عن التهديدات",
            "why_critical_ar": "بدون سجلات شاملة، يستحيل الكشف عن الهجمات أو التحقيق فيها",
            "total_safeguards": 12,
            "ig1_safeguards": 5,
            "ig2_safeguards": 5,
            "ig3_safeguards": 2,
            "key_questions_ar": [
                "هل يتم تفعيل التسجيل على جميع الأنظمة الحساسة؟",
                "هل يتم حماية سجلات التدقيق من التعديل أو الحذف؟",
                "هل يتم مراجعة السجلات للبحث عن أنشطة مشبوهة؟",
                "هل توجد أدوات لتحليل وربط السجلات؟"
            ]
        },
        {
            "id": "CIS-9",
            "number": 9,
            "name_ar": "حماية البريد الإلكتروني ومتصفح الويب",
            "name_en": "Email and Web Browser Protections",
            "description_ar": "تحسين الحماية والتحكم في الأجهزة والبرامج التي تتعامل مع البيانات الإلكترونية",
            "why_critical_ar": "البريد والويب هما المصدران الرئيسيان للهجمات الإلكترونية",
            "total_safeguards": 7,
            "ig1_safeguards": 5,
            "ig2_safeguards": 2,
            "ig3_safeguards": 0,
            "key_questions_ar": [
                "هل يتم فلترة رسائل البريد الإلكتروني للكشف عن التهديدات؟",
                "هل يتم حظر الروابط والمرفقات الخبيثة؟",
                "هل توجد ضوابط لتصفح الإنترنت الآمن؟",
                "هل يتم تحديث المتصفحات وإضافاتها بانتظام؟"
            ]
        },
        {
            "id": "CIS-10",
            "number": 10,
            "name_ar": "الدفاعات ضد البرمجيات الخبيثة",
            "name_en": "Malware Defenses",
            "description_ar": "التحكم في تثبيت وانتشار وتنفيذ البرامج الخبيثة",
            "why_critical_ar": "البرمجيات الخبيثة هي أداة أساسية للمهاجمين لسرقة البيانات وتعطيل الأنظمة",
            "total_safeguards": 7,
            "ig1_safeguards": 5,
            "ig2_safeguards": 2,
            "ig3_safeguards": 0,
            "key_questions_ar": [
                "هل يتم تثبيت وتحديث برامج مكافحة الفيروسات على جميع الأجهزة؟",
                "هل يتم فحص جميع الملفات الواردة من مصادر خارجية؟",
                "هل توجد أدوات للكشف والاستجابة للبرمجيات الخبيثة المتقدمة؟",
                "هل يتم حظر تنفيذ البرامج من المواقع المشبوهة؟"
            ]
        },
        {
            "id": "CIS-11",
            "number": 11,
            "name_ar": "استعادة البيانات",
            "name_en": "Data Recovery",
            "description_ar": "إنشاء والحفاظ على عمليات آمنة لاستعادة البيانات",
            "why_critical_ar": "القدرة على استعادة البيانات ضرورية للتعافي من الحوادث الأمنية",
            "total_safeguards": 5,
            "ig1_safeguards": 4,
            "ig2_safeguards": 1,
            "ig3_safeguards": 0,
            "key_questions_ar": [
                "هل يتم إجراء نسخ احتياطي دوري للبيانات الحساسة؟",
                "هل يتم تخزين النسخ الاحتياطية في مواقع منفصلة؟",
                "هل يتم اختبار عملية استعادة البيانات بانتظام؟",
                "هل النسخ الاحتياطية محمية من التشفير الخبيث؟"
            ]
        },
        {
            "id": "CIS-12",
            "number": 12,
            "name_ar": "إدارة البنية التحتية للشبكة",
            "name_en": "Network Infrastructure Management",
            "description_ar": "إنشاء وتنفيذ والحفاظ على الإدارة الآمنة للبنية التحتية",
            "why_critical_ar": "الشبكة غير المدارة بشكل صحيح توفر مسارات سهلة للمهاجمين",
            "total_safeguards": 8,
            "ig1_safeguards": 4,
            "ig2_safeguards": 3,
            "ig3_safeguards": 1,
            "key_questions_ar": [
                "هل يتم تقسيم الشبكة حسب الوظيفة والحساسية؟",
                "هل توجد جدران نارية لحماية حدود الشبكة؟",
                "هل يتم تأمين أجهزة الشبكة بكلمات مرور قوية وتحديثات؟",
                "هل يتم مراقبة حركة المرور الشبكية للأنشطة المشبوهة؟"
            ]
        },
        {
            "id": "CIS-13",
            "number": 13,
            "name_ar": "مراقبة الشبكة والدفاع عنها",
            "name_en": "Network Monitoring and Defense",
            "description_ar": "تشغيل العمليات والأدوات لإنشاء حدود دفاعية للكشف عن التهديدات",
            "why_critical_ar": "الكشف المبكر عن التهديدات يحد من الضرر الناتج عن الهجمات",
            "total_safeguards": 11,
            "ig1_safeguards": 3,
            "ig2_safeguards": 5,
            "ig3_safeguards": 3,
            "key_questions_ar": [
                "هل توجد أنظمة للكشف عن التسلل؟",
                "هل يتم مراقبة الشبكة على مدار الساعة؟",
                "هل توجد قدرات لتحليل حركة المرور المشفرة؟",
                "هل يتم الاستجابة السريعة للتنبيهات الأمنية؟"
            ]
        },
        {
            "id": "CIS-14",
            "number": 14,
            "name_ar": "التوعية الأمنية والتدريب على المهارات",
            "name_en": "Security Awareness and Skills Training",
            "description_ar": "إنشاء وصيانة برنامج توعية أمنية لكل الموظفين",
            "why_critical_ar": "الخطأ البشري هو السبب الأكثر شيوعاً للاختراقات الأمنية",
            "total_safeguards": 9,
            "ig1_safeguards": 5,
            "ig2_safeguards": 4,
            "ig3_safeguards": 0,
            "key_questions_ar": [
                "هل يتلقى جميع الموظفين تدريباً أمنياً دورياً؟",
                "هل يتم اختبار وعي الموظفين من خلال تمارين محاكاة؟",
                "هل التدريب يغطي التهديدات الحديثة مثل التصيد؟",
                "هل يتم قياس فعالية برامج التوعية؟"
            ]
        },
        {
            "id": "CIS-15",
            "number": 15,
            "name_ar": "إدارة مقدمي الخدمات",
            "name_en": "Service Provider Management",
            "description_ar": "تطوير عملية لتقييم ومراقبة الأمن لمقدمي الخدمات الخارجيين",
            "why_critical_ar": "الجهات الخارجية قد تكون نقطة ضعف إذا لم يتم إدارتها بشكل صحيح",
            "total_safeguards": 7,
            "ig1_safeguards": 3,
            "ig2_safeguards": 3,
            "ig3_safeguards": 1,
            "key_questions_ar": [
                "هل يتم تقييم الأمن السيبراني لمقدمي الخدمات قبل التعاقد؟",
                "هل توجد بنود أمنية في العقود مع الجهات الخارجية؟",
                "هل يتم مراقبة امتثال مقدمي الخدمات للمتطلبات الأمنية؟",
                "هل يتم مراجعة الوصول الممنوح للجهات الخارجية بانتظام؟"
            ]
        },
        {
            "id": "CIS-16",
            "number": 16,
            "name_ar": "أمن البرمجيات التطبيقية",
            "name_en": "Application Software Security",
            "description_ar": "إدارة أمن البرمجيات طوال دورة حياتها",
            "why_critical_ar": "التطبيقات غير الآمنة هي هدف رئيسي للمهاجمين",
            "total_safeguards": 14,
            "ig1_safeguards": 3,
            "ig2_safeguards": 7,
            "ig3_safeguards": 4,
            "key_questions_ar": [
                "هل يتم دمج الأمن في عملية تطوير البرمجيات؟",
                "هل يتم فحص التطبيقات للثغرات قبل النشر؟",
                "هل يتم تدريب المطورين على البرمجة الآمنة؟",
                "هل يتم إدارة وتحديث مكتبات الطرف الثالث؟"
            ]
        },
        {
            "id": "CIS-17",
            "number": 17,
            "name_ar": "إدارة الاستجابة للحوادث",
            "name_en": "Incident Response Management",
            "description_ar": "إنشاء وصيانة برنامج للاستجابة للحوادث الأمنية",
            "why_critical_ar": "الاستجابة السريعة والفعالة تحد من تأثير الحوادث الأمنية",
            "total_safeguards": 9,
            "ig1_safeguards": 4,
            "ig2_safeguards": 4,
            "ig3_safeguards": 1,
            "key_questions_ar": [
                "هل توجد خطة موثقة للاستجابة للحوادث؟",
                "هل يوجد فريق مخصص للاستجابة للحوادث الأمنية؟",
                "هل يتم إجراء تمارين دورية للاستجابة للحوادث؟",
                "هل يتم توثيق وتحليل الحوادث للتعلم منها؟"
            ]
        },
        {
            "id": "CIS-18",
            "number": 18,
            "name_ar": "اختبار الاختراق",
            "name_en": "Penetration Testing",
            "description_ar": "اختبار فعالية دفاعات المؤسسة من خلال محاكاة هجمات حقيقية",
            "why_critical_ar": "اختبار الاختراق يكشف الثغرات قبل أن يستغلها المهاجمون",
            "total_safeguards": 5,
            "ig1_safeguards": 0,
            "ig2_safeguards": 2,
            "ig3_safeguards": 3,
            "key_questions_ar": [
                "هل يتم إجراء اختبارات اختراق دورية؟",
                "هل تغطي الاختبارات جميع الأنظمة والشبكات الحساسة؟",
                "هل يتم معالجة الثغرات المكتشفة من الاختبارات؟",
                "هل يتم إجراء اختبارات من قبل جهات مستقلة؟"
            ]
        }
    ]
}

# Convert to YAML for the application
yaml_data = yaml.dump(assessment_data, allow_unicode=True, sort_keys=False, default_flow_style=False)

# Save to check size
print(f"Generated YAML data structure with {len(assessment_data['controls'])} controls")
print(f"Total size: {len(yaml_data)} characters")
print("\nFirst control sample:")
print(f"Control {assessment_data['controls'][0]['number']}: {assessment_data['controls'][0]['name_ar']}")
print(f"  - Safeguards: {assessment_data['controls'][0]['total_safeguards']}")
print(f"  - Questions: {len(assessment_data['controls'][0]['key_questions_ar'])}")
