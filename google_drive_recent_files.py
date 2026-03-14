#!/usr/bin/env python3
"""Google Driveの最近のファイルを一覧表示するスクリプト"""

import os
import json
from datetime import datetime

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"


def get_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return creds


def list_recent_files(max_results=20):
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    results = service.files().list(
        pageSize=max_results,
        orderBy="viewedByMeTime desc,modifiedTime desc",
        fields="files(id, name, mimeType, modifiedTime, viewedByMeTime, size, webViewLink)",
        q="trashed=false",
    ).execute()

    files = results.get("files", [])
    return files


def format_size(size_str):
    if not size_str:
        return "-"
    size = int(size_str)
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def format_datetime(dt_str):
    if not dt_str:
        return "-"
    dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%d %H:%M")


MIME_TYPE_LABELS = {
    "application/vnd.google-apps.folder": "フォルダ",
    "application/vnd.google-apps.document": "Googleドキュメント",
    "application/vnd.google-apps.spreadsheet": "Googleスプレッドシート",
    "application/vnd.google-apps.presentation": "Googleスライド",
    "application/vnd.google-apps.form": "Googleフォーム",
    "application/pdf": "PDF",
    "image/jpeg": "JPEG画像",
    "image/png": "PNG画像",
    "video/mp4": "MP4動画",
    "text/plain": "テキスト",
}


def get_type_label(mime_type):
    return MIME_TYPE_LABELS.get(mime_type, mime_type.split("/")[-1])


def main():
    print("Google Drive - 最近のファイル一覧")
    print("=" * 70)

    files = list_recent_files(max_results=20)

    if not files:
        print("ファイルが見つかりませんでした。")
        return

    print(f"{'#':<3} {'ファイル名':<35} {'種類':<20} {'最終更新':<17} {'サイズ'}")
    print("-" * 70)

    for i, f in enumerate(files, 1):
        name = f.get("name", "")
        if len(name) > 33:
            name = name[:30] + "..."
        type_label = get_type_label(f.get("mimeType", ""))
        if len(type_label) > 18:
            type_label = type_label[:15] + "..."
        modified = format_datetime(f.get("modifiedTime"))
        size = format_size(f.get("size"))
        print(f"{i:<3} {name:<35} {type_label:<20} {modified:<17} {size}")

    print("-" * 70)
    print(f"合計: {len(files)} 件")

    print("\n詳細情報 (リンク付き):")
    print("-" * 70)
    for i, f in enumerate(files, 1):
        link = f.get("webViewLink", "リンクなし")
        print(f"{i:>2}. {f.get('name', '')}")
        print(f"    {link}")


if __name__ == "__main__":
    main()
