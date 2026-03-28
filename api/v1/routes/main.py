# payment-processor/main.py

import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from payment_processor.schemas import PaymentSchema
from payment_processor.services import PaymentService

app = FastAPI()

class PaymentRequest(BaseModel):
    amount: float
    currency: str

payment_service = PaymentService()

@app.post("/payments/", response_model=PaymentSchema)
async def create_payment(payment_request: PaymentRequest):
    try:
        payment = payment_service.create_payment(payment_request)
        return payment
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/payments/{payment_id}", response_model=PaymentSchema)
async def get_payment(payment_id: str):
    try:
        payment = payment_service.get_payment(payment_id)
        return payment
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)