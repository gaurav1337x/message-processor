# Message Processor
A simple application demonstrating:
Git -> GitHub -> Streamlit -> FastAPI -> Docker 

## Run locally

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Start the API from this directory with:

```powershell
python -m uvicorn api:app --reload --port 9000
```

In a second terminal, start the Streamlit client:

```powershell
streamlit run app.py
```