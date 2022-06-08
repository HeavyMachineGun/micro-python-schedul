
from unittest import mock
from uuid import uuid4
from core.scheduler_service import SchedulerService
from models.configuration import Configuration
from repositories.scheduler_configuration import SchedulerConfiguration
from unittest.mock import  MagicMock, patch

def test_id_configuration_model():
    config = Configuration(name = "test",job_id = "job_id",
    trigger = "",
    trigger_args= {},
    service_name="name")
    assert config.id != None

def test_new_configuration_model():
    uuid = str(uuid4())
    config = Configuration(id=uuid,
    name = "test",job_id = "job_id",
    trigger = "",
    trigger_args= {},
    service_name="name")
    assert str(config.id) == uuid

@patch("core.client_factory.MongoClientFactory.get_collection_client")
@patch("apscheduler.schedulers.asyncio.AsyncIOScheduler.add_jobstore", autospec=True)
@patch("apscheduler.schedulers.asyncio.AsyncIOScheduler.add_job")
def test_reflection_classes(add_job_mock: MagicMock,scheduler_mock: MagicMock,mongo_client: MagicMock):
    configurations=[
        Configuration(name="test_configuration",
        trigger="interval",
        trigger_args= { "seconds": 20},
        service_name= "ServiceGetCurrencies")
    ]
    
    with patch.object(SchedulerConfiguration,"get_all_configurations",return_value = configurations) as mock:
        scheduler = SchedulerService()
        scheduler.add_configuration_tasks()
    
    add_job_mock.assert_called_once()