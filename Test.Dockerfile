FROM python
WORKDIR /app
COPY . .
RUN python3 full_test.py
CMD [ "bash" ,"test.sh"]