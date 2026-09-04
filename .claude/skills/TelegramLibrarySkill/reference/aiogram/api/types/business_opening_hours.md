# BusinessOpeningHours

> Source: [https://docs.aiogram.dev/en/latest/api/types/business_opening_hours.html](https://docs.aiogram.dev/en/latest/api/types/business_opening_hours.html)

*class* aiogram.types.business_opening_hours.BusinessOpeningHours(*\**, *time_zone_name: str*, *opening_hours: list[[BusinessOpeningHoursInterval](business_opening_hours_interval.html#aiogram.types.business_opening_hours_interval.BusinessOpeningHoursInterval "aiogram.types.business_opening_hours_interval.BusinessOpeningHoursInterval")]*, *\*\*extra_data: Any*)
:   Describes the opening hours of a business.

    Source: <https://core.telegram.org/bots/api#businessopeninghours>

    time_zone_name*: str*
    :   Unique name of the time zone for which the opening hours are defined

    opening_hours*: list[[BusinessOpeningHoursInterval](business_opening_hours_interval.html#aiogram.types.business_opening_hours_interval.BusinessOpeningHoursInterval "aiogram.types.business_opening_hours_interval.BusinessOpeningHoursInterval")]*
    :   List of time intervals describing business opening hours
