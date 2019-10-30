import requests

from datetime import timedelta
from django.db import models
from dashboard.models import Client
from dashboard.helpers import monthFirstDay

class API(models.Model):
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r})')

    def get(self, endpoint: str = ''):
        r = requests.get(
            "https://substrakt.freshdesk.com/api/v2/"+ endpoint,
            # authentication needs to come from env
            auth=("5TZvLFZ9pqTpCtdw1C", "x")
        )
        
        if r.status_code == 200:
            return r.json()

        return False

    def sync(self, request):
        for client in request:
            # The sla_hours field is an integer so we need to convert None to 0
            if client['custom_fields']['sla_allowance_hours'] is None:
                client['custom_fields']['sla_allowance_hours'] = 0

            print(f"Importing {client['name']}")

            c = Client(
                client_id=client['id'], 
                name=client['name'], 
                sla_hours=client['custom_fields']['sla_allowance_hours'], 
                time_spent=self._time_by_client(str(client['id']), str(monthFirstDay()))
            )
            c.save()

    def _time_by_client(self, client_id: str, start_time: str = ''):
        """Returns total tracked for for a client converted to minutes"""
        r = self.get(
            f"time_entries?company_id={client_id}&executed_after={start_time}"
        )
        total = 0

        for t in self._time_spent(r):
            total = total + timedelta(
                hours=int(t[0:2]),
                minutes=int(t[3:])
            ).seconds

        return total / 3600

    
    def _time_spent(self, time):
        """Adds all tracked time for a client"""
        tracked_time = []
        if time:
            for time_spent in time:
                tracked_time.append(time_spent.get('time_spent', 0))

        return tracked_time
