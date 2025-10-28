#exit on error
set -o errexit

pip install -r requitements.txt

python manage.py collectstatic --no-input
python manage.py migrate