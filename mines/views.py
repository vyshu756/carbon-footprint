from django.shortcuts import render
from .models import ActivityData, EmissionFactor
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64
from collections import defaultdict


def dashboard(request):
    # -----------------------------
    # Calculate emissions
    # -----------------------------
    emissions = defaultdict(float)

    activities = ActivityData.objects.all()
    factors = {e.source: e.co2_per_unit for e in EmissionFactor.objects.all()}

    for a in activities:
        if a.category in factors:
            emissions[a.category] += a.quantity * factors[a.category]

    labels = list(emissions.keys())
    values = list(emissions.values())

    total_emission = sum(values)

    # -----------------------------
    # Calculate percentage (TEXT)
    # -----------------------------
    percentages = {}
    if total_emission > 0:
        for label, value in zip(labels, values):
            percentages[label] = round((value / total_emission) * 100, 2)

    # -----------------------------
    # BAR CHART (SMALL)
    # -----------------------------
    plt.figure(figsize=(4, 3))
    plt.bar(labels, values,color='green')
    plt.ylabel("CO₂ Emissions (kg)")
    plt.title("Emissions by Source")
    plt.tight_layout()

    bar_buf = io.BytesIO()
    plt.savefig(bar_buf, format='png')
    bar_buf.seek(0)
    bar_chart = base64.b64encode(bar_buf.getvalue()).decode()
    plt.close()

    # -----------------------------
    # PIE CHART (WITH %)
    # -----------------------------
    plt.figure(figsize=(4, 3))
    plt.pie(
        values,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Carbon Emission Share")
    plt.tight_layout()

    pie_buf = io.BytesIO()
    plt.savefig(pie_buf, format='png')
    pie_buf.seek(0)
    pie_chart = base64.b64encode(pie_buf.getvalue()).decode()
    plt.close()

    return render(request, "dashboard.html", {
        "bar_chart": bar_chart,
        "pie_chart": pie_chart,
        "percentages": percentages,
        "total_emission": round(total_emission, 2)
    })



