FROM python:3.10

EXPOSE 8501

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

WORKDIR /app/flight prices

CMD streamlit run app.py