# OAuth2CalenderApp
A simple calender App created on Django.


## Installation (Development)

1. Create a new project in the Google Cloud Console and enable the Google Calendar API.

2. Create OAuth 2.0 credentials for your project. Under "Authorized redirect URIs", add `http://localhost:8000/rest/v1/calendar/redirect/` for local development.

3. Download `client_secret` file from the Google console and place it in the root directory of the project.

4. Run the following commands in your `CLI` to install the required dependencies
```bash
 $ pip3 install -r requirements.txt
```

5. Run the following commands in your `CLI` to run the development server
```bash
 $ pip3 install -r requirements.txt
```

## API Reference

- Django server is hosted on port `8000`.
- Client can use the App by accessing the URL `rest/rest/v1/calendar/init/` in the browser(recommended).
- Client will get the events next 10 events from current date and time. by the URL `rest/v1/calendar/redirect/`.
