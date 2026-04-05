#!/bin/bash

# 1. Automatically detect system environment
CURRENT_USER=$(whoami)
CURRENT_DIR=$(pwd)

echo "------------------------------------------------"
echo "🚀 Starting System Maintenance Installation..."
echo "👤 Target User: $CURRENT_USER"
echo "📂 Script Location: $CURRENT_DIR"
echo "------------------------------------------------"

# 2. Create a temporary service file to avoid modifying the template
cp maintenance.service maintenance.service.tmp

# 3. Inject real paths and user data into the service template
# We use 'sed' to replace placeholders with actual system values
echo "🔧 Configuring systemd service unit..."
sed -i "s|USER_NAME|$CURRENT_USER|g" maintenance.service.tmp
sed -i "s|REPO_PATH|$CURRENT_DIR|g" maintenance.service.tmp

# 4. Move the configured service to system directory and activate
echo "📦 Deploying service to systemd..."
sudo mv maintenance.service.tmp /etc/systemd/system/maintenance.service
sudo systemctl daemon-reload
sudo systemctl enable maintenance.service

echo "------------------------------------------------"
echo "✅ Setup successful! Your HP laptop is now"
echo "   configured for automatic maintenance on boot."
echo "------------------------------------------------"
