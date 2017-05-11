The `textko` platform uses [Textko](https://textko.com) to deliver notifications from Home Assistant.

### Installation
* Clone this repository.
* Copy `custom_components` folder to your Home Assistant `configuration folder`.

### Get your Textko API Token
Go to your [Textko Projects](https://textko.com/projects) section and create your new project. After creating your project, you should now be able to obtain your `API Token`.

### Configuration
To add Textko to your installation, add the following to your Home Assistant `configuration.yaml` file:

```yaml
notify:
  - platform: textko
    name: Textko
    api_token: {{YOUR TEXTKO API TOKEN}}
    to_no: {{YOUR MOBILE NO}}
```

Configuration variables:

* **name** (Optional): Setting the optional parameter name allows multiple notifiers to be created. The default value is `Textko`. The notifier will bind to the service notify.NOTIFIER_NAME.
* **api_token** (Required): Your `API Token` for your Textko project.
* **to_no** (Required): Your mobile no. This is where you want to send your notification messages. eg: `09171234567`


To use notifications, please see the [getting started with automation page](https://home-assistant.io/getting-started/automation/).
