# Magic filters

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/filters/magic_filters.html](https://docs.aiogram.dev/en/latest/dispatcher/filters/magic_filters.html)

Note

This page still in progress. Has many incorrectly worded sentences.

Is external package maintained by *aiogram* core team.

By default installs with *aiogram* and also is available on [PyPi - magic-filter](https://pypi.org/project/magic-filter/).
That’s mean you can install it and use with any other libraries and in own projects without depending *aiogram* installed.

## Usage

The **magic_filter** package implements class shortly named `magic_filter.F` that’s mean `F` can be imported from `aiogram` or `magic_filter`. `F` is alias for `MagicFilter`.

Note

Note that *aiogram* has an small extension over magic-filter and if you want to use this extension you should import magic from *aiogram* instead of *magic_filter* package

The `MagicFilter` object is callable, supports [some actions](#magic-filter-possible-actions)
and memorize the attributes chain and the action which should be checked on demand.

So that’s mean you can chain attribute getters, describe simple data validations
and then call the resulted object passing single object as argument,
for example make attributes chain `F.foo.bar.baz` then add
action ‘`F.foo.bar.baz == 'spam'` and then call the resulted object - `(F.foo.bar.baz == 'spam').resolve(obj)`

## Possible actions

Magic filter object supports some of basic logical operations over object attributes

### Exists or not None

Default actions.

```
F.photo  # lambda message: message.photo
```

### Equals

```
F.text == 'hello'  # lambda message: message.text == 'hello'
F.from_user.id == 42  # lambda message: message.from_user.id == 42
F.text != 'spam'  # lambda message: message.text != 'spam'
```

### Is one of

Can be used as method named `in_` or as matmul operator `@` with any iterable

```
F.from_user.id.in_({42, 1000, 123123})  # lambda query: query.from_user.id in {42, 1000, 123123}
F.data.in_({'foo', 'bar', 'baz'})  # lambda query: query.data in {'foo', 'bar', 'baz'}
```

### Contains

```
F.text.contains('foo')  # lambda message: 'foo' in message.text
```

### String startswith/endswith

Can be applied only for text attributes

```
F.text.startswith('foo')  # lambda message: message.text.startswith('foo')
F.text.endswith('bar')  # lambda message: message.text.startswith('bar')
```

### Regexp

```
F.text.regexp(r'Hello, .+')  # lambda message: re.match(r'Hello, .+', message.text)
```

### Custom function

Accepts any callable. Callback will be called when filter checks result

```
F.chat.func(lambda chat: chat.id == -42)  # lambda message: (lambda chat: chat.id == -42)(message.chat)
```

### Inverting result

Any of available operation can be inverted by bitwise inversion - `~`

```
~F.text  # lambda message: not message.text
~F.text.startswith('spam')  # lambda message: not message.text.startswith('spam')
```

### Combining

All operations can be combined via bitwise and/or operators - `&`/`|`

```
(F.from_user.id == 42) & (F.text == 'admin')
F.text.startswith('a') | F.text.endswith('b')
(F.from_user.id.in_({42, 777, 911})) & (F.text.startswith('!') | F.text.startswith('/')) & F.text.contains('ban')
```

### Attribute modifiers - string manipulations

Make text upper- or lower-case

Can be used only with string attributes.

```
F.text.lower() == 'test'  # lambda message: message.text.lower() == 'test'
F.text.upper().in_({'FOO', 'BAR'})  # lambda message: message.text.upper() in {'FOO', 'BAR'}
F.text.len() == 5  # lambda message: len(message.text) == 5
```

### Get filter result as handler argument

This part is not available in *magic-filter* directly but can be used with *aiogram*

```
from aiogram import F

...

@router.message(F.text.regexp(r"^(\d+)$").as_("digits"))
async def any_digits_handler(message: Message, digits: Match[str]):
    await message.answer(html.quote(str(digits)))
```

## Usage in *aiogram*

```
@router.message(F.text == 'hello')
@router.inline_query(F.data == 'button:1')
@router.message(F.text.startswith('foo'))
@router.message(F.content_type.in_({'text', 'sticker'}))
@router.message(F.text.regexp(r'\d+'))

...

# Many others cases when you will need to check any of available event attribute
```
