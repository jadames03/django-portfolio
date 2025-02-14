# build_files.sh
# Set Python path
export PYTHONPATH="/vercel/path0:${PYTHONPATH}"

# Install requirements
python3.9 -m ensurepip
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Collect static files for S3
python3.9 manage.py collectstatic --no-input