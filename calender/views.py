from datetime import datetime
from django.shortcuts import redirect
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def GoogleCalendarInitView(request):
    flow = Flow.from_client_secrets_file(
        './client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        redirect_uri='http://localhost:8000/rest/v1/calendar/redirect/',
    )

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
    )
    request.session['google_auth_state'] = state
    return redirect(authorization_url)

@api_view(["GET"])
def GoogleCalendarRedirectView(request):
    state = request.session.get('google_auth_state', None)
    flow = Flow.from_client_secrets_file(
        './client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        state=state,
        redirect_uri='http://localhost:8000/rest/v1/calendar/redirect/',
    )
    authorization_response = request.build_absolute_uri()
    if "http:" in authorization_response:
        authorization_response = "https:" + authorization_response[5:]
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    service = build('calendar', 'v3', credentials=credentials)
    events_result = service.events().list(calendarId='primary', timeMin=datetime.utcnow().isoformat() + 'Z',
                                        maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    return Response(status=200,data=events)
