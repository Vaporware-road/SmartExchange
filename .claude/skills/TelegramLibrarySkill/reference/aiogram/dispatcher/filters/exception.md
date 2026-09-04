# Exceptions

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/filters/exception.html](https://docs.aiogram.dev/en/latest/dispatcher/filters/exception.html)

This filters can be helpful for handling errors from the text messages.

*class* aiogram.filters.exception.ExceptionTypeFilter(*\*exceptions: type[Exception]*)
:   Allows to match exception by type

    exceptions

*class* aiogram.filters.exception.ExceptionMessageFilter(*pattern: str | Pattern[str]*)
:   Allow to match exception by message

    pattern

## Allowed handlers

Allowed update types for this filters:

- `error`
