def try_parse_float(text, text_description='', start_idx=0, default=0):
    try:
        return float(text[start_idx:].replace(',', ''))
    except ValueError:
        print(f'ValueError: Tried to parse "{text}" to float!\n')
    except IndexError:
        print(f'{text_description} is not of length <= {start_idx}')
    return default
