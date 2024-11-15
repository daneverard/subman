from django.test import TestCase
from freezegun import freeze_time
from .models import SubscriptionPlan  # Adjust this import to your actual model path
from datetime import date, timedelta

class SubscriptionPlanTests(TestCase):
    
    @freeze_time("2024-01-15")
    def test_is_active(self):
        today = date(2024, 1, 15)

        # Case 1: start_date is before today, end_date is after today (should be active)
        plan = SubscriptionPlan.objects.create(
            start_date=today - timedelta(days=10),
            end_date=today + timedelta(days=10)
        )
        self.assertTrue(plan.is_active, "Expected is_active to be True when within start and end dates")

        # Case 2: start_date is before today, end_date is today (should be inactive)
        plan.end_date = today
        plan.save()
        self.assertFalse(plan.is_active, "Expected is_active to be False when end_date is today")

        # Case 3: start_date and end_date are both before today (should be inactive)
        plan.end_date = today - timedelta(days=1)
        plan.save()
        self.assertFalse(plan.is_active, "Expected is_active to be False when end_date is in the past")

        # Case 4: start_date is after today, end_date is also after today (should be inactive)
        plan.start_date = today + timedelta(days=5)
        plan.end_date = today + timedelta(days=10)
        plan.save()
        self.assertFalse(plan.is_active, "Expected is_active to be False when start_date is in the future")

        # Case 5: start_date is before today, end_date is None (should be active)
        plan.start_date = today - timedelta(days=10)
        plan.end_date = None
        plan.save()
        self.assertTrue(plan.is_active, "Expected is_active to be True when end_date is None and start_date is in the past")