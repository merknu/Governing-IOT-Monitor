# grafana_integration.py
import requests
import json

class GrafanaIntegration:
    def __init__(self, api_key, grafana_url):
        self.api_key = api_key
        self.grafana_url = grafana_url
        self.headers = {
            "Authorization": "Bearer {}".format(self.api_key),
            "Content-Type": "application/json"
        }
    
    def get_dashboards(self):
        dashboards_url = "{}/api/search".format(self.grafana_url)
        response = requests.get(dashboards_url, headers=self.headers)
        return response.json()
    
    def create_dashboard(self, dashboard_json):
        create_dashboard_url = "{}/api/dashboards/db".format(self.grafana_url)
        response = requests.post(create_dashboard_url, headers=self.headers, json=dashboard_json)
        return response.json()
    
    def update_dashboard(self, dashboard_uid, dashboard_json):
        update_dashboard_url = "{}/api/dashboards/uid/{}".format(self.grafana_url, dashboard_uid)
        response = requests.put(update_dashboard_url, headers=self.headers, json=dashboard_json)
        return response.json()
    
    def delete_dashboard(self, dashboard_uid):
        delete_dashboard_url = "{}/api/dashboards/uid/{}".format(self.grafana_url, dashboard_uid)
        response = requests.delete(delete_dashboard_url, headers=self.headers)
        return response.json()
