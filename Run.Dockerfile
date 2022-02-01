FROM python
WORKDIR /app
COPY Pip* ./
RUN pip install pipenv
RUN pipenv install
COPY . .
CMD ["pipenv","run","python3","main.py","&&","bash"]