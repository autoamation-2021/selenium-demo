from faker import Faker
import pandas as pd

fake = Faker()
num_records = 20000
custom_domain = "iverbinden.com"

data = {
    "Name": [fake.name() for _ in range(num_records)],
    "Email": [fake.user_name() + "@" + custom_domain for _ in range(num_records)]
}

df = pd.DataFrame(data)
df.to_excel("dummy_users.xlsx", index=False)

print("Excel file with dummy names and emails created successfully!")
