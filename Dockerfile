FROM python:3.12.9-slim
COPY . .
RUN pip install -r requirements.txt 
EXPOSE 8501
CMD ["streamlit", "run", "app.py","--port","8501:8501","--host","0.0.0.0"]