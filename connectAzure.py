import pyodbc
from flask import Flask
from datetime import timedelta

# Load the JSON data
database_info = {
    "sku": {
        "name": "Basic",
        "tier": "Basic",
        "capacity": 5
    },
    "kind": "v12.0,user",
    "properties": {
        "collation": "SQL_Latin1_General_CP1_CI_AS",
        "maxSizeBytes": 2147483648,
        "status": "Online",
        "databaseId": "d6460bb1-c2b5-4de8-a40d-463cec6f13ce",
        "creationDate": "2023-05-15T13:39:16.023Z",
        "currentServiceObjectiveName": "Basic",
        "requestedServiceObjectiveName": "Basic",
        "defaultSecondaryLocation": "westeurope",
        "catalogCollation": "SQL_Latin1_General_CP1_CI_AS",
        "zoneRedundant": False,
        "earliestRestoreDate": "2023-09-17T20:34:19.8505729Z",
        "readScale": "Disabled",
        "currentSku": {
            "name": "Basic",
            "tier": "Basic",
            "capacity": 5
        },
        "currentBackupStorageRedundancy": "Geo",
        "requestedBackupStorageRedundancy": "Geo",
        "maintenanceConfigurationId": "/subscriptions/06979191-7c74-4488-be38-b5531c780659/providers/Microsoft.Maintenance/publicMaintenanceConfigurations/SQL_Default",
        "isLedgerOn": False,
        "isInfraEncryptionEnabled": False,
        "availabilityZone": "NoPreference"
    },
    "location": "northeurope",
    "tags": {},
    "id": "/subscriptions/06979191-7c74-4488-be38-b5531c780659/resourceGroups/BadmintonSQL/providers/Microsoft.Sql/servers/badmintonsql/databases/Managerspil",
    "name": "Managerspil",
    "type": "Microsoft.Sql/servers/databases"
}

# Extract the relevant information
server = 'badmintonsql.database.windows.net'
database = database_info["name"]  # Use the database name from the JSON
username = 'Asgerfn'
password = 'Asger410'  # Replace with your actual Azure SQL Database password
driver = '{ODBC Driver 18 for SQL Server}'  # Use the appropriate driver version

conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected to Azure SQL Database successfully")
except Exception as e:
    print(f"Error connecting to Azure SQL Database: {str(e)}")

app = Flask(__name__)
app.secret_key = "Asger410!Asger410!"
app.config['SECRET_KEY'] = 'Asger410!Asger410!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=30)
"""server = 'badmintonsql.database.windows.net'
database = 'Managerspil'
username = 'Asgerfn'
password = '{Asger410}'
driver= '{ODBC Driver 18 for SQL Server}'
conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
"""
