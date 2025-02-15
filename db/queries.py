import init_django_orm  # noqa: F401

from django.db.models import QuerySet, Q, F

from db.models import LoyaltyProgram, LoyaltyProgramParticipant, Customer


def all_loyalty_program_names() -> QuerySet:
    return LoyaltyProgram.objects.all().values_list("name", "bonus_percentage")


def not_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__range=("2021-01-01", "2021-12-31")
    ).values("customer__first_name")


def most_active_customers() -> QuerySet:
    return LoyaltyProgramParticipant.objects.order_by(
        "-sum_of_spent_money"
    ).values_list(
        "customer__first_name", "customer__last_name", "sum_of_spent_money"
    )[:5]


def clients_with_i_and_o() -> QuerySet:
    return Customer.objects.filter(
        Q(last_name__icontains="o") | Q(first_name__startswith="i")
    )


def bonuses_less_then_spent_money() -> QuerySet:
    return LoyaltyProgramParticipant.objects.filter(
        active_bonuses__lt=F("sum_of_spent_money")
    ).values("customer__phone_number")
