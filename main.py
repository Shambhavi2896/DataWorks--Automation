from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    try:
        # TODO: Implement task parsing and execution
        return {"message": f"Task '{task}' executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str):
    try:
        if not path.startswith("/data/"):
            raise HTTPException(status_code=400, detail="Invalid path")
        
        full_path = os.path.join(os.getcwd(), path.lstrip("/"))
        if not os.path.exists(full_path):
            raise HTTPException(status_code=404, detail="File not found")
        
        with open(full_path, "r") as file:
            content = file.read()
        return {"content": content}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)