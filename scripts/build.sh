#!/bin/bash
set -e

echo "=== OpenComposites Build Script ==="
echo ""

echo "[1/4] Installing Python dependencies..."
cd web-app/backend
pip install -r requirements.txt
cd ../..

echo ""
echo "[2/4] Installing Node dependencies..."
cd web-app/frontend
npm install

echo ""
echo "[3/4] Building frontend..."
npm run build

echo ""
cd ../..
echo "[4/4] Build complete!"
echo ""
echo "Frontend built to: web-app/frontend/dist/"
echo ""
echo "To start the server:"
echo "  cd web-app/backend && python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"
echo ""
echo "The app will be available at http://localhost:8000"
