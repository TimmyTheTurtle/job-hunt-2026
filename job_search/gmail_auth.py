#!/usr/bin/env python3
"""
Gmail OAuth 2.0 authentication helper.

On first run, opens a browser so you can grant access.
Caches the resulting token to secrets/gmail_token.json for subsequent runs.

Required scope: https://www.googleapis.com/auth/gmail.modify
  (read messages, apply/remove labels, mark read — no delete)
"""

from __future__ import annotations

from pathlib import Path

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


ROOT = Path(__file__).resolve().parents[1]
SECRETS = ROOT / "secrets"
CREDENTIALS_FILE = SECRETS / "gmail_credentials.json"
TOKEN_FILE = SECRETS / "gmail_token.json"

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def get_gmail_service():
    """Return an authenticated Gmail API service object.

    On the first call, opens a browser window for OAuth consent.
    After that, the cached token in secrets/gmail_token.json is reused
    and silently refreshed when it expires.
    """
    if not CREDENTIALS_FILE.exists():
        raise SystemExit(
            f"\nGmail credentials not found at:\n  {CREDENTIALS_FILE}\n\n"
            "Download OAuth 2.0 Desktop credentials from Google Cloud Console\n"
            "and save them to that path.\n"
            "See HOW_TO_RUN_JOB_SEARCH.md — Gmail Triage Setup for step-by-step instructions."
        )

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                creds = None
        else:
            creds = None

        if not creds:
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0, open_browser=False)
        TOKEN_FILE.write_text(creds.to_json())

    return build("gmail", "v1", credentials=creds)
