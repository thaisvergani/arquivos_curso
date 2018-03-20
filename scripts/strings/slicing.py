s = 'hello world'

# fatiando (incluindo inicio, excluindo o final)
s[1:4]  # -> 'ell'

# a partir do início do índice
s[:4]  # -> 'hell'

# a partir do final do índice
s[3:]  # -> 'lo world'

# pode usar índice negativo também
s[2:-2]  # -> 'llo wor'

# saltos
s[::2]  # -> 'hlowrd'
s[1::2]  # -> 'el ol'

# saltos negativos
s[::-1]  # -> 'dlrow olleh'
