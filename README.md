## Purpose

This repository is a custom HomeAssistant integration for provisioning Wiliot devices.  This is a WIP, as there are issues with using the synchronous Wiliot API with the asynchronous flow of HomeAssistant.

## Quick Fix

For a quick fix, you can append the following code to your `configuration.yaml` file in HomeAssistant to set up Wiliot Pixels as "REST sensors" (as seen [here](https://www.home-assistant.io/integrations/rest/)).

The code uses Wiliot's REST API to read sensor data; note that this requires storing your API credentials in plaintext, which is only recommended if you:
  1) Are using a secure compute environment for HomeAssistant
  2) Don't care about security
  3) Care about security, but also live on the wild side

```
#TODO: Bind to standard Wiliot API
rest:
  - authentication: basic
    username: "admin"
    password: "password"
    scan_interval: 60
    resource: https://api.wiliot.com/v1/
    sensor:
      - name: "Sensor 1"
        value_template: "{{ value_json.list[28] }}"
      - name: "Sensor 2"
        value_template: "{{ value_json.list[29] }}"
      - name: "Sensor 3"
        value_template: "{{ value_json.list[30] }}"
      etc...
```
