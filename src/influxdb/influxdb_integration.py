# influxdb_integration.py
import influxdb

class InfluxDBIntegration:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.client = None

    def connect(self):
        self.client = influxdb.InfluxDBClient(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            database=self.database
        )

    def write_data(self, data):
        if not self.client:
            self.connect()
        self.client.write_points(data)

    def query_data(self, query):
        if not self.client:
            self.connect()
        result = self.client.query(query)
        return result
