from dataclasses import dataclass
from typing import List


@dataclass
class Doctor:
    name: str
    age: int
    sex: str
    specialisation: str
    degrees: List[str]
    hospital: str
    email: str
    phone: str
    booking_url: str


DOCTORS: List[Doctor] = [
    # Evercare Hospital Dhaka (45 doctors)
    Doctor("Dr. Ayesha Siddiqua", 38, "Female", "Dermatologist", [
           "MBBS", "MD", "FCPS"], "Evercare Hospital Dhaka", "ayesha.siddiqua@evercare.com", "+8801711001001", "https://booking.evercare.com/ayeshasiddiqua"),
    Doctor("Dr. Kamal Hossain", 50, "Male", "Neurologist", ["MBBS", "FCPS", "PhD"], "Evercare Hospital Dhaka",
           "kamal.hossain@evercare.com", "+8801711001002", "https://booking.evercare.com/kamalhossain"),
    Doctor("Dr. Nusrat Jahan", 42, "Female", "Gynecologist", [
           "MBBS", "FCPS", "DGO"], "Evercare Hospital Dhaka", "nusrat.jahan@evercare.com", "+8801711001003", "https://booking.evercare.com/nusratjahan"),
    Doctor("Dr. Imran Kabir", 35, "Male", "Pediatrician", [
           "MBBS", "MD"], "Evercare Hospital Dhaka", "imran.kabir@evercare.com", "+8801711001004", "https://booking.evercare.com/imrankabir"),
    Doctor("Dr. Maliha Rahman", 47, "Female", "Oncologist", [
           "MBBS", "FCPS", "MRCP"], "Evercare Hospital Dhaka", "maliha.rahman@evercare.com", "+8801711001005", "https://booking.evercare.com/maliharahman"),
    Doctor("Dr. Rashid Alam", 55, "Male", "Orthopedic Surgeon", [
           "MBBS", "MS"], "Evercare Hospital Dhaka", "rashid.alam@evercare.com", "+8801711001006", "https://booking.evercare.com/rashidalam"),
    Doctor("Dr. Farzana Haque", 41, "Female", "Psychiatrist", [
           "MBBS", "FCPS", "MPhil"], "Evercare Hospital Dhaka", "farzana.haque@evercare.com", "+8801711001007", "https://booking.evercare.com/farzanahaque"),
    Doctor("Dr. Shafiq Ahmed", 60, "Male", "ENT Specialist", [
           "MBBS", "DLO"], "Evercare Hospital Dhaka", "shafiq.ahmed@evercare.com", "+8801711001008", "https://booking.evercare.com/shafiqahmed"),
    Doctor("Dr. Tahmina Begum", 36, "Female", "General Physician", [
           "MBBS"], "Evercare Hospital Dhaka", "tahmina.begum@evercare.com", "+8801711001009", "https://booking.evercare.com/tahminabegum"),
    Doctor("Dr. Sajid Chowdhury", 48, "Male", "Cardiologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "sajid.chowdhury@evercare.com", "+8801711001010", "https://booking.evercare.com/sajidchowdhury"),
    Doctor("Dr. Fahmida Begum", 45, "Female", "Endocrinologist", [
           "MBBS", "MD", "FCPS"], "Evercare Hospital Dhaka", "fahmida.begum@evercare.com", "+8801711001011", "https://booking.evercare.com/fahmidabegum"),
    Doctor("Dr. Sohel Rana", 39, "Male", "Gastroenterologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "sohel.rana@evercare.com", "+8801711001012", "https://booking.evercare.com/sohelrana"),
    Doctor("Dr. Yasmin Akter", 44, "Female", "Rheumatologist", [
           "MBBS", "MD"], "Evercare Hospital Dhaka", "yasmin.akter@evercare.com", "+8801711001013", "https://booking.evercare.com/yasminakter"),
    Doctor("Dr. Iqbal Hossain", 52, "Male", "Urologist", ["MBBS", "MS"], "Evercare Hospital Dhaka",
           "iqbal.hossain@evercare.com", "+8801711001014", "https://booking.evercare.com/iqbalhossain"),
    Doctor("Dr. Nazma Sultana", 36, "Female", "Dermatologist", [
           "MBBS", "DDV"], "Evercare Hospital Dhaka", "nazma.sultana@evercare.com", "+8801711001015", "https://booking.evercare.com/nazmasultana"),
    Doctor("Dr. Asaduzzaman Khan", 47, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "Evercare Hospital Dhaka", "asad.khan@evercare.com", "+8801711001016", "https://booking.evercare.com/asadkhan"),
    Doctor("Dr. Rehana Parvin", 41, "Female", "Nephrologist", [
           "MBBS", "MD"], "Evercare Hospital Dhaka", "rehana.parvin@evercare.com", "+8801711001017", "https://booking.evercare.com/rehanaparvin"),
    Doctor("Dr. Shahidul Alam", 53, "Male", "Plastic Surgeon", [
           "MBBS", "MS"], "Evercare Hospital Dhaka", "shahidul.alam@evercare.com", "+8801711001018", "https://booking.evercare.com/shahidulalam"),
    Doctor("Dr. Farida Yasmin", 38, "Female", "Hematologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "farida.yasmin@evercare.com", "+8801711001019", "https://booking.evercare.com/faridayasmin"),
    Doctor("Dr. Zakir Hossain", 49, "Male", "Pulmonologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "zakir.hossain@evercare.com", "+8801711001020", "https://booking.evercare.com/zakirhossain"),
    Doctor("Dr. Selina Akter", 35, "Female", "Family Physician", [
           "MBBS"], "Evercare Hospital Dhaka", "selina.akter@evercare.com", "+8801711001021", "https://booking.evercare.com/selinaakter"),
    Doctor("Dr. Anwarul Karim", 57, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS", "PhD"], "Evercare Hospital Dhaka", "anwar.karim@evercare.com", "+8801711001022", "https://booking.evercare.com/anwarkarim"),
    Doctor("Dr. Moushumi Rahman", 40, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "moushumi.rahman@evercare.com", "+8801711001023", "https://booking.evercare.com/moushumirahman"),
    Doctor("Dr. Jamal Uddin", 46, "Male", "Emergency Medicine", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "jamal.uddin@evercare.com", "+8801711001024", "https://booking.evercare.com/jamaluddin"),
    Doctor("Dr. Sharmin Sultana", 33, "Female", "General Surgeon", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "sharmin.sultana@evercare.com", "+8801711001025", "https://booking.evercare.com/sharminsultana"),
    Doctor("Dr. Rafiqul Islam", 51, "Male", "Interventional Cardiologist", [
           "MBBS", "FCPS", "FACC"], "Evercare Hospital Dhaka", "rafiq.islam@evercare.com", "+8801711001026", "https://booking.evercare.com/rafiqislam"),
    Doctor("Dr. Nasima Begum", 43, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "nasima.begum@evercare.com", "+8801711001027", "https://booking.evercare.com/nasimabegum"),
    Doctor("Dr. Tareq Ahmed", 39, "Male", "Spine Surgeon", [
           "MBBS", "MS"], "Evercare Hospital Dhaka", "tareq.ahmed@evercare.com", "+8801711001028", "https://booking.evercare.com/tareqahmed"),
    Doctor("Dr. Laila Arjumand", 45, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "laila.arjumand@evercare.com", "+8801711001029", "https://booking.evercare.com/lailaarjumand"),
    Doctor("Dr. Sazzad Hossain", 48, "Male", "Neurophysician", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "sazzad.hossain@evercare.com", "+8801711001030", "https://booking.evercare.com/sazzadhossain"),
    Doctor("Dr. Farhana Islam", 36, "Female", "Diabetologist", [
           "MBBS", "MD"], "Evercare Hospital Dhaka", "farhana.islam@evercare.com", "+8801711001031", "https://booking.evercare.com/farhanaislam"),
    Doctor("Dr. Ashraf Uddin", 54, "Male", "Hepatologist", [
           "MBBS", "FCPS", "FRCP"], "Evercare Hospital Dhaka", "ashraf.uddin@evercare.com", "+8801711001032", "https://booking.evercare.com/ashrafuddin"),
    Doctor("Dr. Nargis Akhtar", 41, "Female", "Pain Medicine", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "nargis.akhtar@evercare.com", "+8801711001033", "https://booking.evercare.com/nargisakhtar"),
    Doctor("Dr. Kamal Uddin", 47, "Male", "Vascular Surgeon", [
           "MBBS", "MS", "FCPS"], "Evercare Hospital Dhaka", "kamal.uddin@evercare.com", "+8801711001034", "https://booking.evercare.com/kamaluddin"),
    Doctor("Dr. Shireen Banu", 34, "Female", "Infectious Disease", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "shireen.banu@evercare.com", "+8801711001035", "https://booking.evercare.com/shireenbanu"),
    Doctor("Dr. Arman Chowdhury", 50, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "Evercare Hospital Dhaka", "arman.chowdhury@evercare.com", "+8801711001036", "https://booking.evercare.com/armanchowdhury"),
    Doctor("Dr. Sabina Yasmin", 42, "Female", "Critical Care", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "sabina.yasmin@evercare.com", "+8801711001037", "https://booking.evercare.com/sabinayasmin"),
    Doctor("Dr. Rashed Khan", 56, "Male", "Hand Surgeon", [
           "MBBS", "MS", "FRCS"], "Evercare Hospital Dhaka", "rashed.khan@evercare.com", "+8801711001038", "https://booking.evercare.com/rashedkhan"),
    Doctor("Dr. Tahmina Rahman", 37, "Female", "Allergist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "tahmina.rahman@evercare.com", "+8801711001039", "https://booking.evercare.com/tahminarahman"),
    Doctor("Dr. Saiful Islam", 44, "Male", "Sleep Medicine", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "saiful.islam@evercare.com", "+8801711001040", "https://booking.evercare.com/saifulislam"),
    Doctor("Dr. Naznin Sultana", 32, "Female", "Reproductive Endocrinologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "naznin.sultana@evercare.com", "+8801711001041", "https://booking.evercare.com/nazninsultana"),
    Doctor("Dr. Azharul Haque", 58, "Male", "Geriatrician", [
           "MBBS", "MD"], "Evercare Hospital Dhaka", "azhar.haque@evercare.com", "+8801711001042", "https://booking.evercare.com/azharhaque"),
    Doctor("Dr. Munira Akter", 40, "Female", "Pediatric Cardiologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "munira.akter@evercare.com", "+8801711001043", "https://booking.evercare.com/muniraakter"),
    Doctor("Dr. Jahangir Alam", 45, "Male", "Interventional Radiologist", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "jahangir.alam@evercare.com", "+8801711001044", "https://booking.evercare.com/jahangiralam"),
    Doctor("Dr. Shabnam Begum", 38, "Female", "Breast Surgeon", [
           "MBBS", "FCPS"], "Evercare Hospital Dhaka", "shabnam.begum@evercare.com", "+8801711001045", "https://booking.evercare.com/shabnambegum"),

    # United Hospital Limited (45 doctors)
    Doctor("Dr. Mahmudul Hasan", 49, "Male", "Cardiologist", [
           "MBBS", "FCPS", "FSCAI"], "United Hospital Limited", "mahmudul.hasan@united.com", "+8801811002001", "https://booking.united.com/mahmudulhasan"),
    Doctor("Dr. Feroza Khatun", 43, "Female", "Pediatrician", [
           "MBBS", "FCPS"], "United Hospital Limited", "feroza.khatun@united.com", "+8801811002002", "https://booking.united.com/ferozakhatun"),
    Doctor("Dr. Sajjad Hossain", 52, "Male", "Neurologist", [
           "MBBS", "MS", "FRCS"], "United Hospital Limited", "sajjad.hossain@united.com", "+8801811002003", "https://booking.united.com/sajjadhossain"),
    Doctor("Dr. Nusrat Jahan", 41, "Female", "Gynecologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "nusrat.jahan@united.com", "+8801811002004", "https://booking.united.com/nusratjahan"),
    Doctor("Dr. Asif Iqbal", 47, "Male", "Orthopedic Surgeon", [
           "MBBS", "FCPS"], "United Hospital Limited", "asif.iqbal@united.com", "+8801811002005", "https://booking.united.com/asifiqbal"),
    Doctor("Dr. Salma Akter", 35, "Female", "Dermatologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "salma.akter@united.com", "+8801811002006", "https://booking.united.com/salmaakter"),
    Doctor("Dr. Ruhul Amin", 53, "Male", "General Surgeon", [
           "MBBS", "FCPS", "FRCP"], "United Hospital Limited", "ruhul.amin@united.com", "+8801811002007", "https://booking.united.com/ruhulamin"),
    Doctor("Dr. Sharmin Akter", 39, "Female", "ENT Specialist", [
           "MBBS", "FCPS"], "United Hospital Limited", "sharmin.akter@united.com", "+8801811002008", "https://booking.united.com/sharminakter"),
    Doctor("Dr. Mizanur Rahman", 46, "Male", "Urologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "mizan.rahman@united.com", "+8801811002009", "https://booking.united.com/mizanrahman"),
    Doctor("Dr. Sonia Begum", 33, "Female", "Psychiatrist", [
           "MBBS", "MD"], "United Hospital Limited", "sonia.begum@united.com", "+8801811002010", "https://booking.united.com/soniabegum"),
    Doctor("Dr. Aminul Islam", 50, "Male", "Gastroenterologist", [
           "MBBS", "FCPS", "FHRS"], "United Hospital Limited", "aminul.islam@united.com", "+8801811002011", "https://booking.united.com/aminulislam"),
    Doctor("Dr. Rahela Banu", 44, "Female", "Endocrinologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "rahela.banu@united.com", "+8801811002012", "https://booking.united.com/rahelabanu"),
    Doctor("Dr. Shahriar Ahmed", 57, "Male", "Oncologist", [
           "MBBS", "FCPS", "FRCS"], "United Hospital Limited", "shahriar.ahmed@united.com", "+8801811002013", "https://booking.united.com/shahriarahmed"),
    Doctor("Dr. Farzana Islam", 40, "Female", "Pulmonologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "farzana.islam@united.com", "+8801811002014", "https://booking.united.com/farzanaislam"),
    Doctor("Dr. Zakaria Hossain", 48, "Male", "Nephrologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "zakaria.hossain@united.com", "+8801811002015", "https://booking.united.com/zakariahossain"),
    Doctor("Dr. Nazia Hasan", 36, "Female", "Rheumatologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "nazia.hasan@united.com", "+8801811002016", "https://booking.united.com/naziahasan"),
    Doctor("Dr. Sadek Ahmed", 51, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS", "FACS"], "United Hospital Limited", "sadek.ahmed@united.com", "+8801811002017", "https://booking.united.com/sadekahmed"),
    Doctor("Dr. Rubina Akter", 42, "Female", "Hematologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "rubina.akter@united.com", "+8801811002018", "https://booking.united.com/rubinaakter"),
    Doctor("Dr. Mahfuzur Rahman", 47, "Male", "Plastic Surgeon", [
           "MBBS", "FCPS", "FCCM"], "United Hospital Limited", "mahfuz.rahman@united.com", "+8801811002019", "https://booking.united.com/mahfuzrahman"),
    Doctor("Dr. Shabnaz Begum", 34, "Female", "Emergency Medicine", [
           "MBBS", "FCPS"], "United Hospital Limited", "shabnaz.begum@united.com", "+8801811002020", "https://booking.united.com/shabnazbegum"),
    Doctor("Dr. Anisur Rahman", 49, "Male", "General Physician", [
           "MBBS", "FCPS", "FRCS"], "United Hospital Limited", "anis.rahman@united.com", "+8801811002021", "https://booking.united.com/anisrahman"),
    Doctor("Dr. Nasima Sultana", 43, "Female", "Family Medicine", [
           "MBBS", "PhD"], "United Hospital Limited", "nasima.sultana@united.com", "+8801811002022", "https://booking.united.com/nasimasultana"),
    Doctor("Dr. Harunur Rashid", 54, "Male", "Interventional Cardiologist", [
           "MBBS", "MD"], "United Hospital Limited", "harun.rashid@united.com", "+8801811002023", "https://booking.united.com/harunrashid"),
    Doctor("Dr. Jesmin Akter", 37, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "jesmin.akter@united.com", "+8801811002024", "https://booking.united.com/jesminakter"),
    Doctor("Dr. Moniruzzaman Khan", 45, "Male", "Spine Surgeon", [
           "MBBS", "FCPS"], "United Hospital Limited", "monir.khan@united.com", "+8801811002025", "https://booking.united.com/monirkhan"),
    Doctor("Dr. Sharmin Islam", 39, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "sharmin.islam@united.com", "+8801811002026", "https://booking.united.com/sharminislam"),
    Doctor("Dr. Abdur Rahim", 52, "Male", "Hepatologist", [
           "MBBS", "FCPS", "FRCS"], "United Hospital Limited", "abdur.rahim@united.com", "+8801811002027", "https://booking.united.com/abdurrahim"),
    Doctor("Dr. Fahmida Sultana", 41, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "fahmida.sultana@united.com", "+8801811002028", "https://booking.united.com/fahmidasultana"),
    Doctor("Dr. Nurul Haque", 46, "Male", "Vascular Surgeon", [
           "MBBS", "FCPS"], "United Hospital Limited", "nurul.haque@united.com", "+8801811002029", "https://booking.united.com/nurulhaque"),
    Doctor("Dr. Sabiha Chowdhury", 33, "Female", "Infectious Disease", [
           "MBBS", "DTM&H"], "United Hospital Limited", "sabiha.chowdhury@united.com", "+8801811002030", "https://booking.united.com/sabihachowdhury"),
    Doctor("Dr. Kamrul Hasan", 50, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "United Hospital Limited", "kamrul.hasan@united.com", "+8801811002031", "https://booking.united.com/kamrulhasan"),
    Doctor("Dr. Nasreen Akter", 44, "Female", "Critical Care", [
           "MBBS", "FCPS"], "United Hospital Limited", "nasreen.akter@united.com", "+8801811002032", "https://booking.united.com/nasreenakter"),
    Doctor("Dr. Shahjahan Ali", 55, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS", "FRCS"], "United Hospital Limited", "shahjahan.ali@united.com", "+8801811002033", "https://booking.united.com/shahjahanali"),
    Doctor("Dr. Mita Rahman", 38, "Female", "Diabetologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "mita.rahman@united.com", "+8801811002034", "https://booking.united.com/mitarahman"),
    Doctor("Dr. Asad Ali", 47, "Male", "Pain Medicine", [
           "MBBS", "FCPS"], "United Hospital Limited", "asad.ali@united.com", "+8801811002035", "https://booking.united.com/asadali"),
    Doctor("Dr. Naila Islam", 35, "Female", "Allergist", [
           "MBBS", "FCPS"], "United Hospital Limited", "naila.islam@united.com", "+8801811002036", "https://booking.united.com/nailaislam"),
    Doctor("Dr. Jamal Uddin", 51, "Male", "Hand Surgeon", [
           "MBBS", "FCPS"], "United Hospital Limited", "jamal.uddin@united.com", "+8801811002037", "https://booking.united.com/jamaluddin"),
    Doctor("Dr. Shireen Akter", 42, "Female", "Sleep Medicine", [
           "MBBS", "IBCLC"], "United Hospital Limited", "shireen.akter@united.com", "+8801811002038", "https://booking.united.com/shireenaakter"),
    Doctor("Dr. Rafiqul Islam", 48, "Male", "Geriatrician", [
           "MBBS", "FCPS"], "United Hospital Limited", "rafiq.islam@united.com", "+8801811002039", "https://booking.united.com/rafiqislam"),
    Doctor("Dr. Naznin Sultana", 36, "Female", "Reproductive Endocrinologist", [
           "MBBS", "MD"], "United Hospital Limited", "naznin.sultana@united.com", "+8801811002040", "https://booking.united.com/nazninsultana"),
    Doctor("Dr. Mahmud Hasan", 54, "Male", "Interventional Radiologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "mahmud.hasan@united.com", "+8801811002041", "https://booking.united.com/mahmudhasan"),
    Doctor("Dr. Rashida Begum", 40, "Female", "Breast Surgeon", [
           "MBBS", "FCPS"], "United Hospital Limited", "rashida.begum@united.com", "+8801811002042", "https://booking.united.com/rashidabegum"),
    Doctor("Dr. Karimul Islam", 58, "Male", "Pediatric Cardiologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "karim.islam@united.com", "+8801811002043", "https://booking.united.com/karimislam"),
    Doctor("Dr. Shamsun Nahar", 29, "Female", "Medical Oncologist", [
           "MBBS", "FCPS"], "United Hospital Limited", "shamsun.nahar@united.com", "+8801811002044", "https://booking.united.com/shamsunnahar"),
    Doctor("Dr. Robiul Hasan", 43, "Male", "Colorectal Surgeon", [
           "MBBS", "MS"], "United Hospital Limited", "robiul.hasan@united.com", "+8801811002045", "https://booking.united.com/robiulhasan"),

    # Square Hospitals Ltd. (45 doctors)
    Doctor("Dr. Abdul Karim", 46, "Male", "Cardiologist", [
           "MBBS", "FCPS", "FACC"], "Square Hospitals Ltd.", "abdul.karim@square.com", "+8801911003001", "https://booking.square.com/abdulkarim"),
    Doctor("Dr. Rashida Sultana", 39, "Female", "Gynecologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "rashida.sultana@square.com", "+8801911003002", "https://booking.square.com/rashidasultana"),
    Doctor("Dr. Monir Hossain", 52, "Male", "Neurologist", [
           "MBBS", "FCPS", "PhD"], "Square Hospitals Ltd.", "monir.hossain@square.com", "+8801911003003", "https://booking.square.com/monirhossain"),
    Doctor("Dr. Fatema Khatun", 44, "Female", "Pediatrician", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "fatema.khatun@square.com", "+8801911003004", "https://booking.square.com/fatemakhatun"),
    Doctor("Dr. Habibur Rahman", 37, "Male", "Orthopedic Surgeon", [
           "MBBS", "MS"], "Square Hospitals Ltd.", "habib.rahman@square.com", "+8801911003005", "https://booking.square.com/habibrahman"),
    Doctor("Dr. Nasreen Begum", 41, "Female", "Dermatologist", [
           "MBBS", "DDV"], "Square Hospitals Ltd.", "nasreen.begum@square.com", "+8801911003006", "https://booking.square.com/nasreenbegum"),
    Doctor("Dr. Khalil Ahmed", 55, "Male", "General Surgeon", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "khalil.ahmed@square.com", "+8801911003007", "https://booking.square.com/khalilahmed"),
    Doctor("Dr. Shahina Akter", 34, "Female", "ENT Specialist", [
           "MBBS", "DLO"], "Square Hospitals Ltd.", "shahina.akter@square.com", "+8801911003008", "https://booking.square.com/shahinaakter"),
    Doctor("Dr. Delwar Hossain", 48, "Male", "Urologist", [
           "MBBS", "MS"], "Square Hospitals Ltd.", "delwar.hossain@square.com", "+8801911003009", "https://booking.square.com/delwarhossain"),
    Doctor("Dr. Ruma Begum", 42, "Female", "Psychiatrist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "ruma.begum@square.com", "+8801911003010", "https://booking.square.com/rumabegum"),
    Doctor("Dr. Aminul Haque", 49, "Male", "Gastroenterologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "aminul.haque@square.com", "+8801911003011", "https://booking.square.com/aminulhaque"),
    Doctor("Dr. Salina Rahman", 36, "Female", "Endocrinologist", [
           "MBBS", "MD"], "Square Hospitals Ltd.", "salina.rahman@square.com", "+8801911003012", "https://booking.square.com/salinarahman"),
    Doctor("Dr. Shahid Ullah", 54, "Male", "Oncologist", [
           "MBBS", "FCPS", "MRCP"], "Square Hospitals Ltd.", "shahid.ullah@square.com", "+8801911003013", "https://booking.square.com/shahidullah"),
    Doctor("Dr. Mahmuda Khatun", 38, "Female", "Pulmonologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "mahmuda.khatun@square.com", "+8801911003014", "https://booking.square.com/mahmudakhatun"),
    Doctor("Dr. Rafique Uddin", 47, "Male", "Nephrologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "rafique.uddin@square.com", "+8801911003015", "https://booking.square.com/rafiqueuddin"),
    Doctor("Dr. Jesmin Rahman", 43, "Female", "Rheumatologist", [
           "MBBS", "MD"], "Square Hospitals Ltd.", "jesmin.rahman@square.com", "+8801911003016", "https://booking.square.com/jesminrahman"),
    Doctor("Dr. Mosharraf Hossain", 51, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "Square Hospitals Ltd.", "mosharraf.hossain@square.com", "+8801911003017", "https://booking.square.com/mosharrafhossain"),
    Doctor("Dr. Rabeya Sultana", 35, "Female", "Hematologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "rabeya.sultana@square.com", "+8801911003018", "https://booking.square.com/rabeyasultana"),
    Doctor("Dr. Mainul Islam", 45, "Male", "Plastic Surgeon", [
           "MBBS", "MS"], "Square Hospitals Ltd.", "mainul.islam@square.com", "+8801911003019", "https://booking.square.com/mainulislam"),
    Doctor("Dr. Fatema Begum", 40, "Female", "Emergency Medicine", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "fatema.begum@square.com", "+8801911003020", "https://booking.square.com/fatemabegum"),
    Doctor("Dr. Zakir Hussain", 56, "Male", "General Physician", [
           "MBBS"], "Square Hospitals Ltd.", "zakir.hussain@square.com", "+8801911003021", "https://booking.square.com/zakirhussain"),
    Doctor("Dr. Shiuli Akter", 32, "Female", "Family Medicine", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "shiuli.akter@square.com", "+8801911003022", "https://booking.square.com/shiuliakter"),
    Doctor("Dr. Masud Rana", 50, "Male", "Interventional Cardiologist", [
           "MBBS", "FCPS", "FACC"], "Square Hospitals Ltd.", "masud.rana@square.com", "+8801911003023", "https://booking.square.com/masudrana"),
    Doctor("Dr. Nazma Khatun", 46, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "nazma.khatun@square.com", "+8801911003024", "https://booking.square.com/nazmakhatun"),
    Doctor("Dr. Shamsul Alam", 41, "Male", "Spine Surgeon", [
           "MBBS", "MS"], "Square Hospitals Ltd.", "shamsul.alam@square.com", "+8801911003025", "https://booking.square.com/shamsulalam"),
    Doctor("Dr. Rowshan Ara", 37, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "rowshan.ara@square.com", "+8801911003026", "https://booking.square.com/rowshanara"),
    Doctor("Dr. Golam Kibria", 53, "Male", "Hepatologist", [
           "MBBS", "FCPS", "FRCP"], "Square Hospitals Ltd.", "golam.kibria@square.com", "+8801911003027", "https://booking.square.com/golamkibria"),
    Doctor("Dr. Kulsum Begum", 39, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "kulsum.begum@square.com", "+8801911003028", "https://booking.square.com/kulsumbegum"),
    Doctor("Dr. Anwar Hossain", 44, "Male", "Vascular Surgeon", [
           "MBBS", "MS"], "Square Hospitals Ltd.", "anwar.hossain@square.com", "+8801911003029", "https://booking.square.com/anwarhossain"),
    Doctor("Dr. Taslima Akter", 31, "Female", "Infectious Disease", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "taslima.akter@square.com", "+8801911003030", "https://booking.square.com/taslimaakter"),
    Doctor("Dr. Mokbul Hossain", 58, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "Square Hospitals Ltd.", "mokbul.hossain@square.com", "+8801911003031", "https://booking.square.com/mokbulhossain"),
    Doctor("Dr. Nilufar Yasmin", 42, "Female", "Critical Care", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "nilufar.yasmin@square.com", "+8801911003032", "https://booking.square.com/nilufaryasmin"),
    Doctor("Dr. Hakim Ali", 47, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "hakim.ali@square.com", "+8801911003033", "https://booking.square.com/hakimali"),
    Doctor("Dr. Rashida Khatun", 33, "Female", "Diabetologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "rashida.khatun@square.com", "+8801911003034", "https://booking.square.com/rashidakhatun"),
    Doctor("Dr. Kamal Pasha", 49, "Male", "Pain Medicine", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "kamal.pasha@square.com", "+8801911003035", "https://booking.square.com/kamalpasha"),
    Doctor("Dr. Shahnaz Begum", 36, "Female", "Allergist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "shahnaz.begum@square.com", "+8801911003036", "https://booking.square.com/shahnazbegum"),
    Doctor("Dr. Lutfor Rahman", 52, "Male", "Hand Surgeon", [
           "MBBS", "MS"], "Square Hospitals Ltd.", "lutfor.rahman@square.com", "+8801911003037", "https://booking.square.com/lutforrahman"),
    Doctor("Dr. Parvin Sultana", 38, "Female", "Sleep Medicine", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "parvin.sultana@square.com", "+8801911003038", "https://booking.square.com/parvinsultana"),
    Doctor("Dr. Sirajul Islam", 45, "Male", "Geriatrician", [
           "MBBS", "MD"], "Square Hospitals Ltd.", "siraj.islam@square.com", "+8801911003039", "https://booking.square.com/sirajislam"),
    Doctor("Dr. Rasheda Begum", 41, "Female", "Reproductive Endocrinologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "rasheda.begum@square.com", "+8801911003040", "https://booking.square.com/rashedabegum"),
    Doctor("Dr. Mahbub Alam", 54, "Male", "Interventional Radiologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "mahbub.alam@square.com", "+8801911003041", "https://booking.square.com/mahbubalam"),
    Doctor("Dr. Salma Khatun", 29, "Female", "Breast Surgeon", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "salma.khatun@square.com", "+8801911003042", "https://booking.square.com/salmakhatun"),
    Doctor("Dr. Nurul Islam", 48, "Male", "Pediatric Cardiologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "nurul.islam@square.com", "+8801911003043", "https://booking.square.com/nurulislam"),
    Doctor("Dr. Hosne Ara", 43, "Female", "Medical Oncologist", [
           "MBBS", "FCPS"], "Square Hospitals Ltd.", "hosne.ara@square.com", "+8801911003044", "https://booking.square.com/hosneara"),
    Doctor("Dr. Selim Reza", 50, "Male", "Colorectal Surgeon", [
           "MBBS", "MS"], "Square Hospitals Ltd.", "selim.reza@square.com", "+8801911003045", "https://booking.square.com/selimreza"),

    # Bangladesh Specialized Hospital (45 doctors)
    Doctor("Dr. Kamrul Islam", 44, "Male", "Cardiologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "kamrul.islam@bsh.com", "+8801511004001", "https://booking.bsh.com/kamrulislam"),
    Doctor("Dr. Rashida Islam", 38, "Female", "Gynecologist", [
           "MBBS", "FCPS", "DGO"], "Bangladesh Specialized Hospital", "rashida.islam@bsh.com", "+8801511004002", "https://booking.bsh.com/rashidaislam"),
    Doctor("Dr. Mizanur Rahman", 51, "Male", "Neurologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "mizan.rahman@bsh.com", "+8801511004003", "https://booking.bsh.com/mizanrahman"),
    Doctor("Dr. Nasreen Sultana", 45, "Female", "Pediatrician", [
           "MBBS", "MD"], "Bangladesh Specialized Hospital", "nasreen.sultana@bsh.com", "+8801511004004", "https://booking.bsh.com/nasreensultana"),
    Doctor("Dr. Abdus Salam", 39, "Male", "Orthopedic Surgeon", [
           "MBBS", "MS"], "Bangladesh Specialized Hospital", "abdus.salam@bsh.com", "+8801511004005", "https://booking.bsh.com/abdussalam"),
    Doctor("Dr. Farida Khatun", 42, "Female", "Dermatologist", [
           "MBBS", "DDV"], "Bangladesh Specialized Hospital", "farida.khatun@bsh.com", "+8801511004006", "https://booking.bsh.com/faridakhatun"),
    Doctor("Dr. Shahjahan Miah", 56, "Male", "General Surgeon", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "shahjahan.miah@bsh.com", "+8801511004007", "https://booking.bsh.com/shahjahanmiah"),
    Doctor("Dr. Salma Begum", 35, "Female", "ENT Specialist", [
           "MBBS", "DLO"], "Bangladesh Specialized Hospital", "salma.begum@bsh.com", "+8801511004008", "https://booking.bsh.com/salmabegum"),
    Doctor("Dr. Rafiqul Hasan", 47, "Male", "Urologist", [
           "MBBS", "MS"], "Bangladesh Specialized Hospital", "rafiq.hasan@bsh.com", "+8801511004009", "https://booking.bsh.com/rafiqhasan"),
    Doctor("Dr. Rashida Akter", 40, "Female", "Psychiatrist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "rashida.akter@bsh.com", "+8801511004010", "https://booking.bsh.com/rashidaakter"),
    Doctor("Dr. Golam Mostafa", 48, "Male", "Gastroenterologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "golam.mostafa@bsh.com", "+8801511004011", "https://booking.bsh.com/golammostafa"),
    Doctor("Dr. Shahana Begum", 37, "Female", "Endocrinologist", [
           "MBBS", "MD"], "Bangladesh Specialized Hospital", "shahana.begum@bsh.com", "+8801511004012", "https://booking.bsh.com/shahanabegum"),
    Doctor("Dr. Manzur Morshed", 53, "Male", "Oncologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "manzur.morshed@bsh.com", "+8801511004013", "https://booking.bsh.com/manzurmorshed"),
    Doctor("Dr. Rehana Begum", 41, "Female", "Pulmonologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "rehana.begum@bsh.com", "+8801511004014", "https://booking.bsh.com/rehanabegum"),
    Doctor("Dr. Shamsul Haque", 46, "Male", "Nephrologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "shamsul.haque@bsh.com", "+8801511004015", "https://booking.bsh.com/shamsulhaque"),
    Doctor("Dr. Nasima Akter", 43, "Female", "Rheumatologist", [
           "MBBS", "MD"], "Bangladesh Specialized Hospital", "nasima.akter@bsh.com", "+8801511004016", "https://booking.bsh.com/nasimaakter"),
    Doctor("Dr. Khaled Ahmed", 50, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "Bangladesh Specialized Hospital", "khaled.ahmed@bsh.com", "+8801511004017", "https://booking.bsh.com/khaledahmed"),
    Doctor("Dr. Sultana Razia", 34, "Female", "Hematologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "sultana.razia@bsh.com", "+8801511004018", "https://booking.bsh.com/sultanarazia"),
    Doctor("Dr. Abdur Rahman", 45, "Male", "Plastic Surgeon", [
           "MBBS", "MS"], "Bangladesh Specialized Hospital", "abdur.rahman@bsh.com", "+8801511004019", "https://booking.bsh.com/abdurrahman"),
    Doctor("Dr. Tahmina Sultana", 39, "Female", "Emergency Medicine", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "tahmina.sultana@bsh.com", "+8801511004020", "https://booking.bsh.com/tahminasultana"),
    Doctor("Dr. Humayun Kabir", 54, "Male", "General Physician", [
           "MBBS"], "Bangladesh Specialized Hospital", "humayun.kabir@bsh.com", "+8801511004021", "https://booking.bsh.com/humayunkabir"),
    Doctor("Dr. Fatema Islam", 32, "Female", "Family Medicine", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "fatema.islam@bsh.com", "+8801511004022", "https://booking.bsh.com/fatemaislam"),
    Doctor("Dr. Shafiqur Rahman", 49, "Male", "Interventional Cardiologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "shafiq.rahman@bsh.com", "+8801511004023", "https://booking.bsh.com/shafiqrahman"),
    Doctor("Dr. Nazma Rahman", 44, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "nazma.rahman@bsh.com", "+8801511004024", "https://booking.bsh.com/nazmarahman"),
    Doctor("Dr. Aminur Rahman", 41, "Male", "Spine Surgeon", [
           "MBBS", "MS"], "Bangladesh Specialized Hospital", "aminur.rahman@bsh.com", "+8801511004025", "https://booking.bsh.com/aminurrahman"),
    Doctor("Dr. Shahida Begum", 36, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "shahida.begum@bsh.com", "+8801511004026", "https://booking.bsh.com/shahidabegum"),
    Doctor("Dr. Nazrul Islam", 52, "Male", "Hepatologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "nazrul.islam@bsh.com", "+8801511004027", "https://booking.bsh.com/nazrulislam"),
    Doctor("Dr. Marium Begum", 38, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "marium.begum@bsh.com", "+8801511004028", "https://booking.bsh.com/mariumbegum"),
    Doctor("Dr. Azizul Haque", 43, "Male", "Vascular Surgeon", [
           "MBBS", "MS"], "Bangladesh Specialized Hospital", "azizul.haque@bsh.com", "+8801511004029", "https://booking.bsh.com/azizulhaque"),
    Doctor("Dr. Rashida Rahman", 31, "Female", "Infectious Disease", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "rashida.rahman@bsh.com", "+8801511004030", "https://booking.bsh.com/rashidarahman"),
    Doctor("Dr. Monsur Ali", 57, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "monsur.ali@bsh.com", "+8801511004031", "https://booking.bsh.com/monsurali"),
    Doctor("Dr. Shahnaz Rahman", 42, "Female", "Critical Care", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "shahnaz.rahman@bsh.com", "+8801511004032", "https://booking.bsh.com/shahnazrahman"),
    Doctor("Dr. Jashim Uddin", 47, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "jashim.uddin@bsh.com", "+8801511004033", "https://booking.bsh.com/jashimuddin"),
    Doctor("Dr. Rashida Begum", 33, "Female", "Diabetologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "rashida.begum@bsh.com", "+8801511004034", "https://booking.bsh.com/rashidabegum"),
    Doctor("Dr. Mahbubur Rahman", 48, "Male", "Pain Medicine", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "mahbub.rahman@bsh.com", "+8801511004035", "https://booking.bsh.com/mahbubrahman"),
    Doctor("Dr. Salina Begum", 35, "Female", "Allergist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "salina.begum@bsh.com", "+8801511004036", "https://booking.bsh.com/salinabegum"),
    Doctor("Dr. Farid Ahmed", 51, "Male", "Hand Surgeon", [
           "MBBS", "MS"], "Bangladesh Specialized Hospital", "farid.ahmed@bsh.com", "+8801511004037", "https://booking.bsh.com/faridahmed"),
    Doctor("Dr. Hasina Akter", 37, "Female", "Sleep Medicine", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "hasina.akter@bsh.com", "+8801511004038", "https://booking.bsh.com/hasinaakter"),
    Doctor("Dr. Nurul Amin", 44, "Male", "Geriatrician", [
           "MBBS", "MD"], "Bangladesh Specialized Hospital", "nurul.amin@bsh.com", "+8801511004039", "https://booking.bsh.com/nurulamin"),
    Doctor("Dr. Saleha Begum", 40, "Female", "Reproductive Endocrinologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "saleha.begum@bsh.com", "+8801511004040", "https://booking.bsh.com/salehabegum"),
    Doctor("Dr. Kamrul Hasan", 53, "Male", "Interventional Radiologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "kamrul.hasan@bsh.com", "+8801511004041", "https://booking.bsh.com/kamrulhasan"),
    Doctor("Dr. Moslema Khatun", 29, "Female", "Breast Surgeon", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "moslema.khatun@bsh.com", "+8801511004042", "https://booking.bsh.com/moslemakhatun"),
    Doctor("Dr. Ashraf Ali", 46, "Male", "Pediatric Cardiologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "ashraf.ali@bsh.com", "+8801511004043", "https://booking.bsh.com/ashrafali"),
    Doctor("Dr. Selina Khatun", 42, "Female", "Medical Oncologist", [
           "MBBS", "FCPS"], "Bangladesh Specialized Hospital", "selina.khatun@bsh.com", "+8801511004044", "https://booking.bsh.com/selinakhatun"),
    Doctor("Dr. Mahmudul Islam", 49, "Male", "Colorectal Surgeon", [
           "MBBS", "MS"], "Bangladesh Specialized Hospital", "mahmud.islam@bsh.com", "+8801511004045", "https://booking.bsh.com/mahmudislam"),

    # Ibn Sina Specialized Hospital (45 doctors)
    Doctor("Dr. Zillur Rahman", 45, "Male", "Cardiologist", [
           "MBBS", "FCPS", "FACC"], "Ibn Sina Specialized Hospital", "zillur.rahman@ibnsina.com", "+8801611005001", "https://booking.ibnsina.com/zillurrahman"),
    Doctor("Dr. Mahmuda Akter", 39, "Female", "Gynecologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "mahmuda.akter@ibnsina.com", "+8801611005002", "https://booking.ibnsina.com/mahmudaakter"),
    Doctor("Dr. Saifur Rahman", 52, "Male", "Neurologist", [
           "MBBS", "FCPS", "PhD"], "Ibn Sina Specialized Hospital", "saifur.rahman@ibnsina.com", "+8801611005003", "https://booking.ibnsina.com/saifurrahman"),
    Doctor("Dr. Halima Khatun", 46, "Female", "Pediatrician", [
           "MBBS", "MD"], "Ibn Sina Specialized Hospital", "halima.khatun@ibnsina.com", "+8801611005004", "https://booking.ibnsina.com/halimakhatun"),
    Doctor("Dr. Anisul Haque", 40, "Male", "Orthopedic Surgeon", [
           "MBBS", "MS"], "Ibn Sina Specialized Hospital", "anis.haque@ibnsina.com", "+8801611005005", "https://booking.ibnsina.com/anishaque"),
    Doctor("Dr. Shahida Khatun", 43, "Female", "Dermatologist", [
           "MBBS", "DDV"], "Ibn Sina Specialized Hospital", "shahida.khatun@ibnsina.com", "+8801611005006", "https://booking.ibnsina.com/shahidakhatun"),
    Doctor("Dr. Mahfuz Ahmed", 57, "Male", "General Surgeon", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "mahfuz.ahmed@ibnsina.com", "+8801611005007", "https://booking.ibnsina.com/mahfuzahmed"),
    Doctor("Dr. Ruksana Begum", 36, "Female", "ENT Specialist", [
           "MBBS", "DLO"], "Ibn Sina Specialized Hospital", "ruksana.begum@ibnsina.com", "+8801611005008", "https://booking.ibnsina.com/ruksanabegum"),
    Doctor("Dr. Zakaria Rahman", 48, "Male", "Urologist", ["MBBS", "MS"], "Ibn Sina Specialized Hospital",
           "zakaria.rahman@ibnsina.com", "+8801611005009", "https://booking.ibnsina.com/zakariarahman"),
    Doctor("Dr. Nasreen Jahan", 41, "Female", "Psychiatrist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "nasreen.jahan@ibnsina.com", "+8801611005010", "https://booking.ibnsina.com/nasreenjahan"),
    Doctor("Dr. Harun Rashid", 49, "Male", "Gastroenterologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "harun.rashid@ibnsina.com", "+8801611005011", "https://booking.ibnsina.com/harunrashid"),
    Doctor("Dr. Rashida Parvin", 38, "Female", "Endocrinologist", [
           "MBBS", "MD"], "Ibn Sina Specialized Hospital", "rashida.parvin@ibnsina.com", "+8801611005012", "https://booking.ibnsina.com/rashidaparvin"),
    Doctor("Dr. Abdul Malek", 54, "Male", "Oncologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "abdul.malek@ibnsina.com", "+8801611005013", "https://booking.ibnsina.com/abdulmalek"),
    Doctor("Dr. Shamima Begum", 42, "Female", "Pulmonologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "shamima.begum@ibnsina.com", "+8801611005014", "https://booking.ibnsina.com/shamimabegum"),
    Doctor("Dr. Lutfar Rahman", 47, "Male", "Nephrologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "lutfar.rahman@ibnsina.com", "+8801611005015", "https://booking.ibnsina.com/lutfarrahman"),
    Doctor("Dr. Shahana Akter", 44, "Female", "Rheumatologist", [
           "MBBS", "MD"], "Ibn Sina Specialized Hospital", "shahana.akter@ibnsina.com", "+8801611005016", "https://booking.ibnsina.com/shahanaakter"),
    Doctor("Dr. Jahangir Hossain", 51, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "Ibn Sina Specialized Hospital", "jahangir.hossain@ibnsina.com", "+8801611005017", "https://booking.ibnsina.com/jahangirhossain"),
    Doctor("Dr. Rashida Sultana", 35, "Female", "Hematologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "rashida.sultana@ibnsina.com", "+8801611005018", "https://booking.ibnsina.com/rashidasultana"),
    Doctor("Dr. Sirajul Haque", 46, "Male", "Plastic Surgeon", [
           "MBBS", "MS"], "Ibn Sina Specialized Hospital", "siraj.haque@ibnsina.com", "+8801611005019", "https://booking.ibnsina.com/sirajhaque"),
    Doctor("Dr. Rasheda Khatun", 40, "Female", "Emergency Medicine", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "rasheda.khatun@ibnsina.com", "+8801611005020", "https://booking.ibnsina.com/rashedakhatun"),
    Doctor("Dr. Moazzem Hossain", 55, "Male", "General Physician", [
           "MBBS"], "Ibn Sina Specialized Hospital", "moazzem.hossain@ibnsina.com", "+8801611005021", "https://booking.ibnsina.com/moazzemhossain"),
    Doctor("Dr. Shirin Akter", 33, "Female", "Family Medicine", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "shirin.akter@ibnsina.com", "+8801611005022", "https://booking.ibnsina.com/shirinakter"),
    Doctor("Dr. Khairul Islam", 50, "Male", "Interventional Cardiologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "khairul.islam@ibnsina.com", "+8801611005023", "https://booking.ibnsina.com/khairulislam"),
    Doctor("Dr. Rashida Ahmad", 45, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "rashida.ahmad@ibnsina.com", "+8801611005024", "https://booking.ibnsina.com/rashidaahmad"),
    Doctor("Dr. Nurul Huda", 42, "Male", "Spine Surgeon", [
           "MBBS", "MS"], "Ibn Sina Specialized Hospital", "nurul.huda@ibnsina.com", "+8801611005025", "https://booking.ibnsina.com/nurulhuda"),
    Doctor("Dr. Salma Sultana", 37, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "salma.sultana@ibnsina.com", "+8801611005026", "https://booking.ibnsina.com/salmasultana"),
    Doctor("Dr. Mahbubul Alam", 53, "Male", "Hepatologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "mahbub.alam@ibnsina.com", "+8801611005027", "https://booking.ibnsina.com/mahbubalam"),
    Doctor("Dr. Rabeya Khatun", 39, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "rabeya.khatun@ibnsina.com", "+8801611005028", "https://booking.ibnsina.com/rabeyakhatun"),
    Doctor("Dr. Kamrul Ahmed", 44, "Male", "Vascular Surgeon", [
           "MBBS", "MS"], "Ibn Sina Specialized Hospital", "kamrul.ahmed@ibnsina.com", "+8801611005029", "https://booking.ibnsina.com/kamrulahmed"),
    Doctor("Dr. Taslima Begum", 32, "Female", "Infectious Disease", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "taslima.begum@ibnsina.com", "+8801611005030", "https://booking.ibnsina.com/taslimabegum"),
    Doctor("Dr. Abdus Sattar", 58, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "abdus.sattar@ibnsina.com", "+8801611005031", "https://booking.ibnsina.com/abdussattar"),
    Doctor("Dr. Nazma Begum", 43, "Female", "Critical Care", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "nazma.begum@ibnsina.com", "+8801611005032", "https://booking.ibnsina.com/nazmabegum"),
    Doctor("Dr. Rafiqul Islam", 48, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "rafiq.islam@ibnsina.com", "+8801611005033", "https://booking.ibnsina.com/rafiqislam"),
    Doctor("Dr. Shahnaz Parvin", 34, "Female", "Diabetologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "shahnaz.parvin@ibnsina.com", "+8801611005034", "https://booking.ibnsina.com/shahnazparvin"),
    Doctor("Dr. Aminul Hasan", 49, "Male", "Pain Medicine", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "aminul.hasan@ibnsina.com", "+8801611005035", "https://booking.ibnsina.com/aminulhasan"),
    Doctor("Dr. Rashida Hasan", 36, "Female", "Allergist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "rashida.hasan@ibnsina.com", "+8801611005036", "https://booking.ibnsina.com/rashidahasan"),
    Doctor("Dr. Golam Sarwar", 52, "Male", "Hand Surgeon", [
           "MBBS", "MS"], "Ibn Sina Specialized Hospital", "golam.sarwar@ibnsina.com", "+8801611005037", "https://booking.ibnsina.com/golamsarwar"),
    Doctor("Dr. Sabina Khatun", 38, "Female", "Sleep Medicine", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "sabina.khatun@ibnsina.com", "+8801611005038", "https://booking.ibnsina.com/sabinakhatun"),
    Doctor("Dr. Moshiur Rahman", 45, "Male", "Geriatrician", [
           "MBBS", "MD"], "Ibn Sina Specialized Hospital", "moshiur.rahman@ibnsina.com", "+8801611005039", "https://booking.ibnsina.com/moshiurrahman"),
    Doctor("Dr. Rashida Yasmin", 41, "Female", "Reproductive Endocrinologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "rashida.yasmin@ibnsina.com", "+8801611005040", "https://booking.ibnsina.com/rashidayasmin"),
    Doctor("Dr. Shafiqul Islam", 54, "Male", "Interventional Radiologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "shafiq.islam@ibnsina.com", "+8801611005041", "https://booking.ibnsina.com/shafiqislam"),
    Doctor("Dr. Farjana Begum", 30, "Female", "Breast Surgeon", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "farjana.begum@ibnsina.com", "+8801611005042", "https://booking.ibnsina.com/farjanabegum"),
    Doctor("Dr. Matiur Rahman", 47, "Male", "Pediatric Cardiologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "matiur.rahman@ibnsina.com", "+8801611005043", "https://booking.ibnsina.com/matiurrahman"),
    Doctor("Dr. Nasreen Sultana", 43, "Female", "Medical Oncologist", [
           "MBBS", "FCPS"], "Ibn Sina Specialized Hospital", "nasreen.sultana@ibnsina.com", "+8801611005044", "https://booking.ibnsina.com/nasreensultana"),
    Doctor("Dr. Hanif Ahmed", 50, "Male", "Colorectal Surgeon", [
           "MBBS", "MS"], "Ibn Sina Specialized Hospital", "hanif.ahmed@ibnsina.com", "+8801611005045", "https://booking.ibnsina.com/hanifahmed"),

    # Popular Medical College & Hospital (45 doctors)
    Doctor("Dr. Shamim Ahmed", 46, "Male", "Cardiologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "shamim.ahmed@popular.com", "+8801711006001", "https://booking.popular.com/shamimahmed"),
    Doctor("Dr. Rashida Khanam", 40, "Female", "Gynecologist", [
           "MBBS", "FCPS", "DGO"], "Popular Medical College & Hospital", "rashida.khanam@popular.com", "+8801711006002", "https://booking.popular.com/rashidakhanam"),
    Doctor("Dr. Nazrul Haque", 53, "Male", "Neurologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "nazrul.haque@popular.com", "+8801711006003", "https://booking.popular.com/nazrulhaque"),
    Doctor("Dr. Fatema Rahman", 47, "Female", "Pediatrician", [
           "MBBS", "MD"], "Popular Medical College & Hospital", "fatema.rahman@popular.com", "+8801711006004", "https://booking.popular.com/fatemarahman"),
    Doctor("Dr. Sirajul Islam", 41, "Male", "Orthopedic Surgeon", [
           "MBBS", "MS"], "Popular Medical College & Hospital", "siraj.islam@popular.com", "+8801711006005", "https://booking.popular.com/sirajislam"),
    Doctor("Dr. Shahnaz Khatun", 44, "Female", "Dermatologist", [
           "MBBS", "DDV"], "Popular Medical College & Hospital", "shahnaz.khatun@popular.com", "+8801711006006", "https://booking.popular.com/shahnazkhatun"),
    Doctor("Dr. Rafique Ahmed", 58, "Male", "General Surgeon", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rafique.ahmed@popular.com", "+8801711006007", "https://booking.popular.com/rafiqueahmed"),
    Doctor("Dr. Salma Rahman", 37, "Female", "ENT Specialist", [
           "MBBS", "DLO"], "Popular Medical College & Hospital", "salma.rahman@popular.com", "+8801711006008", "https://booking.popular.com/salmarahman"),
    Doctor("Dr. Mahbub Hasan", 49, "Male", "Urologist", ["MBBS", "MS"], "Popular Medical College & Hospital",
           "mahbub.hasan@popular.com", "+8801711006009", "https://booking.popular.com/mahbubhasan"),
    Doctor("Dr. Rashida Begum", 42, "Female", "Psychiatrist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rashida.begum@popular.com", "+8801711006010", "https://booking.popular.com/rashidabegum"),
    Doctor("Dr. Shamsul Islam", 50, "Male", "Gastroenterologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "shamsul.islam@popular.com", "+8801711006011", "https://booking.popular.com/shamsulislam"),
    Doctor("Dr. Nasreen Rahman", 39, "Female", "Endocrinologist", [
           "MBBS", "MD"], "Popular Medical College & Hospital", "nasreen.rahman@popular.com", "+8801711006012", "https://booking.popular.com/nasreenrahman"),
    Doctor("Dr. Kamal Ahmed", 55, "Male", "Oncologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "kamal.ahmed@popular.com", "+8801711006013", "https://booking.popular.com/kamalahed"),
    Doctor("Dr. Shahina Rahman", 43, "Female", "Pulmonologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "shahina.rahman@popular.com", "+8801711006014", "https://booking.popular.com/shahinarahman"),
    Doctor("Dr. Lutfur Rahman", 48, "Male", "Nephrologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "lutfur.rahman@popular.com", "+8801711006015", "https://booking.popular.com/lutfurrahman"),
    Doctor("Dr. Rashida Islam", 45, "Female", "Rheumatologist", [
           "MBBS", "MD"], "Popular Medical College & Hospital", "rashida.islam@popular.com", "+8801711006016", "https://booking.popular.com/rashidaislam"),
    Doctor("Dr. Masud Ahmed", 52, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "Popular Medical College & Hospital", "masud.ahmed@popular.com", "+8801711006017", "https://booking.popular.com/masudahmed"),
    Doctor("Dr. Selina Rahman", 36, "Female", "Hematologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "selina.rahman@popular.com", "+8801711006018", "https://booking.popular.com/selinarahman"),
    Doctor("Dr. Golam Rahman", 47, "Male", "Plastic Surgeon", [
           "MBBS", "MS"], "Popular Medical College & Hospital", "golam.rahman@popular.com", "+8801711006019", "https://booking.popular.com/golamrahman"),
    Doctor("Dr. Tahmina Khatun", 41, "Female", "Emergency Medicine", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "tahmina.khatun@popular.com", "+8801711006020", "https://booking.popular.com/tahminakhatun"),
    Doctor("Dr. Anwar Islam", 56, "Male", "General Physician", [
           "MBBS"], "Popular Medical College & Hospital", "anwar.islam@popular.com", "+8801711006021", "https://booking.popular.com/anwarislam"),
    Doctor("Dr. Rashida Haque", 34, "Female", "Family Medicine", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rashida.haque@popular.com", "+8801711006022", "https://booking.popular.com/rashidahaque"),
    Doctor("Dr. Aminul Islam", 51, "Male", "Interventional Cardiologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "aminul.islam@popular.com", "+8801711006023", "https://booking.popular.com/aminulislam"),
    Doctor("Dr. Shamima Rahman", 46, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "shamima.rahman@popular.com", "+8801711006024", "https://booking.popular.com/shamimarahman"),
    Doctor("Dr. Shafiqur Alam", 43, "Male", "Spine Surgeon", [
           "MBBS", "MS"], "Popular Medical College & Hospital", "shafiq.alam@popular.com", "+8801711006025", "https://booking.popular.com/shafiqalam"),
    Doctor("Dr. Rowshan Jahan", 38, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rowshan.jahan@popular.com", "+8801711006026", "https://booking.popular.com/rowshanjahan"),
    Doctor("Dr. Mahfuzur Islam", 54, "Male", "Hepatologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "mahfuz.islam@popular.com", "+8801711006027", "https://booking.popular.com/mahfuzislam"),
    Doctor("Dr. Rashida Sultana", 40, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rashida.sultana@popular.com", "+8801711006028", "https://booking.popular.com/rashidasultana"),
    Doctor("Dr. Hafizur Rahman", 45, "Male", "Vascular Surgeon", [
           "MBBS", "MS"], "Popular Medical College & Hospital", "hafiz.rahman@popular.com", "+8801711006029", "https://booking.popular.com/hafizrahman"),
    Doctor("Dr. Salma Begum", 33, "Female", "Infectious Disease", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "salma.begum@popular.com", "+8801711006030", "https://booking.popular.com/salmabegum"),
    Doctor("Dr. Munir Ahmed", 59, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "munir.ahmed@popular.com", "+8801711006031", "https://booking.popular.com/munirahmed"),
    Doctor("Dr. Shahana Khatun", 44, "Female", "Critical Care", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "shahana.khatun@popular.com", "+8801711006032", "https://booking.popular.com/shahanakhatun"),
    Doctor("Dr. Shahidul Haque", 49, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "shahid.haque@popular.com", "+8801711006033", "https://booking.popular.com/shahidhaque"),
    Doctor("Dr. Rashida Ahmed", 35, "Female", "Diabetologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rashida.ahmed@popular.com", "+8801711006034", "https://booking.popular.com/rashidaahmed"),
    Doctor("Dr. Nurul Islam", 50, "Male", "Pain Medicine", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "nurul.islam@popular.com", "+8801711006035", "https://booking.popular.com/nurulislam"),
    Doctor("Dr. Salina Khatun", 37, "Female", "Allergist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "salina.khatun@popular.com", "+8801711006036", "https://booking.popular.com/salinakhatun"),
    Doctor("Dr. Manzur Ahmed", 53, "Male", "Hand Surgeon", [
           "MBBS", "MS"], "Popular Medical College & Hospital", "manzur.ahmed@popular.com", "+8801711006037", "https://booking.popular.com/manzurahmed"),
    Doctor("Dr. Rashida Parvin", 39, "Female", "Sleep Medicine", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rashida.parvin@popular.com", "+8801711006038", "https://booking.popular.com/rashidaparvin"),
    Doctor("Dr. Shafiul Alam", 46, "Male", "Geriatrician", [
           "MBBS", "MD"], "Popular Medical College & Hospital", "shafi.alam@popular.com", "+8801711006039", "https://booking.popular.com/shafialam"),
    Doctor("Dr. Rashida Khan", 42, "Female", "Reproductive Endocrinologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rashida.khan@popular.com", "+8801711006040", "https://booking.popular.com/rashidakhan"),
    Doctor("Dr. Rafiqul Hasan", 55, "Male", "Interventional Radiologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rafiq.hasan@popular.com", "+8801711006041", "https://booking.popular.com/rafiqhasan"),
    Doctor("Dr. Salma Islam", 31, "Female", "Breast Surgeon", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "salma.islam@popular.com", "+8801711006042", "https://booking.popular.com/salmaislam"),
    Doctor("Dr. Mahbubul Haque", 48, "Male", "Pediatric Cardiologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "mahbub.haque@popular.com", "+8801711006043", "https://booking.popular.com/mahbubhaque"),
    Doctor("Dr. Rashida Rahman", 44, "Female", "Medical Oncologist", [
           "MBBS", "FCPS"], "Popular Medical College & Hospital", "rashida.rahman@popular.com", "+8801711006044", "https://booking.popular.com/rashidarahman"),
    Doctor("Dr. Abdur Rahman", 51, "Male", "Colorectal Surgeon", [
           "MBBS", "MS"], "Popular Medical College & Hospital", "abdur.rahman@popular.com", "+8801711006045", "https://booking.popular.com/abdurrahman"),

    # Dhaka Medical College Hospital (DMCH) (45 doctors)
    Doctor("Dr. Abdul Latif", 47, "Male", "Cardiologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "abdul.latif@dmch.gov.bd", "+8801811007001", "https://booking.dmch.gov.bd/abdullatif"),
    Doctor("Dr. Rashida Nasreen", 41, "Female", "Gynecologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.nasreen@dmch.gov.bd", "+8801811007002", "https://booking.dmch.gov.bd/rashidanasreen"),
    Doctor("Dr. Mahbubur Rahman", 54, "Male", "Neurologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "mahbub.rahman@dmch.gov.bd", "+8801811007003", "https://booking.dmch.gov.bd/mahbubrahman"),
    Doctor("Dr. Salma Khatun", 48, "Female", "Pediatrician", [
           "MBBS", "MD"], "Dhaka Medical College Hospital (DMCH)", "salma.khatun@dmch.gov.bd", "+8801811007004", "https://booking.dmch.gov.bd/salmakhatun"),
    Doctor("Dr. Rashidul Islam", 42, "Male", "Orthopedic Surgeon", [
           "MBBS", "MS"], "Dhaka Medical College Hospital (DMCH)", "rashid.islam@dmch.gov.bd", "+8801811007005", "https://booking.dmch.gov.bd/rashidislam"),
    Doctor("Dr. Nasreen Akter", 45, "Female", "Dermatologist", [
           "MBBS", "DDV"], "Dhaka Medical College Hospital (DMCH)", "nasreen.akter@dmch.gov.bd", "+8801811007006", "https://booking.dmch.gov.bd/nasreenakter"),
    Doctor("Dr. Abdus Sabur", 59, "Male", "General Surgeon", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "abdus.sabur@dmch.gov.bd", "+8801811007007", "https://booking.dmch.gov.bd/abdussabur"),
    Doctor("Dr. Shahida Rahman", 38, "Female", "ENT Specialist", [
           "MBBS", "DLO"], "Dhaka Medical College Hospital (DMCH)", "shahida.rahman@dmch.gov.bd", "+8801811007008", "https://booking.dmch.gov.bd/shahidarahman"),
    Doctor("Dr. Nazrul Islam", 50, "Male", "Urologist", ["MBBS", "MS"], "Dhaka Medical College Hospital (DMCH)",
           "nazrul.islam@dmch.gov.bd", "+8801811007009", "https://booking.dmch.gov.bd/nazrulislam"),
    Doctor("Dr. Rashida Khatun", 43, "Female", "Psychiatrist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.khatun@dmch.gov.bd", "+8801811007010", "https://booking.dmch.gov.bd/rashidakhatun"),
    Doctor("Dr. Nurul Amin", 51, "Male", "Gastroenterologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "nurul.amin@dmch.gov.bd", "+8801811007011", "https://booking.dmch.gov.bd/nurulamin"),
    Doctor("Dr. Salina Begum", 40, "Female", "Endocrinologist", [
           "MBBS", "MD"], "Dhaka Medical College Hospital (DMCH)", "salina.begum@dmch.gov.bd", "+8801811007012", "https://booking.dmch.gov.bd/salinabegum"),
    Doctor("Dr. Mahfuz Rahman", 56, "Male", "Oncologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "mahfuz.rahman@dmch.gov.bd", "+8801811007013", "https://booking.dmch.gov.bd/mahfuzrahman"),
    Doctor("Dr. Rashida Islam", 44, "Female", "Pulmonologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.islam@dmch.gov.bd", "+8801811007014", "https://booking.dmch.gov.bd/rashidaislam"),
    Doctor("Dr. Shamsul Haque", 49, "Male", "Nephrologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "shamsul.haque@dmch.gov.bd", "+8801811007015", "https://booking.dmch.gov.bd/shamsulhaque"),
    Doctor("Dr. Rashida Begum", 46, "Female", "Rheumatologist", [
           "MBBS", "MD"], "Dhaka Medical College Hospital (DMCH)", "rashida.begum@dmch.gov.bd", "+8801811007016", "https://booking.dmch.gov.bd/rashidabegum"),
    Doctor("Dr. Jahangir Alam", 53, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "jahangir.alam@dmch.gov.bd", "+8801811007017", "https://booking.dmch.gov.bd/jahangiralam"),
    Doctor("Dr. Sultana Razia", 37, "Female", "Hematologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "sultana.razia@dmch.gov.bd", "+8801811007018", "https://booking.dmch.gov.bd/sultanarazia"),
    Doctor("Dr. Rafiqul Islam", 48, "Male", "Plastic Surgeon", [
           "MBBS", "MS"], "Dhaka Medical College Hospital (DMCH)", "rafiq.islam@dmch.gov.bd", "+8801811007019", "https://booking.dmch.gov.bd/rafiqislam"),
    Doctor("Dr. Rashida Akter", 42, "Female", "Emergency Medicine", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.akter@dmch.gov.bd", "+8801811007020", "https://booking.dmch.gov.bd/rashidaakter"),
    Doctor("Dr. Azizul Haque", 57, "Male", "General Physician", [
           "MBBS"], "Dhaka Medical College Hospital (DMCH)", "azizul.haque@dmch.gov.bd", "+8801811007021", "https://booking.dmch.gov.bd/azizulhaque"),
    Doctor("Dr. Sharmin Sultana", 35, "Female", "Family Medicine", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "sharmin.sultana@dmch.gov.bd", "+8801811007022", "https://booking.dmch.gov.bd/sharminsultana"),
    Doctor("Dr. Shafiqul Islam", 52, "Male", "Interventional Cardiologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "shafiq.islam@dmch.gov.bd", "+8801811007023", "https://booking.dmch.gov.bd/shafiqislam"),
    Doctor("Dr. Rashida Rahman", 47, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.rahman@dmch.gov.bd", "+8801811007024", "https://booking.dmch.gov.bd/rashidarahman"),
    Doctor("Dr. Anwarul Haque", 44, "Male", "Spine Surgeon", [
           "MBBS", "MS"], "Dhaka Medical College Hospital (DMCH)", "anwar.haque@dmch.gov.bd", "+8801811007025", "https://booking.dmch.gov.bd/anwarhaque"),
    Doctor("Dr. Salma Islam", 39, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "salma.islam@dmch.gov.bd", "+8801811007026", "https://booking.dmch.gov.bd/salmaislam"),
    Doctor("Dr. Mahmudul Hasan", 55, "Male", "Hepatologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "mahmud.hasan@dmch.gov.bd", "+8801811007027", "https://booking.dmch.gov.bd/mahmudhasan"),
    Doctor("Dr. Rashida Sultana", 41, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.sultana@dmch.gov.bd", "+8801811007028", "https://booking.dmch.gov.bd/rashidasultana"),
    Doctor("Dr. Lutfar Rahman", 46, "Male", "Vascular Surgeon", [
           "MBBS", "MS"], "Dhaka Medical College Hospital (DMCH)", "lutfar.rahman@dmch.gov.bd", "+8801811007029", "https://booking.dmch.gov.bd/lutfarrahman"),
    Doctor("Dr. Rashida Yasmin", 34, "Female", "Infectious Disease", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.yasmin@dmch.gov.bd", "+8801811007030", "https://booking.dmch.gov.bd/rashidayasmin"),
    Doctor("Dr. Abdur Rahim", 60, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "abdur.rahim@dmch.gov.bd", "+8801811007031", "https://booking.dmch.gov.bd/abdurrahim"),
    Doctor("Dr. Rashida Ahmed", 45, "Female", "Critical Care", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.ahmed@dmch.gov.bd", "+8801811007032", "https://booking.dmch.gov.bd/rashidaahmed"),
    Doctor("Dr. Rafique Uddin", 50, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rafique.uddin@dmch.gov.bd", "+8801811007033", "https://booking.dmch.gov.bd/rafiqueuddin"),
    Doctor("Dr. Rashida Haque", 36, "Female", "Diabetologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.haque@dmch.gov.bd", "+8801811007034", "https://booking.dmch.gov.bd/rashidahaque"),
    Doctor("Dr. Mainul Haque", 51, "Male", "Pain Medicine", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "mainul.haque@dmch.gov.bd", "+8801811007035", "https://booking.dmch.gov.bd/mainulhaque"),
    Doctor("Dr. Rashida Khan", 38, "Female", "Allergist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.khan@dmch.gov.bd", "+8801811007036", "https://booking.dmch.gov.bd/rashidakhan"),
    Doctor("Dr. Saifur Rahman", 54, "Male", "Hand Surgeon", [
           "MBBS", "MS"], "Dhaka Medical College Hospital (DMCH)", "saifur.rahman@dmch.gov.bd", "+8801811007037", "https://booking.dmch.gov.bd/saifurrahman"),
    Doctor("Dr. Rashida Miah", 40, "Female", "Sleep Medicine", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.miah@dmch.gov.bd", "+8801811007038", "https://booking.dmch.gov.bd/rashidamiah"),
    Doctor("Dr. Nurul Huda", 47, "Male", "Geriatrician", [
           "MBBS", "MD"], "Dhaka Medical College Hospital (DMCH)", "nurul.huda@dmch.gov.bd", "+8801811007039", "https://booking.dmch.gov.bd/nurulhuda"),
    Doctor("Dr. Rashida Alam", 43, "Female", "Reproductive Endocrinologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.alam@dmch.gov.bd", "+8801811007040", "https://booking.dmch.gov.bd/rashidaalam"),
    Doctor("Dr. Hakim Ali", 56, "Male", "Interventional Radiologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "hakim.ali@dmch.gov.bd", "+8801811007041", "https://booking.dmch.gov.bd/hakimali"),
    Doctor("Dr. Rashida Parveen", 32, "Female", "Breast Surgeon", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.parveen@dmch.gov.bd", "+8801811007042", "https://booking.dmch.gov.bd/rashidaparveen"),
    Doctor("Dr. Mushfiqur Rahman", 49, "Male", "Pediatric Cardiologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "mushfiq.rahman@dmch.gov.bd", "+8801811007043", "https://booking.dmch.gov.bd/mushfiqrahman"),
    Doctor("Dr. Rashida Bibi", 45, "Female", "Medical Oncologist", [
           "MBBS", "FCPS"], "Dhaka Medical College Hospital (DMCH)", "rashida.bibi@dmch.gov.bd", "+8801811007044", "https://booking.dmch.gov.bd/rashidabibi"),
    Doctor("Dr. Shamsur Rahman", 52, "Male", "Colorectal Surgeon", [
           "MBBS", "MS"], "Dhaka Medical College Hospital (DMCH)", "shamsur.rahman@dmch.gov.bd", "+8801811007045", "https://booking.dmch.gov.bd/shamsurrahman"),

    # Labaid Specialized Hospital (45 doctors)
    Doctor("Dr. Faruque Ahmed", 48, "Male", "Cardiologist", [
           "MBBS", "FCPS", "FACC"], "Labaid Specialized Hospital", "faruque.ahmed@labaid.com", "+8801911008001", "https://booking.labaid.com/faruqueahmed"),
    Doctor("Dr. Rashida Nasrin", 42, "Female", "Gynecologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.nasrin@labaid.com", "+8801911008002", "https://booking.labaid.com/rashidanasrin"),
    Doctor("Dr. Zahirul Islam", 55, "Male", "Neurologist", [
           "MBBS", "FCPS", "PhD"], "Labaid Specialized Hospital", "zahir.islam@labaid.com", "+8801911008003", "https://booking.labaid.com/zahirislam"),
    Doctor("Dr. Fatema Sultana", 49, "Female", "Pediatrician", [
           "MBBS", "MD"], "Labaid Specialized Hospital", "fatema.sultana@labaid.com", "+8801911008004", "https://booking.labaid.com/fatemasultana"),
    Doctor("Dr. Masudur Rahman", 43, "Male", "Orthopedic Surgeon", [
           "MBBS", "MS"], "Labaid Specialized Hospital", "masud.rahman@labaid.com", "+8801911008005", "https://booking.labaid.com/masudrahman"),
    Doctor("Dr. Shahida Akter", 46, "Female", "Dermatologist", [
           "MBBS", "DDV"], "Labaid Specialized Hospital", "shahida.akter@labaid.com", "+8801911008006", "https://booking.labaid.com/shahidaakter"),
    Doctor("Dr. Shahidul Islam", 60, "Male", "General Surgeon", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "shahid.islam@labaid.com", "+8801911008007", "https://booking.labaid.com/shahidislam"),
    Doctor("Dr. Selina Khatun", 39, "Female", "ENT Specialist", [
           "MBBS", "DLO"], "Labaid Specialized Hospital", "selina.khatun@labaid.com", "+8801911008008", "https://booking.labaid.com/selinakhatun"),
    Doctor("Dr. Golam Rabbani", 51, "Male", "Urologist", [
           "MBBS", "MS"], "Labaid Specialized Hospital", "golam.rabbani@labaid.com", "+8801911008009", "https://booking.labaid.com/golamrabbani"),
    Doctor("Dr. Rashida Sultana", 44, "Female", "Psychiatrist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.sultana@labaid.com", "+8801911008010", "https://booking.labaid.com/rashidasultana"),
    Doctor("Dr. Hafizur Rahman", 52, "Male", "Gastroenterologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "hafiz.rahman@labaid.com", "+8801911008011", "https://booking.labaid.com/hafizrahman"),
    Doctor("Dr. Rashida Parvin", 41, "Female", "Endocrinologist", [
           "MBBS", "MD"], "Labaid Specialized Hospital", "rashida.parvin@labaid.com", "+8801911008012", "https://booking.labaid.com/rashidaparvin"),
    Doctor("Dr. Monirul Islam", 57, "Male", "Oncologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "monir.islam@labaid.com", "+8801911008013", "https://booking.labaid.com/monirislam"),
    Doctor("Dr. Rashida Khanam", 45, "Female", "Pulmonologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.khanam@labaid.com", "+8801911008014", "https://booking.labaid.com/rashidakhanam"),
    Doctor("Dr. Maksudur Rahman", 50, "Male", "Nephrologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "maksud.rahman@labaid.com", "+8801911008015", "https://booking.labaid.com/maksudrahman"),
    Doctor("Dr. Rashida Begum", 47, "Female", "Rheumatologist", [
           "MBBS", "MD"], "Labaid Specialized Hospital", "rashida.begum@labaid.com", "+8801911008016", "https://booking.labaid.com/rashidabegum"),
    Doctor("Dr. Shahjalal Ahmed", 54, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS", "FRCS"], "Labaid Specialized Hospital", "shahjalal.ahmed@labaid.com", "+8801911008017", "https://booking.labaid.com/shahjalalahmed"),
    Doctor("Dr. Rashida Islam", 38, "Female", "Hematologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.islam@labaid.com", "+8801911008018", "https://booking.labaid.com/rashidaislam"),
    Doctor("Dr. Aminul Haque", 49, "Male", "Plastic Surgeon", [
           "MBBS", "MS"], "Labaid Specialized Hospital", "aminul.haque@labaid.com", "+8801911008019", "https://booking.labaid.com/aminulhaque"),
    Doctor("Dr. Rashida Rahman", 43, "Female", "Emergency Medicine", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.rahman@labaid.com", "+8801911008020", "https://booking.labaid.com/rashidarahman"),
    Doctor("Dr. Nazrul Haque", 58, "Male", "General Physician", [
           "MBBS"], "Labaid Specialized Hospital", "nazrul.haque@labaid.com", "+8801911008021", "https://booking.labaid.com/nazrulhaque"),
    Doctor("Dr. Rashida Yasmin", 36, "Female", "Family Medicine", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.yasmin@labaid.com", "+8801911008022", "https://booking.labaid.com/rashidayasmin"),
    Doctor("Dr. Mahbubul Hasan", 53, "Male", "Interventional Cardiologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "mahbub.hasan@labaid.com", "+8801911008023", "https://booking.labaid.com/mahbubhasan"),
    Doctor("Dr. Rashida Akter", 48, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.akter@labaid.com", "+8801911008024", "https://booking.labaid.com/rashidaakter"),
    Doctor("Dr. Mosharraf Hossain", 45, "Male", "Spine Surgeon", [
           "MBBS", "MS"], "Labaid Specialized Hospital", "mosharraf.hossain@labaid.com", "+8801911008025", "https://booking.labaid.com/mosharrafhossain"),
    Doctor("Dr. Rashida Ahmed", 40, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.ahmed@labaid.com", "+8801911008026", "https://booking.labaid.com/rashidaahmed"),
    Doctor("Dr. Shafiul Azam", 56, "Male", "Hepatologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "shafi.azam@labaid.com", "+8801911008027", "https://booking.labaid.com/shafiazam"),
    Doctor("Dr. Rashida Khatun", 42, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.khatun@labaid.com", "+8801911008028", "https://booking.labaid.com/rashidakhatun"),
    Doctor("Dr. Shamim Ahmed", 47, "Male", "Vascular Surgeon", [
           "MBBS", "MS"], "Labaid Specialized Hospital", "shamim.ahmed@labaid.com", "+8801911008029", "https://booking.labaid.com/shamimahmed"),
    Doctor("Dr. Rashida Hasan", 35, "Female", "Infectious Disease", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.hasan@labaid.com", "+8801911008030", "https://booking.labaid.com/rashidahasan"),
    Doctor("Dr. Anisur Rahman", 61, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "anis.rahman@labaid.com", "+8801911008031", "https://booking.labaid.com/anisrahman"),
    Doctor("Dr. Rashida Sultana", 46, "Female", "Critical Care", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.sultana@labaid.com", "+8801911008032", "https://booking.labaid.com/rashidasultana"),
    Doctor("Dr. Khairul Bashar", 51, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "khairul.bashar@labaid.com", "+8801911008033", "https://booking.labaid.com/khairulbashar"),
    Doctor("Dr. Rashida Khan", 37, "Female", "Diabetologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.khan@labaid.com", "+8801911008034", "https://booking.labaid.com/rashidakhan"),
    Doctor("Dr. Shahabuddin Ahmed", 52, "Male", "Pain Medicine", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "shahab.ahmed@labaid.com", "+8801911008035", "https://booking.labaid.com/shahabahmed"),
    Doctor("Dr. Rashida Miah", 39, "Female", "Allergist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.miah@labaid.com", "+8801911008036", "https://booking.labaid.com/rashidamiah"),
    Doctor("Dr. Mahmudul Haque", 55, "Male", "Hand Surgeon", [
           "MBBS", "MS"], "Labaid Specialized Hospital", "mahmud.haque@labaid.com", "+8801911008037", "https://booking.labaid.com/mahmudhaque"),
    Doctor("Dr. Rashida Begum", 41, "Female", "Sleep Medicine", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.begum@labaid.com", "+8801911008038", "https://booking.labaid.com/rashidabegum"),
    Doctor("Dr. Abdus Samad", 48, "Male", "Geriatrician", [
           "MBBS", "MD"], "Labaid Specialized Hospital", "abdus.samad@labaid.com", "+8801911008039", "https://booking.labaid.com/abdussamad"),
    Doctor("Dr. Rashida Islam", 44, "Female", "Reproductive Endocrinologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.islam@labaid.com", "+8801911008040", "https://booking.labaid.com/rashidaislam"),
    Doctor("Dr. Abdur Rahman", 57, "Male", "Interventional Radiologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "abdur.rahman@labaid.com", "+8801911008041", "https://booking.labaid.com/abdurrahman"),
    Doctor("Dr. Rashida Ahmed", 33, "Female", "Breast Surgeon", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.ahmed@labaid.com", "+8801911008042", "https://booking.labaid.com/rashidaahmed"),
    Doctor("Dr. Saifuddin Ahmed", 50, "Male", "Pediatric Cardiologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "saif.ahmed@labaid.com", "+8801911008043", "https://booking.labaid.com/saifahmed"),
    Doctor("Dr. Rashida Nasreen", 46, "Female", "Medical Oncologist", [
           "MBBS", "FCPS"], "Labaid Specialized Hospital", "rashida.nasreen@labaid.com", "+8801911008044", "https://booking.labaid.com/rashidanasreen"),
    Doctor("Dr. Mofizur Rahman", 53, "Male", "Colorectal Surgeon", [
           "MBBS", "MS"], "Labaid Specialized Hospital", "mofiz.rahman@labaid.com", "+8801911008045", "https://booking.labaid.com/mofizrahman"),

    # Anwer Khan Modern Hospital (40 doctors)
    Doctor("Dr. Shahidul Haque", 49, "Male", "Cardiologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "shahid.haque@akmh.com", "+8801511009001", "https://booking.akmh.com/shahidhaque"),
    Doctor("Dr. Rashida Ahmed", 43, "Female", "Gynecologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.ahmed@akmh.com", "+8801511009002", "https://booking.akmh.com/rashidaahmed"),
    Doctor("Dr. Mokhlesur Rahman", 56, "Male", "Neurologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "mokhles.rahman@akmh.com", "+8801511009003", "https://booking.akmh.com/mokhlesrahman"),
    Doctor("Dr. Salina Rahman", 50, "Female", "Pediatrician", [
           "MBBS", "MD"], "Anwer Khan Modern Hospital", "salina.rahman@akmh.com", "+8801511009004", "https://booking.akmh.com/salinarahman"),
    Doctor("Dr. Rafiqul Hasan", 44, "Male", "Orthopedic Surgeon", [
           "MBBS", "MS"], "Anwer Khan Modern Hospital", "rafiq.hasan@akmh.com", "+8801511009005", "https://booking.akmh.com/rafiqhasan"),
    Doctor("Dr. Rashida Sultana", 47, "Female", "Dermatologist", [
           "MBBS", "DDV"], "Anwer Khan Modern Hospital", "rashida.sultana@akmh.com", "+8801511009006", "https://booking.akmh.com/rashidasultana"),
    Doctor("Dr. Khalilur Rahman", 61, "Male", "General Surgeon", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "khalil.rahman@akmh.com", "+8801511009007", "https://booking.akmh.com/khalilrahman"),
    Doctor("Dr. Rashida Khatun", 40, "Female", "ENT Specialist", [
           "MBBS", "DLO"], "Anwer Khan Modern Hospital", "rashida.khatun@akmh.com", "+8801511009008", "https://booking.akmh.com/rashidakhatun"),
    Doctor("Dr. Shamsul Huda", 52, "Male", "Urologist", [
           "MBBS", "MS"], "Anwer Khan Modern Hospital", "shamsul.huda@akmh.com", "+8801511009009", "https://booking.akmh.com/shamsulhuda"),
    Doctor("Dr. Rashida Parvin", 45, "Female", "Psychiatrist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.parvin@akmh.com", "+8801511009010", "https://booking.akmh.com/rashidaparvin"),
    Doctor("Dr. Mahfuzul Haque", 53, "Male", "Gastroenterologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "mahfuz.haque@akmh.com", "+8801511009011", "https://booking.akmh.com/mahfuzhaque"),
    Doctor("Dr. Rashida Yasmin", 42, "Female", "Endocrinologist", [
           "MBBS", "MD"], "Anwer Khan Modern Hospital", "rashida.yasmin@akmh.com", "+8801511009012", "https://booking.akmh.com/rashidayasmin"),
    Doctor("Dr. Shafiqur Rahman", 58, "Male", "Oncologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "shafiq.rahman@akmh.com", "+8801511009013", "https://booking.akmh.com/shafiqrahman"),
    Doctor("Dr. Rashida Begum", 46, "Female", "Pulmonologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.begum@akmh.com", "+8801511009014", "https://booking.akmh.com/rashidabegum"),
    Doctor("Dr. Nurul Hasan", 51, "Male", "Nephrologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "nurul.hasan@akmh.com", "+8801511009015", "https://booking.akmh.com/nurulhasan"),
    Doctor("Dr. Rashida Akter", 48, "Female", "Rheumatologist", [
           "MBBS", "MD"], "Anwer Khan Modern Hospital", "rashida.akter@akmh.com", "+8801511009016", "https://booking.akmh.com/rashidaakter"),
    Doctor("Dr. Shahjalal Miah", 55, "Male", "Cardiothoracic Surgeon", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "shahjalal.miah@akmh.com", "+8801511009017", "https://booking.akmh.com/shahjalalmiha"),
    Doctor("Dr. Rashida Islam", 39, "Female", "Hematologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.islam@akmh.com", "+8801511009018", "https://booking.akmh.com/rashidaislam"),
    Doctor("Dr. Shahidul Islam", 50, "Male", "Plastic Surgeon", [
           "MBBS", "MS"], "Anwer Khan Modern Hospital", "shahid.islam@akmh.com", "+8801511009019", "https://booking.akmh.com/shahidislam"),
    Doctor("Dr. Rashida Rahman", 44, "Female", "Emergency Medicine", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.rahman@akmh.com", "+8801511009020", "https://booking.akmh.com/rashidarahman"),
    Doctor("Dr. Abdur Rouf", 59, "Male", "General Physician", [
           "MBBS"], "Anwer Khan Modern Hospital", "abdur.rouf@akmh.com", "+8801511009021", "https://booking.akmh.com/abdurrouf"),
    Doctor("Dr. Rashida Haque", 37, "Female", "Family Medicine", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.haque@akmh.com", "+8801511009022", "https://booking.akmh.com/rashidahaque"),
    Doctor("Dr. Asaduzzaman Khan", 54, "Male", "Interventional Cardiologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "asad.khan@akmh.com", "+8801511009023", "https://booking.akmh.com/asadkhan"),
    Doctor("Dr. Rashida Sultana", 49, "Female", "Pediatric Neurologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.sultana@akmh.com", "+8801511009024", "https://booking.akmh.com/rashidasultana"),
    Doctor("Dr. Masudur Rahman", 46, "Male", "Spine Surgeon", [
           "MBBS", "MS"], "Anwer Khan Modern Hospital", "masud.rahman@akmh.com", "+8801511009025", "https://booking.akmh.com/masudrahman"),
    Doctor("Dr. Rashida Ahmed", 41, "Female", "Gynecologic Oncologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.ahmed@akmh.com", "+8801511009026", "https://booking.akmh.com/rashidaahmed"),
    Doctor("Dr. Mahfuz Ahmed", 57, "Male", "Hepatologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "mahfuz.ahmed@akmh.com", "+8801511009027", "https://booking.akmh.com/mahfuzahmed"),
    Doctor("Dr. Rashida Khatun", 43, "Female", "Neonatologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.khatun@akmh.com", "+8801511009028", "https://booking.akmh.com/rashidakhatun"),
    Doctor("Dr. Zakir Hossain", 48, "Male", "Vascular Surgeon", [
           "MBBS", "MS"], "Anwer Khan Modern Hospital", "zakir.hossain@akmh.com", "+8801511009029", "https://booking.akmh.com/zakirhossain"),
    Doctor("Dr. Rashida Yasmin", 36, "Female", "Infectious Disease", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.yasmin@akmh.com", "+8801511009030", "https://booking.akmh.com/rashidayasmin"),
    Doctor("Dr. Shamsul Alam", 62, "Male", "Thoracic Surgeon", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "shamsul.alam@akmh.com", "+8801511009031", "https://booking.akmh.com/shamsulalam"),
    Doctor("Dr. Rashida Parvin", 47, "Female", "Critical Care", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.parvin@akmh.com", "+8801511009032", "https://booking.akmh.com/rashidaparvin"),
    Doctor("Dr. Abdus Salam", 52, "Male", "Radiation Oncologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "abdus.salam@akmh.com", "+8801511009033", "https://booking.akmh.com/abdussalam"),
    Doctor("Dr. Rashida Khan", 38, "Female", "Diabetologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.khan@akmh.com", "+8801511009034", "https://booking.akmh.com/rashidakhan"),
    Doctor("Dr. Shahidul Hasan", 53, "Male", "Pain Medicine", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "shahid.hasan@akmh.com", "+8801511009035", "https://booking.akmh.com/shahidhasan"),
    Doctor("Dr. Rashida Miah", 40, "Female", "Allergist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.miah@akmh.com", "+8801511009036", "https://booking.akmh.com/rashidamiah"),
    Doctor("Dr. Motiur Rahman", 56, "Male", "Hand Surgeon", [
           "MBBS", "MS"], "Anwer Khan Modern Hospital", "moti.rahman@akmh.com", "+8801511009037", "https://booking.akmh.com/motirahman"),
    Doctor("Dr. Rashida Begum", 42, "Female", "Sleep Medicine", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.begum@akmh.com", "+8801511009038", "https://booking.akmh.com/rashidabegum"),
    Doctor("Dr. Shafiqul Hasan", 49, "Male", "Geriatrician", [
           "MBBS", "MD"], "Anwer Khan Modern Hospital", "shafiq.hasan@akmh.com", "+8801511009039", "https://booking.akmh.com/shafiqhasan"),
    Doctor("Dr. Rashida Rahman", 45, "Female", "Reproductive Endocrinologist", [
           "MBBS", "FCPS"], "Anwer Khan Modern Hospital", "rashida.rahman@akmh.com", "+8801511009040", "https://booking.akmh.com/rashidarahman"),
]
