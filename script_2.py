
# Create a comprehensive implementation guide CSV for GitHub repository
import csv
import io

implementation_guide_data = [
    ["Control ID", "Control Name (Arabic)", "Control Name (English)", "Total Safeguards", "IG1", "IG2", "IG3", "Priority", "Estimated Cost", "Implementation Time", "Key Tools Required"],
    ["CIS-1", "جرد ومراقبة أصول المؤسسة", "Inventory and Control of Enterprise Assets", "5", "4", "1", "0", "Critical", "Medium", "2-4 weeks", "Asset Discovery Tools, CMDB"],
    ["CIS-2", "جرد ومراقبة الأصول البرمجية", "Inventory and Control of Software Assets", "7", "4", "3", "0", "Critical", "Medium", "2-4 weeks", "Software Inventory Tools, Application Control"],
    ["CIS-3", "حماية البيانات", "Data Protection", "14", "6", "5", "3", "Critical", "High", "3-6 months", "DLP, Encryption Tools, Classification Tools"],
    ["CIS-4", "التكوين الآمن للأصول والبرمجيات", "Secure Configuration of Enterprise Assets and Software", "12", "7", "4", "1", "High", "Medium", "1-3 months", "Configuration Management, CIS-CAT"],
    ["CIS-5", "إدارة الحسابات", "Account Management", "6", "4", "2", "0", "High", "Low", "2-4 weeks", "IAM Solutions, Password Management"],
    ["CIS-6", "إدارة التحكم في الوصول", "Access Control Management", "8", "5", "2", "1", "High", "Medium", "1-2 months", "MFA, PAM, Access Management"],
    ["CIS-7", "الإدارة المستمرة للثغرات", "Continuous Vulnerability Management", "7", "4", "3", "0", "Critical", "Medium", "Ongoing", "Vulnerability Scanners, Patch Management"],
    ["CIS-8", "إدارة سجلات التدقيق", "Audit Log Management", "12", "5", "5", "2", "High", "Medium-High", "2-4 months", "SIEM, Log Management"],
    ["CIS-9", "حماية البريد الإلكتروني ومتصفح الويب", "Email and Web Browser Protections", "7", "5", "2", "0", "High", "Medium", "1-2 months", "Email Gateway, Web Filter"],
    ["CIS-10", "الدفاعات ضد البرمجيات الخبيثة", "Malware Defenses", "7", "5", "2", "0", "Critical", "Medium", "2-4 weeks", "Antivirus, EDR, Anti-malware"],
    ["CIS-11", "استعادة البيانات", "Data Recovery", "5", "4", "1", "0", "Critical", "Medium", "1-2 months", "Backup Solutions, DR Tools"],
    ["CIS-12", "إدارة البنية التحتية للشبكة", "Network Infrastructure Management", "8", "4", "3", "1", "High", "High", "2-4 months", "Network Segmentation, Firewalls"],
    ["CIS-13", "مراقبة الشبكة والدفاع عنها", "Network Monitoring and Defense", "11", "3", "5", "3", "High", "High", "3-6 months", "IDS/IPS, Network Monitoring"],
    ["CIS-14", "التوعية الأمنية والتدريب على المهارات", "Security Awareness and Skills Training", "9", "5", "4", "0", "High", "Low-Medium", "Ongoing", "Training Platform, Phishing Simulation"],
    ["CIS-15", "إدارة مقدمي الخدمات", "Service Provider Management", "7", "3", "3", "1", "Medium", "Low", "1-2 months", "Vendor Assessment Tools, Contracts"],
    ["CIS-16", "أمن البرمجيات التطبيقية", "Application Software Security", "14", "3", "7", "4", "High", "High", "3-6 months", "SAST, DAST, Secure Development"],
    ["CIS-17", "إدارة الاستجابة للحوادث", "Incident Response Management", "9", "4", "4", "1", "Critical", "Medium", "2-3 months", "IR Platform, Forensics Tools"],
    ["CIS-18", "اختبار الاختراق", "Penetration Testing", "5", "0", "2", "3", "Medium-High", "High", "Quarterly", "Pentest Tools, External Consultants"]
]

# Save to CSV
csv_output = io.StringIO()
writer = csv.writer(csv_output)
writer.writerows(implementation_guide_data)

print("CIS Controls Implementation Guide")
print("=" * 100)
print("\nThis CSV provides a comprehensive roadmap for Kuwait government entities to implement CIS Controls")
print(f"\nTotal Controls: 18")
print(f"Total Rows: {len(implementation_guide_data)}")
print("\nColumns: Control ID, Arabic Name, English Name, Safeguards, IG Distribution, Priority, Cost, Time, Tools")
print("\nSample data (first 3 controls):")
for i, row in enumerate(implementation_guide_data[:4]):
    print(row)

# Save the CSV content
csv_content = csv_output.getvalue()
print(f"\n\nCSV file ready for GitHub repository (SiteQ8/CIS-Kuwait-Assessment)")
print(f"File size: {len(csv_content)} bytes")
