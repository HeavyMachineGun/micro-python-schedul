
from models.configuration import Configuration
from apscheduler.job import Job

class ServiceGetCurrencies: 
    def do_work(configuration: Configuration):
        print(f"doing some work for {configuration.name}")
