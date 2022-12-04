if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Sahidmalik07/pm_test.git /pm_test
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /pm_test
fi
cd /pm_test
pip3 install -U -r requirements.txt
echo "Starting Bot....💥"
python3 bot.py
