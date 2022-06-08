import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

def tick():
    print('Tick! The time is: %s' % datetime.now())

def test_scheduler():
    scheduler = AsyncIOScheduler()
    user = "scheduler-trading-2022"
    password = "sch3dul3r-tr4d1ng-2022" 
    scheduler.add_jobstore("mongodb",collection="test-collection",username=user, password=password)
    scheduler.start()
    scheduler.remove_all_jobs()
    scheduler.add_job(tick, 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    
    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        scheduler.shutdown(True)
    except (KeyboardInterrupt, SystemExit):
        pass
    assert scheduler.running == True