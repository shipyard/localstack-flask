#!/bin/bash

if [ ${DEV:-False} = 'true' ]; then
  # Run celery in the background
  # NOTE: -B is for the heartbeat task scheduler
  poetry run celery -B \
    -A src.entry.celery worker \
    --loglevel=info \
    --pidfile=/var/run/celery/worker.pid
    #--pidfile=/var/run/celery/worker.pid &

  # Trigger a celery reload whenever a file changes
  #watchman-make \
    #--root '/srv' \
    #-p 'src/**' \
    #--make 'bash' \
    #-t '/entrypoints/restart-worker.sh'
else
  # Run celery in the foreground
  poetry run celery -B \
    -A src.entry.celery worker \
    --loglevel=info
fi
