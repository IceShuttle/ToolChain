FROM python
WORKDIR /app
COPY . .
RUN python3 main-test.py
CMD [ "bash" ,"test.sh"]