import sqlite3

# Connect to your database file
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Sample access log entries
logs = [
    ('2024-06-27 12:00:00', 'TenantA', 'Login'),
    ('2024-06-27 12:01:00', 'TenantB', 'Download Report'),
    ('2024-06-27 12:02:00', 'TenantA', 'Logout'),
]

# Insert data
cursor.executemany("INSERT INTO access_logs (time, tenant, action) VALUES (?, ?, ?)", logs)
conn.commit()
conn.close()

print("✅ Sample data inserted.")
