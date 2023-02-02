# build_files.sh

echo "Building project..."
pip install -r requirements.txt

echo "Make migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect static"
python3.9 manage.py collectstatic --noinput --clear