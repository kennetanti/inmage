# inmage
programmatically find inmates by state and last name

# docker build
git clone https://github.com/kennetanti/inmage
cd inmage
docker build -t inmage .
## run search
docker run -it inmage PA garcia
or
docker run -it inmage PA garcia jose

docker run -it inmage <state> <last name> [first name]

# boring way
apt -y update; apt -y install git python-pip;
git clone https://github.com/kennetanti/inmage; cd inmage; pip install -r requirements.txt

## run search
python inmage.py PA garcia
or
python inmage.py PA garcia jose

python inmage.py <state> <last name> [first name]

# NOTICE
this tool is basic as shit and basically useless
i wrote it for something, and now you are reading this for some reason.
