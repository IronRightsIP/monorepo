from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class LicenseRequest(BaseModel):
    nft_id: str
    usage: str

@app.post("/generate-license")
async def generate_license(data: LicenseRequest):
    return {
        "nft_id": data.nft_id,
        "usage": data.usage,
        "terms": "Standard non-exclusive license",
        "price": "0.05 ETH"
    }
