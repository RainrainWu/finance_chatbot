FROM python:3.6.8-slim

# Install Pipenv
RUN pip3 install pipenv==2018.11.26
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Install dependencies
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --sequential

COPY ./chatbot /chatbot
WORKDIR /chatbot

RUN useradd -ms /bin/bash guest
RUN chown -R guest:guest /chatbot
USER guest

CMD ["pipenv", "run", "python3", "app.py"]

