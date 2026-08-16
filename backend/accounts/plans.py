"""Subscription plans that gate picture templates."""

PLAN_BRONZE = "bronze"
PLAN_SILVER = "silver"
PLAN_GOLD = "gold"

PLAN_CHOICES = (
    (PLAN_BRONZE, "Bronze"),
    (PLAN_SILVER, "Silver"),
    (PLAN_GOLD, "Gold"),
)

PLAN_RANK = {
    PLAN_BRONZE: 0,
    PLAN_SILVER: 1,
    PLAN_GOLD: 2,
}


def normalize_plan(plan):
    key = str(plan or PLAN_BRONZE).strip().lower()
    if key not in PLAN_RANK:
        return PLAN_BRONZE
    return key


def allowed_plans_for(plan):
    rank = PLAN_RANK[normalize_plan(plan)]
    return [name for name, value in PLAN_RANK.items() if value <= rank]


def user_plan(user):
    return normalize_plan(getattr(user, "plan", None))


def is_impersonating(request):
    token = getattr(request, "auth", None)
    if token is None:
        return False
    try:
        return bool(token.get("impersonator_id"))
    except Exception:
        return False


def is_programmer_user(user):
    if not user or not getattr(user, "is_authenticated", False):
        return False
    if getattr(user, "is_superuser", False):
        return True
    role = str(getattr(user, "role", "") or "").strip().lower().replace("-", "_")
    if role == "superadmin":
        role = "super_admin"
    return role in ("developer", "super_admin")


def can_see_all_templates(request):
    user = getattr(request, "user", None)
    return is_programmer_user(user) and not is_impersonating(request)


def can_assign_template_plan(request):
    return can_see_all_templates(request)


def filter_templates_queryset(queryset, request):
    if can_see_all_templates(request):
        return queryset
    user = getattr(request, "user", None)
    return queryset.filter(plan__in=allowed_plans_for(user_plan(user)))


def user_may_use_template(user, template, request=None):
    if request is not None and can_see_all_templates(request):
        return True
    template_plan = normalize_plan(getattr(template, "plan", None))
    return PLAN_RANK[template_plan] <= PLAN_RANK[user_plan(user)]
