# BusinessOpeningHoursInterval

> Source: [https://docs.aiogram.dev/en/latest/api/types/business_opening_hours_interval.html](https://docs.aiogram.dev/en/latest/api/types/business_opening_hours_interval.html)

*class* aiogram.types.business_opening_hours_interval.BusinessOpeningHoursInterval(*\**, *opening_minute: int*, *closing_minute: int*, *\*\*extra_data: Any*)
:   Describes an interval of time during which a business is open.

    Source: <https://core.telegram.org/bots/api#businessopeninghoursinterval>

    opening_minute*: int*
    :   The minute’s sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 \* 24 \* 60

    closing_minute*: int*
    :   The minute’s sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 \* 24 \* 60
