import contextlib
import uvicorn
from fastapi import FastAPI
from adder import mcp as adder_mcp
from suber import mcp as suber_mcp

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(adder_mcp.session_manager.run())
        await stack.enter_async_context(suber_mcp.session_manager.run())
        yield

app = FastAPI(lifespan=lifespan)
app.mount("/adder", adder_mcp.streamable_http_app())
app.mount("/suber", suber_mcp.streamable_http_app())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
