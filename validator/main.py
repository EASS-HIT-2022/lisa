import time
import database.handlers as handlers
import datetime


if __name__ == '__main__':
    print("validating events...")

    while True:
        handlers.validate_events()
        print(str(datetime.date) + " - validated")

        # sleep until 12AM
        t = datetime.datetime.today()
        future = datetime.datetime(t.year, t.month, t.day, 0, 0)
        if t.hour >= 0:
            future += datetime.timedelta(days=1)
        time.sleep((future - t).total_seconds())
