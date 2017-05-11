"""
Textko platform for notify component.
For more details about this platform, please refer to the documentation at
https://github.com/textko/hass-notify
"""

# Import dependencies.
import logging
import requests
import json

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.notify import (
    PLATFORM_SCHEMA, BaseNotificationService)

# Get logger instance.
_LOGGER = logging.getLogger(__name__)

# Set platform  parameters.
CONF_API_URL_MSG = 'https://textko.com/api/v2/messages'
CONF_API_TOKEN = 'api_token'
CONF_TO_NO = 'to_no'

# Validate parameter schema.
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_TOKEN): cv.string,
    vol.Required(CONF_TO_NO): cv.string,
})

# Define service instance.
def get_service(hass, config, discovery_info=None):
    
    # Set notification service instance.
    return TextkoNotificationService(config[CONF_API_TOKEN], config[CONF_TO_NO])

# Implement the notification service.
class TextkoNotificationService(BaseNotificationService):
    """Implementation of a notification service for the Twitter service."""

    def __init__(self, access_token, to_no):
        
        # Set variables.
        self.access_token = access_token
        self.to_no = to_no

    def send_message(self, message="", **kwargs):

        # Send request.
        data = {'to_no': self.to_no, 'text': message}
        headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + self.access_token}

        resp = requests.post(CONF_API_URL_MSG, data=json.dumps(data), headers=headers)
        
        # Display error when failed.
        if resp.status_code != 200:
          
            obj = json.loads(resp.text)
            error_message = obj['response_msg']
            error_code = obj['http_code']
            _LOGGER.error("Error %s : %s (Code %s)", resp.status_code,
                          error_message, error_code)