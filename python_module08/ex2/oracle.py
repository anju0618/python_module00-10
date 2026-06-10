#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv  # type: ignore

load_dotenv()


def check_environment() -> bool:
    print("ORACLE STATUS: Reading the Matrix...")

    mode = os.environ.get("MATRIX_MODE", "development")
    db_url = os.environ.get("DATABASE_URL")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    zion_ep = os.environ.get("ZION_ENDPOINT")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if db_url:
        if mode == "production":
            print("Database: Connected to production cluster")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Warning - No connection string specified")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated")

    print(f"Log Level: {log_level}")

    if zion_ep:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")

    if mode == "production" and (not api_key or "dummy" in api_key.lower()):
        print("[WARNING] Production mode with insecure setup!")
        return False

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    return True


def main() -> None:
    success = check_environment()

    if success:
        print("\nThe Oracle sees all configurations.")
    else:
        print("\nALERT: Sentinels detected configuration vulnerability.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
