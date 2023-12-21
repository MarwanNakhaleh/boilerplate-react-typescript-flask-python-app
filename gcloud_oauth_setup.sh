## THIS SCRIPT IS NOT USED. IT IS HERE FOR REFERENCE ONLY.

#!/bin/bash

# gcloud auth login
# gcloud config set project <project-id>
# gcloud services enable iap.googleapis.com --project <your-project-id>

# Variables
CLIENT_NAME="BoilerplateApp" # Change this to your client name
PROJECT_ID="$(gcloud config get-value project)" # Gets the current project ID
SUPPORT_EMAIL="email@example.com"
REDIRECT_URIS=("http://localhost:3000" "https://boilerplate-ui.example.com") # Add your redirect URIs
JAVASCRIPT_ORIGINS=("http://localhost:3000" "https://boilerplate-ui.example.com") # Add your JavaScript origins

# Convert arrays to comma-separated strings
REDIRECT_URIS_STR=$(IFS=,; echo "${REDIRECT_URIS[*]}")
JAVASCRIPT_ORIGINS_STR=$(IFS=,; echo "${JAVASCRIPT_ORIGINS[*]}")

# Create OAuth 2.0 credentials
# Check if an OAuth brand already exists
BRAND=$(gcloud iap oauth-brands list --format="value(name)" --project="$PROJECT_ID")
if [ -z "$BRAND" ]; then
    # Create a new OAuth brand if it doesn't exist
    gcloud iap oauth-brands create --application_title="$CLIENT_NAME" --project="$PROJECT_ID" --support_email="$SUPPORT_EMAIL"
    BRAND=$(gcloud iap oauth-brands list --format="value(name)" --filter="applicationTitle:$CLIENT_NAME" --project="$PROJECT_ID")
fi
# Create the OAuth client
gcloud iap oauth-clients create $BRAND --display_name="$CLIENT_NAME" --project="$PROJECT_ID" # --redirect_uris="$REDIRECT_URIS_STR" --javascript_origins="$JAVASCRIPT_ORIGINS_STR"
