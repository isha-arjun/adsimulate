from math import ceil
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(
    title="AdSimulate API",
    version="0.1.0",
    description=(
        "Deterministic campaign-economics calculations based on "
        "user-supplied assumptions. These are scenarios, not forecasts."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://adsimulate.vercel.app",
        "https://adsimulate-clear-board.vercel.app",
        "http://localhost:3000",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class SimulationInput(BaseModel):
    currency: str = Field(default="INR", min_length=3, max_length=3)
    selling_price: float = Field(gt=0)
    product_cost: float = Field(ge=0)
    variable_cost_per_order: float = Field(default=0, ge=0)
    ad_spend: float = Field(ge=0)
    cpm: float = Field(gt=0, description="Cost per 1,000 impressions")
    ctr_percent: float = Field(ge=0, le=100)
    click_to_purchase_percent: float = Field(ge=0, le=100)


class SimulationOutput(BaseModel):
    model_type: str
    not_a_forecast: bool
    currency: str
    impressions: float
    clicks: float
    estimated_orders: float
    revenue: float
    product_and_variable_costs: float
    contribution_before_ad_spend: float
    estimated_profit_after_ad_spend: float
    contribution_per_order: float
    break_even_orders: Optional[int]
    estimated_cac: Optional[float]
    roas: Optional[float]
    roi_percent: Optional[float]


@app.get("/")
def root():
    return {
        "name": "AdSimulate API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/api/v1/health",
    }


@app.get("/api/v1/health")
def health():
    return {"status": "ok", "service": "adsimulate-api", "version": "0.1.0"}


@app.post("/api/v1/simulate", response_model=SimulationOutput)
def simulate(data: SimulationInput):
    impressions = (
        data.ad_spend / data.cpm * 1000 if data.cpm > 0 else 0.0
    )
    clicks = impressions * data.ctr_percent / 100
    orders = clicks * data.click_to_purchase_percent / 100
    revenue = orders * data.selling_price
    costs = orders * (
        data.product_cost + data.variable_cost_per_order
    )
    contribution = revenue - costs
    profit = contribution - data.ad_spend
    contribution_per_order = (
        data.selling_price
        - data.product_cost
        - data.variable_cost_per_order
    )

    break_even_orders = (
        ceil(data.ad_spend / contribution_per_order)
        if contribution_per_order > 0
        else None
    )
    cac = data.ad_spend / orders if orders > 0 else None
    roas = revenue / data.ad_spend if data.ad_spend > 0 else None
    roi = profit / data.ad_spend * 100 if data.ad_spend > 0 else None

    return SimulationOutput(
        model_type="deterministic_scenario",
        not_a_forecast=True,
        currency=data.currency.upper(),
        impressions=impressions,
        clicks=clicks,
        estimated_orders=orders,
        revenue=revenue,
        product_and_variable_costs=costs,
        contribution_before_ad_spend=contribution,
        estimated_profit_after_ad_spend=profit,
        contribution_per_order=contribution_per_order,
        break_even_orders=break_even_orders,
        estimated_cac=cac,
        roas=roas,
        roi_percent=roi,
    )
