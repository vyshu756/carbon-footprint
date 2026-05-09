from .models import ActivityData, EmissionFactor

def calculate_emissions():
    results = {}

    activities = ActivityData.objects.all()

    for activity in activities:
        try:
            factor = EmissionFactor.objects.get(
                source=activity.category
            )
            emission = activity.quantity * factor.co2_per_unit
            results[activity.category] = results.get(activity.category, 0) + emission
        except EmissionFactor.DoesNotExist:
            continue

    return results

