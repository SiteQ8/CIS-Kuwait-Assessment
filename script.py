
# Let me create a comprehensive structure for the CIS Benchmark Compliance Checker tool
# This will outline the technical specifications and implementation details

cis_controls_v8 = {
    "Control 1": {
        "name_en": "Inventory and Control of Enterprise Assets",
        "name_ar": "جرد ومراقبة أصول المؤسسة",
        "safeguards": 5,
        "ig1": 4,
        "ig2": 1,
        "ig3": 0
    },
    "Control 2": {
        "name_en": "Inventory and Control of Software Assets",
        "name_ar": "جرد ومراقبة الأصول البرمجية",
        "safeguards": 7,
        "ig1": 4,
        "ig2": 3,
        "ig3": 0
    },
    "Control 3": {
        "name_en": "Data Protection",
        "name_ar": "حماية البيانات",
        "safeguards": 14,
        "ig1": 6,
        "ig2": 5,
        "ig3": 3
    },
    "Control 4": {
        "name_en": "Secure Configuration of Enterprise Assets and Software",
        "name_ar": "التكوين الآمن للأصول والبرمجيات",
        "safeguards": 12,
        "ig1": 7,
        "ig2": 4,
        "ig3": 1
    },
    "Control 5": {
        "name_en": "Account Management",
        "name_ar": "إدارة الحسابات",
        "safeguards": 6,
        "ig1": 4,
        "ig2": 2,
        "ig3": 0
    },
    "Control 6": {
        "name_en": "Access Control Management",
        "name_ar": "إدارة التحكم في الوصول",
        "safeguards": 8,
        "ig1": 5,
        "ig2": 2,
        "ig3": 1
    },
    "Control 7": {
        "name_en": "Continuous Vulnerability Management",
        "name_ar": "الإدارة المستمرة للثغرات",
        "safeguards": 7,
        "ig1": 4,
        "ig2": 3,
        "ig3": 0
    },
    "Control 8": {
        "name_en": "Audit Log Management",
        "name_ar": "إدارة سجلات التدقيق",
        "safeguards": 12,
        "ig1": 5,
        "ig2": 5,
        "ig3": 2
    },
    "Control 9": {
        "name_en": "Email and Web Browser Protections",
        "name_ar": "حماية البريد الإلكتروني ومتصفح الويب",
        "safeguards": 7,
        "ig1": 5,
        "ig2": 2,
        "ig3": 0
    },
    "Control 10": {
        "name_en": "Malware Defenses",
        "name_ar": "الدفاعات ضد البرمجيات الخبيثة",
        "safeguards": 7,
        "ig1": 5,
        "ig2": 2,
        "ig3": 0
    },
    "Control 11": {
        "name_en": "Data Recovery",
        "name_ar": "استعادة البيانات",
        "safeguards": 5,
        "ig1": 4,
        "ig2": 1,
        "ig3": 0
    },
    "Control 12": {
        "name_en": "Network Infrastructure Management",
        "name_ar": "إدارة البنية التحتية للشبكة",
        "safeguards": 8,
        "ig1": 4,
        "ig2": 3,
        "ig3": 1
    },
    "Control 13": {
        "name_en": "Network Monitoring and Defense",
        "name_ar": "مراقبة الشبكة والدفاع عنها",
        "safeguards": 11,
        "ig1": 3,
        "ig2": 5,
        "ig3": 3
    },
    "Control 14": {
        "name_en": "Security Awareness and Skills Training",
        "name_ar": "التوعية الأمنية والتدريب على المهارات",
        "safeguards": 9,
        "ig1": 5,
        "ig2": 4,
        "ig3": 0
    },
    "Control 15": {
        "name_en": "Service Provider Management",
        "name_ar": "إدارة مقدمي الخدمات",
        "safeguards": 7,
        "ig1": 3,
        "ig2": 3,
        "ig3": 1
    },
    "Control 16": {
        "name_en": "Application Software Security",
        "name_ar": "أمن البرمجيات التطبيقية",
        "safeguards": 14,
        "ig1": 3,
        "ig2": 7,
        "ig3": 4
    },
    "Control 17": {
        "name_en": "Incident Response Management",
        "name_ar": "إدارة الاستجابة للحوادث",
        "safeguards": 9,
        "ig1": 4,
        "ig2": 4,
        "ig3": 1
    },
    "Control 18": {
        "name_en": "Penetration Testing",
        "name_ar": "اختبار الاختراق",
        "safeguards": 5,
        "ig1": 0,
        "ig2": 2,
        "ig3": 3
    }
}

# Calculate totals
total_safeguards = sum(control["safeguards"] for control in cis_controls_v8.values())
total_ig1 = sum(control["ig1"] for control in cis_controls_v8.values())
total_ig2 = sum(control["ig2"] for control in cis_controls_v8.values())
total_ig3 = sum(control["ig3"] for control in cis_controls_v8.values())

print("CIS Controls v8 Overview")
print("=" * 60)
print(f"Total Controls: 18")
print(f"Total Safeguards: {total_safeguards}")
print(f"IG1 Safeguards: {total_ig1}")
print(f"IG2 Safeguards: {total_ig2} (cumulative with IG1: {total_ig1 + total_ig2})")
print(f"IG3 Safeguards: {total_ig3} (cumulative total: {total_safeguards})")
print("\n")

# Create detailed breakdown for the tool
import pandas as pd

controls_data = []
for control_id, control_info in cis_controls_v8.items():
    controls_data.append({
        "Control ID": control_id,
        "English Name": control_info["name_en"],
        "Arabic Name": control_info["name_ar"],
        "Total Safeguards": control_info["safeguards"],
        "IG1": control_info["ig1"],
        "IG2": control_info["ig2"],
        "IG3": control_info["ig3"]
    })

df = pd.DataFrame(controls_data)
print(df.to_string(index=False))
print("\n")
print("This structure forms the foundation for the CIS Benchmark Compliance Checker tool")
