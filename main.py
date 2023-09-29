import uvicorn
# running server
if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)