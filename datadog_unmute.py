#!/usr/bin/python

from datadog import initialize, api
import time

options = {
    'api_key': '',
    'app_key': ''
}
initialize(**options)

# Unmute all alerts
api.Monitor.unmute_all()

print("All monitors are now unmuted.");
