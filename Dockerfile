# using python ver 3.9 found on dockerhub
FROM python:3.9

# Create the working directory for app
WORKDIR /danbooru_bot

# copy th requirements.txt file into the working directory
COPY requirements.txt .

# Run PIP and install items rom requirements .txt
RUN pip install -r requirements.txt

#Since I have multiple files use copy instead of add
COPY ./app ./app

CMD [ "python", "./app/bot.py"]