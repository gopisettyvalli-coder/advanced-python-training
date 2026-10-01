environment = "development"

if environment == "development":
    database = "development_db"
elif environment == "production":
    database = "production_db"

print("Environment:", environment)
print("Database:", database)