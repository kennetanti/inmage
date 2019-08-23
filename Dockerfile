FROM python:2.7

RUN mkdir /pybin
WORKDIR /pybin
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY *.py ./

ENTRYPOINT ["python", "inmage.py"]
