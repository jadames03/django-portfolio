# build_files.sh
# Set Python path
export PYTHONPATH="/vercel/path0:${PYTHONPATH}"

# Install requirements
python3.9 -m ensurepip
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Create staticfiles directory and collect static files
rm -rf staticfiles/*  # Clean the directory first
python3.9 manage.py collectstatic --no-input --clear 