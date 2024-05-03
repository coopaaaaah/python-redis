
#=================================
# BUILDER IMAGE
#=================================
FROM python:3.11-slim-bookworm as builder

WORKDIR /home/root/app
RUN apt update && apt install -y libpq-dev
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./

# Creates a virtual env using --copies to avoid symlinks
# Then use pipenv to install dependencies in this exact newly created env
RUN python -m venv --copies venv && \
  . ./venv/bin/activate && \
  pipenv install --deploy --ignore-pipfile --dev

#=================================
# RUNNER IMAGE
#=================================
FROM python:3.11-slim-bookworm


WORKDIR /home/root/app
COPY . .
COPY --from=builder /home/root/app/venv /home/root/app/venv

CMD ["/home/root/app/venv/bin/python3", "main.py"]