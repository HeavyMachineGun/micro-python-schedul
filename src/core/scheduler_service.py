from importlib import import_module
import os
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from repositories.scheduler_configuration import SchedulerConfiguration

class SchedulerService:

    def __init__(self,configuration_repo= SchedulerConfiguration()) -> None:
        self.configuration_repo= configuration_repo

        service_name = self.__class__.__name__
        self.scheduler = SchedulerService.get_scheduler(service_name)

        self.scheduler.start()
        self.add_configuration_tasks()
        logging.info(f"scheduler {service_name} was started successfuly")
    
    @staticmethod
    def get_scheduler(scheduler_name):
        user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
        password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
        host = os.getenv("HOST")

        scheduler = AsyncIOScheduler()
        scheduler.add_jobstore("mongodb",collection=scheduler_name,username= user, password=password, host=host)
        
        return scheduler
        
    def add_configuration_tasks(self):
        configurations = self.configuration_repo.get_all_configurations()
        
        logging.info(f"Loading configurations as jobs")
        for configuration in configurations:
            
            module = import_module(f"core.tasks.{configuration.service_name}")
            _class = getattr(module,configuration.service_name,None)
            if(_class):
                
                instance = _class()
                
                if getattr(instance,"do_work",None):
                    
                    job = self.scheduler.add_job(instance.do_work, configuration.trigger,
                     id= configuration.id,
                     name=configuration.service_name,
                     trigger_args= configuration.trigger_args,
                     replace_existing=True, args={"configuration":configuration})
                    
                    logging.info(f"A job was created for service {configuration.service_name}")
                else:
                    logging.error(f"Not supported method: {'do_work'} for class service {configuration.service_name}")
        