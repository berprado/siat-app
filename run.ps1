Start-Process powershell -ArgumentList 'cd backend; uvicorn main:app --reload'
Start-Process powershell -ArgumentList 'cd frontend/siat-ui; npm run dev'
