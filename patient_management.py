def search_patients(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    return result


patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"},
]

search_disease = "Flu"
result = search_patients(patients, search_disease)
print(f"Patients with {search_disease}: {result}")
