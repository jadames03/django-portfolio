# build_files.sh
# Set Python path
export PYTHONPATH="/vercel/path0:${PYTHONPATH}"

# Install requirements directly with python3.9
python3.9 -m ensurepip
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Run collectstatic
python3.9 manage.py collectstatic --noinput 