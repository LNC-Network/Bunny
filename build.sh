
set -e

# Check if Python is installed
if ! command -v python3 &>/dev/null && ! command -v python &>/dev/null && ! command -v py &>/dev/null; then
    echo "Python not installed"
    exit 1
fi

# Install dependencies
if ! pip install -r requirements.txt; then
    echo "Failed to install requirements"
    exit 1
fi

# Build with PyInstaller
if ! pyinstaller --onefile src/main.py; then
    echo "Failed to build"
    exit 1
fi

echo "Build successful!"

# Delete the "build" folder
if [ -d "build" ]; then
    rm -rf build
    if [ $? -ne 0 ]; then
        echo "Failed to clear build folder"
        exit 1
    fi
fi

exit 0
