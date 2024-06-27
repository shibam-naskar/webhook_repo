FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV MONGO_URI=mongodb://localhost:27017/ACTIONS
CMD python ./run.py