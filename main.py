from fastapi import FastAPI

# print( "begin...")
app = FastAPI()

@app.get( "/")
def read_root():
    return { "Hello": "瘋狂的FastAPI, 這里是分支 sub1/sub2_1"}

@app.get( "/blog/{id}")
def get_blog( id: int):
    return { "data": f"Blog id:{id}"}
