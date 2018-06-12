#!/usr/bin/env python

from datadog import initialize, api
import time

options = {
    'api_key': '',
    'app_key': ''
}
initialize(**options)

# Mute all monitors
api.Monitor.mute_all()

print("All monitors are muted. Please run datadog_unmute.py to unmute the monitors.");
